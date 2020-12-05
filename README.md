# Zolpia-Server
Zolpia는 EEG 센서와 진동 모듈을 이용한 딥러닝 기반의 수면 케어 솔루션 앱 서비스 입니다.

본 레포지토리는 서비스의 서버 부문을 맡았습니다.

## 사용법
1. `git clone https://github.com/AceOfGSM/Zolpia-Server.git` - 깃 클론 생성
2. `cd zolpia-server` - 루트 디렉토리 진입
3. `python -m venv venv` - 가상환경 생성
4. `source venv/bin/activate` - 가상환경 진입
5. `pip install -r requirements.txt` - 필요한 패키지 다운로드
6. `python .\zolia_server\manage.py runserver 0.0.0.0:8000` - 서버(코드) 실행


## API 명세서
[Notion 링크](https://www.notion.so/API-7c450ba99f0345e8acfccc3a41541ba9)