# 시스템 전체 설계 (System Design)

**Cline 필수 읽기 문서** — Python + Flask + SQLite 프로젝트

## 1. 프로젝트 개요
- 언어: Python 3.11+
- 웹 프레임워크: Flask (Blueprint + Application Factory 패턴 사용)
- 데이터베이스: SQLite (초기 뼈대용, 나중에 PostgreSQL 등으로 전환 가능)
- 목표: 확장 가능하고 유지보수하기 쉬운 Flask 애플리케이션

## 2. 고수준 아키텍처
- Application Factory 패턴 (`create_app()`)
- Blueprint로 모듈화 (routes, services, models 분리)
- Layered 구조: routes → services → models/repositories
