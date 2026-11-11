# 시험 대비 스터디 노트 (과제 목표 3번 기준)

> 읽는 순서: **0. 전체 지도 → 1~4. 목표별 정리 → 5. 코드 따라가기 → 6. 예상 문제**
> 예시는 모두 이 프로젝트 코드(`quiz.py`, `quiz_game.py`, `main.py`)에서 가져왔습니다.
> 개념은 Visual Basic / 슈도코드와 비교해서 적었습니다.

---

## 0. 전체 지도

```
main.py ──실행──▶ QuizGame().run()
                    │ 메뉴 루프 (while)
                    ├─ 1 play_quiz()   ← Quiz.display / Quiz.is_correct
                    ├─ 2 add_quiz()    ← Quiz(...) 객체 생성
                    ├─ 3 list_quizzes()
                    ├─ 4 show_score()
                    └─ 5 종료
        시작할 때 load_state()  /  바뀔 때마다 save_state()  ⇄  state.json
```

---

## 1. Python 기초

### 1-1. 변수란? 왜 쓰나?
**값에 이름을 붙여 저장해 두는 상자.** 같은 값을 여러 번 쓰고, 나중에 바꿀 수 있게 하려고 쓴다.

| VB | Python |
|---|---|
| `Dim score As Integer` <br> `score = 80` | `score = 80` (타입 선언 없음, 값을 넣으면 타입이 정해짐) |

- 코드 예: `correct = 0` → 정답 수를 세는 변수, `correct += 1`로 증가.
- Python은 **동적 타입**: 같은 변수에 나중에 다른 타입도 넣을 수 있다 (권장하진 않음).

### 1-2. int, str, bool, list, dict 차이

| 타입 | 의미 | 예 | 이 프로젝트에서 |
|---|---|---|---|
| `int` | 정수 | `80`, `-3` | 점수 `score`, 정답 번호 `answer` |
| `str` | 문자열 | `"안녕"` | 문제 `question` |
| `bool` | 참/거짓 | `True`, `False` | `running`, `is_correct()` 반환값 |
| `list` | **순서 있는** 목록, 번호(0부터)로 접근, 수정 가능 | `["a","b"]` | 선택지 `choices`, 퀴즈 목록 `quizzes` |
| `dict` | **키-값** 쌍, 키로 접근 | `{"answer": 2}` | `to_dict()` 결과, state.json 내용 |

- VB 비교: `list` ≈ 배열/`List(Of T)`, `dict` ≈ `Dictionary(Of K, V)`. 단, Python list의 **첫 인덱스는 0**.
- `tuple`은 list와 비슷하지만 **수정 불가**. (퀴즈 3번 보기에도 등장)
- 구분 포인트: **순서/번호로 찾으면 list, 이름(키)으로 찾으면 dict.**
- 괄호 기호: `[]` list, `{}` dict, `()` tuple.
- `None`: "값이 없음" (VB의 `Nothing`). 코드에서 `best_score = None` = 아직 안 풀었음.

### 1-3. if / elif / else
```python
if choice == 1:
    self.play_quiz()
elif choice == 2:
    self.add_quiz()
else:
    ...
```
- VB: `If ... ElseIf ... Else ... End If` → Python은 `End If` 대신 **들여쓰기(4칸)와 `:`** 로 블록을 표시한다.
- `elif`는 앞 조건이 거짓일 때만 검사. `loop`는 키워드가 아님 (퀴즈 4번 정답).
- 비교는 `==`, 대입은 `=`.

### 1-4. for와 while
| | for | while |
|---|---|---|
| 언제 | **횟수/대상이 정해져 있을 때** (목록 전체 순회) | **조건이 참인 동안** 반복 (끝을 모를 때) |
| 코드 | `for quiz in self.quizzes:` (퀴즈 목록 전체) | `while self.running:` (사용자가 종료할 때까지), `while True:` + `return`/`continue` (올바른 입력이 올 때까지) |
| VB | `For Each` / `For i = 1 To n` | `Do While ... Loop` |

- `enumerate(list, start=1)`: 번호와 값을 같이 꺼냄 (`1. 보기` 출력에 사용).
- `break` 반복 탈출, `continue` 이번 회차 건너뛰고 다음 반복.

