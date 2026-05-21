# Git Convention

## 브랜치 전략
- main : 최종 제출
- develop : 팀 공용 작업 브랜치

---

## 작업 순서

### 1. 최신 코드 받기
```bash
git pull origin develop
```

### 2. 작업 진행

담당 파일 수정

### 3. 변경사항 저장
```bash
git add .
git commit -m "feat: 작업 내용"
```

### 4. 원격 저장소 반영
```bash
git push origin develop
```

---

## Commit Message Rule

- feat : 기능 추가
- fix : 오류 수정
- docs : 문서 수정
- chore : 기타 설정
- refactor : 코드 구조 개선

---

## 협업 규칙
- 작업 시작 전 반드시 pull
- 동일 파일 동시 수정 지양
- 충돌 발생 시 즉시 공유
- 의미 없는 커밋명 금지
