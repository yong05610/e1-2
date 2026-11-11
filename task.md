# TASK: 파이썬 기초 퀴즈 게임 작업 목록

> 기준 문서: `PRD.md`, `mission.md`
> 진행 방법: 위에서 아래로 순서대로 진행하고, 단계가 끝나면 체크(`[x]`)하고 커밋한다.

## Task 0. 준비
- [ ] `python --version`으로 3.10 이상인지 확인
- [ ] `git remote -v`로 origin 주소 확인 (`https://github.com/yong05610/e1-2.git`)
- [ ] `git status`로 현재 상태 확인 (이름 바꾼 mission 파일, PRD.md, task.md 정리)
- [ ] 퀴즈 주제 확정: **파이썬 기초**

## Task 1. 저장소 설정
- [ ] `.gitignore` 생성 (`__pycache__/`, `*.pyc`, `.vscode/` 등)
- [ ] `README.md` 뼈대 작성 (제목, 개요, 주제 선정 이유)
- [ ] `git add` → `git commit` → `git push`
- 커밋: `Docs: 초기 설정 및 README 뼈대`

## Task 2. 메뉴 기능
- [ ] `main.py` 생성
- [ ] `QuizGame` 클래스 뼈대 (`__init__`, `run`, `show_menu`)
- [ ] 메뉴 출력 (1.퀴즈 풀기 2.퀴즈 추가 3.퀴즈 목록 4.점수 확인 5.종료)
- [ ] `read_int(prompt, lo, hi)` 구현
  - [ ] 앞뒤 공백 제거
  - [ ] 숫자가 아닐 때 안내 후 재입력
  - [ ] 범위 밖 숫자일 때 안내 후 재입력
  - [ ] 빈 입력일 때 안내 후 재입력
- [ ] 선택 번호에 따른 분기 (아직 없는 기능은 "준비 중" 출력)
- [ ] 5번 종료 동작
- [ ] Ctrl+C / EOFError 처리 후 안전 종료
- [ ] 직접 실행해 확인: `abc`, `9`, 빈 Enter, ` 1 `, Ctrl+C
- 커밋: `Feat: 메뉴 및 입력 검증 구현`

## Task 3. Quiz 클래스
- [ ] `Quiz` 클래스 작성 (`question`, `choices`, `answer`)
- [ ] `display(index)`: 문제와 선택지 출력
- [ ] `is_correct(user_answer)`: 정답 여부 반환
- [ ] `to_dict()` / `from_dict()` 작성 (저장 대비)
- [ ] 임시로 객체 1개를 만들어 출력과 정답 확인 테스트
- 커밋: `Feat: Quiz 클래스 구현`

## Task 4. 기본 퀴즈 데이터
- [ ] `default_quizzes()` 작성, `Quiz` 인스턴스 5개 이상 (PRD 6장 초안 사용)
- [ ] 각 퀴즈의 선택지 4개, 정답 번호(1~4) 확인
- [ ] `QuizGame.quizzes`에 기본 퀴즈 로드
- 커밋: `Feat: 기본 퀴즈 데이터 추가`

## Task 5. 퀴즈 풀기 (브랜치 사용)
- [ ] 브랜치 생성: `git checkout -b feature/play`
- [ ] `play_quiz()` 구현
  - [ ] 퀴즈가 없으면 안내 후 메뉴로 복귀
  - [ ] 문제 출력과 정답 입력 (`read_int` 재사용, 1~4)
  - [ ] 정답/오답 안내 (오답이면 정답 번호 표시)
  - [ ] 모두 풀면 결과 표시 (`N문제 중 M문제 정답! (점수)`)
- [ ] 메뉴 1번과 연결해 직접 실행 확인
- [ ] 커밋: `Feat: 퀴즈 출제 기능 구현`
- [ ] 병합: `git checkout main` → `git merge feature/play`
- [ ] `git push`

## Task 6. 퀴즈 추가
- [ ] `add_quiz()` 구현
  - [ ] 문제 입력 (빈 값이면 재입력)
  - [ ] 선택지 4개 입력 (빈 값이면 재입력)
  - [ ] 정답 번호 입력 (1~4)
  - [ ] `Quiz` 생성 후 `quizzes`에 추가
- [ ] 메뉴 2번과 연결해 직접 실행 확인
- 커밋: `Feat: 퀴즈 추가 기능 구현`