### 1-5. 함수: 매개변수와 반환값
```python
def read_int(self, prompt, low, high):   # 매개변수 3개 (self는 별도 설명)
    ...
    return number                        # 반환값
```
- VB: `Function ReadInt(prompt, low, high) As Integer` … `Return number`
- **매개변수(parameter)** = 함수가 받는 입력 / **반환값(return value)** = 함수가 돌려주는 결과.
- `return` 없으면 `None` 반환. `print`는 화면 출력일 뿐 반환값이 아니다.
- 이 프로젝트의 반환값 예: `is_correct()`는 `True/False`, `update_best_score()`는 갱신 여부 `True/False`.
- 함수를 나누는 이유: 한 번 만들어 재사용(예: `read_int`를 메뉴, 정답, 추가에서 모두 사용), 읽기 쉬움, 수정 쉬움.

---

## 2. 클래스와 객체

### 2-1. 클래스란? 왜 쓰나?
- **클래스 = 설계도, 객체(인스턴스) = 설계도로 만든 실물.** 관련된 데이터(속성)와 동작(메서드)을 한 덩어리로 묶는다.
- VB의 `Class`와 같은 개념. 예: `Quiz`는 설계도, `Quiz("문제", [...], 2)`는 퀴즈 1개(객체).
- 쓰는 이유: 역할별로 구조화 → 이해/수정/재사용이 쉬움. 이 프로젝트: `Quiz`(문제 1개) / `QuizGame`(게임 전체 관리).

### 2-2. `__init__`과 `self`
```python
class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer
```
- `__init__` = **생성자.** 객체를 만들 때 **자동 호출**되어 속성의 초기값을 정한다. (VB의 `Sub New()`)
- `self` = **만들어지는/호출한 그 객체 자기 자신.** (VB의 `Me`) 모든 메서드의 첫 매개변수로 적는다. 호출할 때는 쓰지 않는다: `quiz.display(1)` (내부적으로 `self=quiz`).
- `self.question = question` → "이 객체의 question 속성에 값을 저장".

### 2-3. 속성과 메서드
| | 의미 | 예 |
|---|---|---|
| 속성(attribute) | 객체가 가진 **데이터(변수)** | `quiz.question`, `game.best_score` |
| 메서드(method) | 객체가 하는 **동작(함수)** | `quiz.display()`, `game.play_quiz()` |

- 호출: `객체.메서드()` / 접근: `객체.속성`
- 클래스 변수 `LINE = "=" * 40`: 모든 객체가 공유하는 값 (`self.LINE`로 사용).
- `@classmethod from_dict(cls, data)`: 객체 없이 클래스로 호출해 **객체를 만들어 돌려주는** 메서드. `Quiz.from_dict(...)`
- `to_dict()` ⇄ `from_dict()`: 객체 ↔ dict 변환 (JSON 저장/불러오기용).

---

## 3. 파일 입출력

### 3-1. 파일 열고, 읽고, 쓰는 기본 과정
**열기 → 읽기/쓰기 → 닫기**
```python
with open("state.json", "r", encoding="utf-8") as f:   # 읽기
    data = json.load(f)

with open("state.json", "w", encoding="utf-8") as f:   # 쓰기
    json.dump(data, f, ensure_ascii=False, indent=4)
```
- 모드: `"r"` 읽기, `"w"` 쓰기(기존 내용 덮어씀), `"a"` 이어쓰기.
- `with` 블록이 끝나면 **자동으로 파일을 닫는다** (VB `Using`과 비슷). 닫는 것을 잊지 않게 해 준다.
- `encoding="utf-8"`: 한글이 깨지지 않게 하는 문자 인코딩 지정.
- `ensure_ascii=False`: 한글을 `\uXXXX`가 아닌 **그대로** 저장. `indent=4`: 보기 좋게 들여쓰기.
- 모듈 사용: `import json`, `import os` (`os.path.exists`로 파일 존재 확인).

