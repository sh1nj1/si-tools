# Git Diff to CSV

## Description

This script parses the output of a git diff command, extracts the modified and
added files with full path from the root, and creates a csv file with the following
columns:

```
● "module" which is the first path of the file and the last word of that path
● "full path" which is the full path of the file from the root
● "file name" which is the name of the file
● "commit message" which is the last commit message for the file.
```
The commit message column is cut to 80 characters if it's longer, and the charset is
assumed to be UTF-8.

## Usage

Make sure you're in the git repository directory before running the script.

You can run the script using the following command:

Copy code

git diff--name-only--diff-filter=ACMRTUXB | pythonscript.py> path/to/csv/file

This command will pipe the output of the git diff command to the script and
redirect the output to a csv file at the specified path.

Please note that this script assumes that you have git installed on your system and
available in PATH.

## Additional Note

You can make changes to the script as per your requirement, for example if you
want to extract different columns or if you want to extract data from other source.


## Troubleshooting

In case of any issues, please check the stdout for error messages and make sure
that you're in a git repository directory before running the script.

## Author

OpenAI



