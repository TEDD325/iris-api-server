poetry run uvicorn app.main:app --host 0.0.0.0 --port $PORT
# start.sh는 로컬 테스트시에 사용
# entrypoint.sh를 클라우드 배포 시에 사용
