import csv
import json
import re
from datetime import datetime

CONFIG_JSON = '''
{
    "start_row_pattern": "conveyorBoxMap controller called",
    "start_row_merge_key_pattern": ", pid=(\\\d+),",
    "end_row_pattern": "conveyorBoxMap call. auto labeller",
    "end_row_merge_key_pattern": ",{merge_key},",
    "merge_key_name": "pid"
}
'''

input_file = './kibana-log.csv'
output_file = './kibana-log-out.csv'

def to_timestamp_ms(timstamp_str):
    return int(datetime.strptime(timstamp_str, "%b %d, %Y @ %H:%M:%S.%f").timestamp() * 1000)

def format_timestamp_ms(timestamp_ms):
    timestamp = datetime.fromtimestamp(timestamp_ms/1000.0)
    return timestamp.strftime('%Y-%m-%d_%H:%M:%S.%f')[:-3]


class ProcessContext:
    def __init__(self, writer, config):
        self.start_time = None
        self.merge_key = None
        self.writer = writer
        self.config = config

    def update_start_row(self, start_time, merge_key):
        self.start_time = start_time
        self.merge_key = merge_key

    def reset(self):
        self.start_time = None
        self.merge_key = None

def process_row(row, context):
    message = row['message']
    timestamp_str = row['@timestamp']

    start_time = context.start_time
    # Check if this is a starting row
    if message.startswith(context.config['start_row_pattern']):
        merge_key_match = re.search(context.config['start_row_merge_key_pattern'], message)
        if merge_key_match:
            context.update_start_row(to_timestamp_ms(timestamp_str), merge_key_match.group(1))

    # Check if this is an ending row
    elif message.startswith(context.config['end_row_pattern']) and context.merge_key is not None:
        merge_key_match = re.search(context.config['end_row_merge_key_pattern'].format(merge_key=context.merge_key), message)
        if merge_key_match:
            end_time = to_timestamp_ms(timestamp_str)
            time_diff_ms = end_time - start_time

            context.writer.writerow([format_timestamp_ms(start_time),
                                     format_timestamp_ms(end_time),
                                     context.merge_key,
                                     time_diff_ms])
            context.reset()

def process_csv(input_file, output_file, config_json):

    config = json.loads(config_json)

    with open(input_file, 'r') as csv_file:
        reader = list(csv.DictReader(csv_file))
        reader.reverse()

        with open(output_file, 'w') as output_file:
            writer = csv.writer(output_file)
            writer.writerow(['start date', 'end date', config['merge_key_name'], 'time difference ms'])

            context = ProcessContext(writer, config)

            for row in reader:
                process_row(row, context)

process_csv(input_file, output_file, CONFIG_JSON)