### 3-2. JSON이란? 왜 쓰나?
- **JavaScript Object Notation.** 데이터를 `{ "키": 값 }`, `[ ... ]` 형태의 **텍스트**로 표현하는 형식.
- Python의 dict/list와 모양이 거의 같아 **변환이 쉽다**: `json.dump`(Python → 파일), `json.load`(파일 → Python).
- 쓰는 이유: 사람이 읽을 수 있음, 언어/시스템에 상관없이 표준, 프로그램 종료 후에도 데이터 유지 (**데이터 영속성**).
- 주의: JSON에서 `None`은 `null`, `True`는 `true`. 문자열은 반드시 큰따옴표.

### 3-3. try / except 오류 처리
```python
try:
    number = int(text)          # "abc"이면 오류 발생
except ValueError:
    print("잘못된 입력입니다.")   # 오류가 나면 여기 실행
```
- VB의 `On Error` / `Try ... Catch ... End Try`와 같은 개념. 오류가 나도 프로그램이 **비정상 종료하지 않고** 대처하게 한다.
- 이 프로젝트에서 처리하는 오류:
  | 오류 | 발생 상황 |
  |---|---|
  | `ValueError` | `int("abc")` 숫자 변환 실패 |
  | `json.JSONDecodeError` | state.json이 깨졌을 때 |
  | `KeyError` | JSON에 `quizzes` 키가 없을 때 |
  | `OSError` | 파일 읽기/쓰기 실패 |
  | `KeyboardInterrupt` | Ctrl+C |
  | `EOFError` | 입력 스트림이 끝났을 때 |
- `finally`: 오류 여부와 상관없이 **항상 실행** (이 프로젝트: 종료 시 `save_state()`).

---

## 4. Git 기초

### 4-1. Git이란? 왜 필요한가?
- **분산 버전 관리 시스템.** 파일의 변경 이력을 기록해 두는 도구.
- 필요한 이유: 이전 상태로 되돌리기, 누가 언제 무엇을 바꿨는지 추적, 브랜치로 안전하게 새 기능 개발, GitHub로 백업/협업.
- Git ≠ GitHub. **Git = 도구(로컬), GitHub = Git 저장소를 올려두는 웹 서비스(원격).**

### 4-2. 명령어 7종

| 명령 | 하는 일 | 이 프로젝트에서 |
|---|---|---|
| `git init` | 현재 폴더를 새 Git 저장소로 만듦 (`.git` 생성) | 저장소 처음 설정 |
| `git add` | 변경 파일을 **스테이징(커밋 대기)** 영역에 올림 | `git add main.py` |
| `git commit` | 스테이징된 변경을 **이력(스냅샷)으로 저장** | `git commit -m "Feat: ..."` |
| `git push` | 내 **로컬 커밋을 원격(GitHub)에 올림** | `git push origin main` |
| `git pull` | **원격 변경을 가져와(fetch) 내 브랜치에 병합(merge)** | clone 실습 후 반영 |
| `git checkout` | **브랜치를 이동**(또는 `-b`로 새로 만들며 이동) | `git checkout -b feature/play` |
| `git clone` | **원격 저장소를 통째로 복제**해 새 로컬 폴더 생성 | 실습용 복제 |

- 흐름: **작업 폴더 → (add) → 스테이징 → (commit) → 로컬 저장소 → (push) → 원격 저장소**, 반대로 **(pull)**.
- 보조 명령: `git status`(상태), `git log --oneline --graph`(이력), `git remote -v`(원격 확인), `git merge`(병합), `git branch`(브랜치 목록).
- 최신 Git에서는 `checkout` 대신 `git switch`(브랜치 이동), `git restore`(파일 복원)도 쓰지만, 이 과제는 `checkout` 기준.

### 4-3. 브랜치 생성과 병합
```
git checkout -b feature/play    # 브랜치 생성 + 이동
# ... 작업, add, commit ...
git checkout main               # main으로 이동
git merge feature/play          # feature/play를 main에 병합
```
- 브랜치 = **독립된 작업 갈래.** main을 건드리지 않고 새 기능을 개발하기 위해 사용.
- 병합 방식: main에 새 커밋이 없으면 **fast-forward**(그냥 앞으로 이동), 갈라졌으면 **merge commit** 생성 (이 프로젝트는 `--no-ff`로 병합 기록을 남김 → `git log --graph`에 갈래가 보임).
- **충돌(conflict):** 같은 부분을 양쪽에서 다르게 고쳤을 때 → 직접 정리 후 `add`, `commit`.

