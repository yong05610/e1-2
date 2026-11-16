# 제출 보고서: 파이썬 기초 퀴즈 게임

<img src="docs/quiz_game_overview.png" alt="파이썬 기초 퀴즈 게임 기능 및 구조 요약" width="50%">

## 1. 제출 정보
| 항목 | 내용 |
|---|---|
| GitHub 저장소 | https://github.com/yong05610/e1-2 |
| 주제 | 파이썬 기초 퀴즈 |
| 실행 | `python main.py` (Python 3.12.10, 외부 라이브러리 없음) |

## 2. 개발 환경
| 항목 | 확인 명령 | 결과 |
|---|---|---|
| Python | `python --version` | Python 3.12.10 (3.10 이상 요구 충족) |
| Git | `git --version` | git version 2.55.0.windows.4 |
| 에디터 | VS Code (PowerShell 터미널) | |
| Git 설정 | `git config user.name` / `user.email` | 설정됨 |

> 스크린샷: `docs/screenshots/env.png` (VS Code + 위 3개 명령 실행 화면)

## 3. 미션 요구사항 충족 현황

### 3.1 동작하는 퀴즈 게임
| 요구사항 | 충족 | 근거 |
|---|---|---|
| 메뉴에서 번호 선택 (풀기/추가/목록/점수/종료) | O | `QuizGame.show_menu`, `handle_choice` |
| 퀴즈 5개 이상 (본인 주제) | O | 기본 퀴즈 6개 (`default_quizzes`) |
| 종료 후 재실행해도 퀴즈/최고 점수 유지 | O | `state.json` 저장/불러오기 |
| 잘못된 입력 처리 | O | `read_int`: 공백 제거, 숫자 아님, 범위 밖, 빈 입력 |
| Ctrl+C / EOFError 안전 종료 | O | `run()`의 `try/except/finally` |
| 파일 없음/손상 시 실행 가능 | O | `load_state()`: 없음 → 기본 퀴즈, 손상 → 안내 후 초기화 |

### 3.2 코드 구조
| 요구사항 | 충족 | 근거 |
|---|---|---|
| 클래스 2개 이상 | O | `Quiz` (quiz.py), `QuizGame` (quiz_game.py) |
| 기능별 메서드 분리 | O | 입력(`read_int`, `read_text`) / 진행(`play_quiz`) / 저장(`save_state`, `load_state`) |
| `state.json` UTF-8 저장 | O | `open(..., encoding="utf-8")`, `ensure_ascii=False` |

### 3.3 GitHub 저장소
| 요구사항 | 충족 | 근거 |
|---|---|---|
| 코드가 GitHub에 업로드 | O | origin/main 과 로컬 main 일치 |
| 의미 있는 커밋 10개 이상 | O | 총 23개 (`git rev-list --count HEAD`) |
| 브랜치 생성 및 병합 | O | `feature/play`, `feature/random`, `feature/count` 생성 → 각각 `main`에 병합 (병합 커밋 `ddcfcbb`, `55a3443`, `9cf7e04`) |
| clone, pull 각 1회 이상 | O | 아래 4장 참조 |
| README 필수 항목 | O | 개요, 선정 이유, 실행 방법, 기능 목록, 파일 구조, 데이터 파일 설명 |

## 4. Git 명령 7종 사용 증거
| 명령 | 사용 증거 |
|---|---|
| `git init` | `git reflog`의 첫 기록 `commit (initial): start mission` (a2a9518) |
| `git add` | 모든 커밋 전에 사용 |
| `git commit` | 커밋 23개, `Feat:`/`Fix:`/`Docs:`/`Refactor:` 형식 |
| `git push` | `git push origin main`으로 GitHub에 반영 |
| `git pull` | ① `pull origin main --allow-unrelated-histories` (원격 초기 커밋과 병합, e093db6) ② clone 실습 후 `git pull` (Fast-forward, 4ddaa9f 반영) |
| `git checkout` | `git checkout -b feature/play` → `git checkout main` |
| `git clone` | `e1-2-clone` 폴더에 복제 (`git reflog`: `clone: from https://github.com/yong05610/e1-2.git`) |

### clone/pull 실습 기록
1. `git clone https://github.com/yong05610/e1-2.git` → 별도 폴더 `e1-2-clone`
2. 복제본 README에 한 줄 추가 → `commit` → `push` (4ddaa9f `Docs: clone 실습용 README 한 줄 추가`)
3. 기존 작업 폴더에서 `git pull` (`There is no tracking information` 오류 → `git branch --set-upstream-to=origin/main main` 후 재실행, Fast-forward)
4. `git log`와 README에서 변경 반영 확인

### 브랜치 병합 기록 (`git log --oneline --graph` 일부)
```
*   ddcfcbb Merge branch 'feature/play': 퀴즈 풀기 기능 병합
|\
| * 3bead60 Feat: 퀴즈 출제 기능 구현
|/
* 3761006 Feat: 기본 퀴즈 데이터 추가
```

