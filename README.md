# Git Diff를 CSV로


git diff 로 부터 특정 보고를 위한 엑셀을 만들때 사용할 수 있다.


## 설명

이 스크립트는 git diff 명령의 출력을 구문 분석하고 수정된
루트에서 전체 경로로 파일을 추가하고 다음을 사용하여 csv 파일을 만듭니다.
열:


* 파일의 첫 번째 경로이자 해당 경로의 마지막 단어인 "module"
* 루트에서 파일의 전체 경로인 "전체 경로"
* 파일 이름인 '파일 이름'
* 파일에 대한 마지막 커밋 메시지인 "커밋 메시지".

커밋 메시지 열은 더 길면 80자로 잘리고 문자셋은
UTF-8로 가정합니다.

## 용법

스크립트를 실행하기 전에 git 저장소 디렉토리에 있는지 확인하십시오.

다음 명령을 사용하여 스크립트를 실행할 수 있습니다.

Linux-Like (Linux, Windows WSL, Mac OS) 환경:
```
git diff "대상 브랜치" | COLUMNS="구분,경로,파일명,사유,QA서버 반영일" python gen-diff-summary-csv.py > diff.csv
```

Windows 환경:
```
set "COLUMNS=구분,경로,파일명,사유,QA서버 반영일"
git diff "대상 브랜치" > temp.diff
python gen-diff-summary-csv.py temp.diff > diff.csv
```

이 명령은 git diff 명령의 출력을 스크립트로 파이프하고
출력을 지정된 경로의 csv 파일로 리디렉션합니다.

이 스크립트는 시스템에 git이 설치되어 있고
PATH에서 사용할 수 있습니다.

## 추가 참고 사항

예를 들어 다음과 같은 경우 요구 사항에 따라 스크립트를 변경할 수 있습니다.
다른 열을 추출하거나 다른 소스에서 데이터를 추출하려는 경우.


## 문제 해결

문제가 있는 경우 stdout에서 오류 메시지를 확인하고 다음을 확인하십시오.
스크립트를 실행하기 전에 git 저장소 디렉토리에 있음을 확인하십시오.

## 기여자

OpenAI