### 4-4. clone과 pull
- `git clone <URL>`: 처음 한 번, 저장소 전체를 복제 (이력 포함, `origin` 자동 설정).
- `git pull`: 이미 있는 저장소에서 **원격의 새 커밋을 가져와 반영**. (`fetch` + `merge`)
- 실습 시나리오: ① 다른 폴더에 clone → ② 복제본에서 수정, commit, push → ③ 원래 폴더에서 pull → ④ 반영 확인.
- 이 과제에서 겪은 오류들(실전 지식):
  | 오류 | 원인/해결 |
  |---|---|
  | `Could not resolve host: github.com` | 네트워크/DNS 문제 |
  | `refusing to merge unrelated histories` | 로컬과 원격의 시작 커밋이 서로 달라서 → `--allow-unrelated-histories` |
  | push 거절 (non-fast-forward) | 원격에 내 로컬에 없는 커밋이 있음 → 먼저 pull |
  | remote URL이 두 번 붙음 | `git remote set-url origin <URL>`로 수정 |

### 4-5. 커밋 메시지 규칙 (이 과제)
`Feat:` 기능 추가 / `Fix:` 오류 수정 / `Docs:` 문서 / `Refactor:` 구조 개선(동작 변화 없음)

---

## 5. 코드 따라가기 (실행 흐름)

`python main.py` 를 실행하면:
1. `main.py` → `QuizGame()` 객체 생성 → `__init__` 실행 → 속성 초기화 → `load_state()` 호출
2. `load_state()`: `state.json` 없음 → 기본 퀴즈 / 있음 → 읽어서 `Quiz` 객체 목록으로 변환 / 깨짐 → 안내 후 기본값
3. `run()`: `while self.running:` 안에서 `show_menu()` → `read_int("선택: ", 1, 5)` → `handle_choice()`
4. `read_int`: 빈 입력 → 안내, `int()` 실패(`except ValueError`) → 안내, 범위 밖 → 안내, 모두 통과해야 `return`
5. 1번 `play_quiz()`: 퀴즈 없으면 안내 후 `return`. 있으면 `for`로 한 문제씩 `display` → 입력 → `is_correct` → 정답 수 집계 → 점수 `correct * 100 // total` → `update_best_score` → 갱신 시 `save_state()`
6. 2번 `add_quiz()`: `read_text`(빈 값 거부) ×5 입력 → `Quiz(...)` 생성 → `quizzes.append` → `save_state()`
7. 5번 또는 Ctrl+C/EOF: `running=False` 또는 `except` → `finally`에서 `save_state()` 후 종료

### VB 슈도코드로 본 핵심 로직 (`read_int`)
```vb
Function ReadInt(prompt, low, high) As Integer
    Do While True
        text = Trim(InputBox(prompt))
        If text = "" Then
            Print "비어 있음" : Continue Do
        End If
        If Not IsNumeric(text) Then
            Print "숫자 아님" : Continue Do
        End If
        number = CInt(text)
        If number < low Or number > high Then
            Print "범위 밖" : Continue Do
        End If
        Return number
    Loop
End Function
```
Python 코드와 한 줄씩 대응: `.strip()` = `Trim`, `int()` = `CInt`, `try/except` = 숫자 변환 오류 처리, `continue` = `Continue Do`.

---

## 6. 예상 문제와 모범 답안

**Q1. 변수란 무엇이고 왜 사용하는가?**
값을 저장하고 이름으로 다시 사용하기 위한 메모리 공간의 이름. 같은 값을 반복 사용하고 상황에 따라 값을 바꿀 수 있게 하려고 쓴다.

**Q2. list와 dict의 차이는?**
list는 순서가 있고 인덱스(0부터)로 접근, dict는 키로 값에 접근하는 키-값 쌍. 예) `choices`는 list, 퀴즈 데이터 하나는 dict(`to_dict`).