## 5. 커밋 이력 (기능 단위)
| 단계 | 커밋 |
|---|---|
| 초기 설정 | `Docs: 초기 설정 및 README 뼈대, 미션 문서 정리` |
| 메뉴 | `Feat: 메뉴 및 입력 검증 구현` |
| Quiz 클래스 | `Feat: Quiz 클래스 구현` |
| 기본 퀴즈 | `Feat: 기본 퀴즈 데이터 추가` |
| 퀴즈 풀기 (브랜치) | `Feat: 퀴즈 출제 기능 구현` + 병합 커밋 |
| 퀴즈 추가 | `Feat: 퀴즈 추가 기능 구현` |
| 퀴즈 목록 | `Feat: 퀴즈 목록 기능 구현` |
| 점수 | `Feat: 최고 점수 기능 구현`, `Fix: 점수 출력 문자열 오류 수정` |
| 구조 정리 | `Refactor: Quiz/QuizGame/main 파일 분리 및 메서드 정리` |
| 저장 | `Feat: state.json 저장 및 불러오기 구현 (손상/누락 복구 포함)` |
| README | `Docs: README 작성` (9a87b09) |
| 보너스: 랜덤 출제 (브랜치) | `Feat: 퀴즈 랜덤 출제 구현 (random.shuffle)` + 병합 커밋 |
| 보너스: 문제 수 선택 (브랜치) | `Feat: 풀 문제 수 선택 기능 구현` + 병합 커밋 |
| 제출물 정리 | `Docs: 제출 보고서, 스크린샷, README 갱신` |

### 보너스 기능 (선택 과제 중 2개 구현)
| 기능 | 구현 | 검증 |
|---|---|---|
| 랜덤 출제 | `play_quiz`에서 퀴즈 목록을 복사해 `random.shuffle`로 섞어 출제 (원본 목록 순서는 유지) | 5회 실행 시 모두 다른 순서, 전체 문제가 한 번씩만 출제 |
| 문제 수 선택 | 풀기 시작 시 `read_int`로 1 ~ 전체 문제 수를 입력받아 섞은 목록의 앞에서 N개 사용 | 3, 전체, 1 입력 확인 / `abc`, 빈 입력, 0, 범위 초과는 재입력 / 결과는 선택한 문제 수 기준 |

## 6. 실행 결과
실제 실행 화면은 7장의 스크린샷을 참고합니다. 요약은 다음과 같습니다.
```
📂 저장된 데이터를 불러왔습니다. (퀴즈 11개, 최고점수 83점)
선택: 2  →  ✅ 퀴즈가 추가되었습니다!   (퀴즈 12개)
선택: 1  →  풀 문제 수 (1-11): 5  →  📝 퀴즈를 시작합니다! (총 5문제)
선택: 4  →  🏆 최고 점수: 100점 (5문제 중 5문제 정답)
```
재실행해도 추가한 퀴즈와 최고 점수가 `state.json`에서 그대로 불러와집니다.

### 입력 오류 처리 확인
| 입력 | 결과 |
|---|---|
| `abc` | `⚠️ 잘못된 입력입니다. 1-5 사이의 숫자를 입력하세요.` |
| `9` | `⚠️ 범위를 벗어났습니다. 1-5 사이의 숫자를 입력하세요.` |
| (빈 Enter) | `⚠️ 입력이 비어 있습니다. 1-5 사이의 숫자를 입력하세요.` |
| ` 1 ` (공백 포함) | 공백 제거 후 1번으로 처리 |
| Ctrl+C / 입력 종료 | `⚠️ 입력이 중단되었습니다. 저장 후 안전하게 종료합니다.` |
| `state.json` 손상 | `⚠️ 데이터 파일이 손상되어 기본 퀴즈로 초기화합니다.` |

## 7. 스크린샷 (`docs/screenshots/`)
| 파일 | 내용 | 이미지 |
|---|---|---|
| `env.png` | Python 3.12.10, git 2.55.0, `git config user.name` | ![env](docs/screenshots/env.png) |
| `menu.png` | 실행 직후 메뉴 화면 | ![menu](docs/screenshots/menu.png) |
| `add_quiz.png` | 2번 퀴즈 추가 입력 과정과 `✅ 퀴즈가 추가되었습니다!` | ![add_quiz](docs/screenshots/add_quiz.png) |
| `list.png` | 3번 퀴즈 목록 | ![list](docs/screenshots/list.png) |
| `play.png` | 1번 퀴즈 풀기 (풀 문제 수 선택 후 무작위 출제) | ![play](docs/screenshots/play.png) |
| `score.png` | 4번 점수 확인 | ![score](docs/screenshots/score.png) |
| `git_graph.png` | `git log --oneline --graph` (브랜치 병합 기록) | ![git_graph](docs/screenshots/git_graph.png) |

> `git_graph.png`는 보너스 브랜치 병합 직전의 그래프입니다. 최종 이력은 `git log --oneline --graph`로 확인할 수 있습니다.
