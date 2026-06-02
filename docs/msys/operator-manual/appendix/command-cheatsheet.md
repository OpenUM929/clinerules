# 자주 쓰는 명령어 모음

## 서비스 제어

```bash
# 기동
./start_moni.sh

# 중지
./kill_data_moni.sh

# 프로세스 확인
ps -ef | grep msys
```

## 로그 확인

```bash
# 실시간
tail -f /data/external_data_monitoring/log/external_data_monitoring.log

# 오늘 100줄
tail -n 100 /data/external_data_monitoring/log/external_data_monitoring.log

# 오류 검색
grep "ERROR" /data/external_data_monitoring/log/external_data_monitoring.log
```

## DB 명령어

```bash
# 접속
psql -h [DB_HOST] -U [DB_USER] -d [DB_NAME]

# 테이블 목록
\dt

# 사용자 조회
SELECT * FROM tb_user;

# 세션 종료
\q
```

---

> 다음 문서: [config-reference.md](config-reference.md)