**Q3. `"3"`과 `3`의 차이는? / `input()`이 돌려주는 타입은?**
`"3"`은 str, `3`은 int. `input()`은 항상 str을 반환하므로 숫자로 쓰려면 `int()`로 변환해야 하고, 이때 실패하면 ValueError.

**Q4. for와 while 중 언제 어느 것을 쓰나?**
반복 횟수나 대상이 정해져 있으면 for(퀴즈 목록 순회), 조건이 만족되는 동안/올바른 입력이 올 때까지 반복이면 while(메뉴 루프, 입력 재요청).

**Q5. 함수의 매개변수와 반환값을 설명하라.**
매개변수는 함수에 전달하는 입력값, 반환값은 `return`으로 돌려주는 결과. `read_int(prompt, low, high)`는 3개를 받아 검증된 정수를 반환한다.

**Q6. 클래스를 왜 쓰는가?**
관련 데이터와 기능을 하나로 묶어 코드를 역할별로 구조화하고, 같은 설계로 여러 객체를 만들어 재사용하기 위해.

**Q7. `__init__`과 `self`의 역할은?**
`__init__`은 객체 생성 시 자동 호출되어 속성을 초기화하는 생성자. `self`는 그 객체 자신을 가리키며, `self.속성`으로 객체별 데이터를 저장·접근한다.

**Q8. 속성과 메서드의 차이는?**
속성은 객체가 가진 데이터(`quiz.answer`), 메서드는 객체가 수행하는 동작(`quiz.is_correct()`).

**Q9. 파일을 읽고 쓰는 기본 과정은?**
열기(`open`, 모드 지정) → 읽기/쓰기(`json.load`/`json.dump`) → 닫기. `with`를 쓰면 자동으로 닫힌다.

**Q10. JSON은 무엇이며 왜 저장에 쓰는가?**
키-값과 배열로 데이터를 표현하는 텍스트 형식. 사람이 읽기 쉽고 언어 독립적이며 Python의 dict/list와 쉽게 변환된다. 프로그램이 종료돼도 데이터를 유지(영속성)할 수 있다.

**Q11. try/except는 왜 쓰는가?**
오류가 발생해도 프로그램이 비정상 종료되지 않도록 잡아서 안내/복구하기 위해. 예) 숫자 변환 실패, 손상된 JSON 파일.

**Q12. Git이 무엇이고 왜 필요한가?**
변경 이력을 관리하는 분산 버전 관리 시스템. 이전 상태로 복구, 변경 추적, 브랜치를 이용한 안전한 개발, 협업을 위해 필요.

**Q13. add, commit, push의 차이는?**
add: 변경 파일을 커밋 대기 영역에 올림 / commit: 이력으로 저장(로컬) / push: 로컬 커밋을 원격에 업로드.

**Q14. clone과 pull의 차이는?**
clone은 원격 저장소 전체를 처음 복제, pull은 이미 있는 로컬 저장소에 원격의 새 변경을 가져와 병합.

**Q15. 브랜치를 만들고 병합하는 명령은?**
`git checkout -b 이름`(생성+이동) → 작업/커밋 → `git checkout main` → `git merge 이름`.

**Q16. 아래 코드의 출력은?**
```python
choices = ["a", "b", "c", "d"]
answer = 2
print(choices[answer - 1])      # b   (인덱스는 0부터라서 -1)
```
```python
score = 4 * 100 // 6            # 66   (// 는 몫, 정수 나눗셈)
```

**Q17. `if` 조건에서 `=`와 `==`의 차이는?**
`=`는 대입, `==`는 비교. 조건문에는 `==`를 쓴다.

### 자주 틀리는 포인트 체크
- [ ] list 인덱스는 **0부터** (화면 번호는 1부터라 `-1` 필요)
- [ ] `input()`은 **항상 문자열**
- [ ] 블록은 **들여쓰기 + 콜론(:)**
- [ ] `self`는 정의할 때만 적고, 호출할 때는 적지 않는다
- [ ] `open(..., "w")`는 **기존 내용을 지운다**
- [ ] `git add`/`commit`은 로컬, 원격에 올리려면 **`push`**
- [ ] Git(도구) ≠ GitHub(서비스)