## Task 7. 퀴즈 목록
- [ ] `list_quizzes()` 구현 (`[번호] 문제`, 총 개수 표시)
- [ ] 퀴즈가 없을 때 안내 메시지
- [ ] 메뉴 3번과 연결해 직접 실행 확인
- 커밋: `Feat: 퀴즈 목록 기능 구현`

## Task 8. 점수 확인
- [ ] `best_score`, `best_total` 속성 추가 (초기값 `None`)
- [ ] `play_quiz()` 종료 시 최고 점수와 비교하고 갱신
- [ ] 갱신되면 `🎉 새로운 최고 점수입니다!` 표시
- [ ] `show_score()` 구현, 아직 안 푼 경우 안내 메시지
- [ ] 메뉴 4번과 연결해 직접 실행 확인
- 커밋: `Feat: 최고 점수 기능 구현`

## Task 9. QuizGame 구조 정리
- [ ] 메서드 분리 상태 점검 (한 메서드가 한 가지 일만 하는지)
- [ ] 중복 코드 정리, 메서드 이름 통일
- [ ] 필요하면 `quiz.py`, `quiz_game.py`로 파일 분리
- [ ] 정리 후에도 모든 기능이 동일하게 동작하는지 확인
- 커밋: `Refactor: QuizGame 책임 분리`

## Task 10. 파일 저장/불러오기 (`state.json`)
- [ ] `save_state()`: `quizzes`, `best_score`, `best_total`을 UTF-8, `ensure_ascii=False`, `indent=4`로 저장
- [ ] `load_state()`: 시작 시 불러오기
- [ ] 파일이 없을 때 기본 퀴즈 사용
- [ ] 파일이 손상되었을 때 안내 메시지 후 기본 퀴즈로 초기화
- [ ] 읽기/쓰기 오류를 `try/except`로 처리
- [ ] 퀴즈 추가, 최고 점수 갱신, 종료 시 `save_state()` 호출
- [ ] 시작 시 `📂 저장된 데이터를 불러왔습니다. (퀴즈 N개, 최고점수 M점)` 표시
- [ ] 테스트: 퀴즈 추가 후 종료 → 재실행 시 유지되는지
- [ ] 테스트: `state.json` 삭제 후 실행, 내용 일부를 지워 손상시킨 뒤 실행
- 커밋: `Feat: JSON 저장 및 불러오기 구현`

## Task 11. README 작성
- [ ] 프로젝트 개요
- [ ] 퀴즈 주제와 선정 이유
- [ ] 실행 방법 (`python main.py`)
- [ ] 기능 목록 (풀기/추가/목록/점수)
- [ ] 파일 구조
- [ ] 데이터 파일 설명 (`state.json` 경로/역할/스키마)
- [ ] 실행 화면 스크린샷 링크 (`docs/screenshots/...`)
- [ ] `git push`
- 커밋: `Docs: README 작성`

## Task 12. clone / pull 실습
- [ ] 다른 폴더에 `git clone https://github.com/yong05610/e1-2.git`
- [ ] 복제본에서 README에 한 줄 추가 후 commit → push
- [ ] 기존 작업 폴더에서 `git pull`
- [ ] pull 결과가 반영되었는지 확인 (`git log`, README 확인)

## Task 13. 최종 점검 및 제출물
- [ ] `git log --oneline` 기준 커밋 10개 이상인지 확인
- [ ] 브랜치 생성/병합 기록 확인
- [ ] Git 명령 7종 사용 확인: init, add, commit, push, pull, checkout, clone
- [ ] PRD 9장 완료 기준 체크리스트 전부 확인
- [ ] 스크린샷 촬영
  - [ ] 개발환경 (VS Code, Python 버전, Git 설정)
  - [ ] 퀴즈 추가 (`docs/screenshots/add_quiz.png`)
  - [ ] 퀴즈 목록
  - [ ] 퀴즈 플레이 (`docs/screenshots/play.png`)
  - [ ] 점수 확인 (`docs/screenshots/score.png`)
  - [ ] 메뉴 (`docs/screenshots/menu.png`)
  - [ ] `git log --oneline --graph`
- [ ] 최종 `git push`
- [ ] GitHub 저장소 URL 제출

## Task 14. 보너스 (선택)
- [ ] 랜덤 출제 (`random` 모듈)
- [ ] 문제 수 선택
- [ ] 힌트 기능 (점수 차감)
- [ ] 퀴즈 삭제
- [ ] 점수 기록 히스토리 (날짜/시간, 푼 문제 수, 점수)
