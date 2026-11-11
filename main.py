"""파이썬 기초 퀴즈 게임 (터미널 프로그램)"""


class Quiz:
    """개별 퀴즈 1개를 표현하는 클래스"""

    def __init__(self, question, choices, answer):
        # self: 만들어지는 객체 자기 자신. self.xxx = 값 -> 속성 저장
        self.question = question  # 문제 (str)
        self.choices = choices    # 선택지 4개 (list)
        self.answer = answer      # 정답 번호 1~4 (int)

    def display(self, index):
        """문제와 선택지를 출력한다."""
        print(f"[문제 {index}]")
        print(self.question)
        print()
        for number, choice in enumerate(self.choices, start=1):
            print(f"{number}. {choice}")
        print()

    def is_correct(self, user_answer):
        """사용자가 입력한 번호가 정답이면 True."""
        return user_answer == self.answer

    def to_dict(self):
        """JSON 저장용 dict로 변환"""
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer,
        }

    @classmethod
    def from_dict(cls, data):
        """dict에서 Quiz 객체 생성"""
        return cls(data["question"], data["choices"], data["answer"])


class QuizGame:
    """게임 전체를 관리하는 클래스"""

    LINE = "=" * 40

    def __init__(self):
        # 속성(attribute): 객체가 가지는 데이터
        self.running = True
        self.quizzes = self.default_quizzes()  # 퀴즈 목록 (list)

    # ---------- 기본 데이터 ----------
    def default_quizzes(self):
        """기본 퀴즈 6개를 Quiz 객체로 만들어 list로 반환"""
        return [
            Quiz("파이썬에서 리스트를 만들 때 사용하는 기호는?",
                 ["()", "[]", "{}", "<>"], 2),
            Quiz("type(3.14)의 결과로 알맞은 것은?",
                 ["int", "str", "float", "bool"], 3),
            Quiz("키와 값의 쌍으로 데이터를 저장하는 자료형은?",
                 ["list", "dict", "tuple", "str"], 2),
            Quiz("조건에 따라 분기할 때 사용하는 키워드가 아닌 것은?",
                 ["if", "elif", "else", "loop"], 4),
            Quiz("정해진 횟수만큼 반복할 때 주로 사용하는 구문은?",
                 ["for", "if", "def", "class"], 1),
            Quiz("함수를 정의할 때 사용하는 키워드는?",
                 ["func", "def", "function", "define"], 2),
        ]

    # ---------- 화면 ----------
    def show_menu(self):
        print(self.LINE)
        print("        🎯 파이썬 기초 퀴즈 게임 🎯")
        print(self.LINE)
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료")
        print(self.LINE)

    # ---------- 입력 처리 ----------
    def read_int(self, prompt, low, high):
        """low~high 사이의 정수를 입력받을 때까지 반복한다."""
        while True:
            text = input(prompt).strip()  # 앞뒤 공백 제거
            if text == "":
                print(f"⚠️ 입력이 비어 있습니다. {low}-{high} 사이의 숫자를 입력하세요.")
                continue
            try:
                number = int(text)
            except ValueError:
                print(f"⚠️ 잘못된 입력입니다. {low}-{high} 사이의 숫자를 입력하세요.")
                continue
            if number < low or number > high:
                print(f"⚠️ 범위를 벗어났습니다. {low}-{high} 사이의 숫자를 입력하세요.")
                continue
            return number

    # ---------- 메뉴 동작 ----------
    def handle_choice(self, choice):
        if choice == 5:
            print("프로그램을 종료합니다. 안녕히 가세요!")
            self.running = False
        else:
            print("🚧 준비 중인 기능입니다.")

    def run(self):
        """메인 루프. Ctrl+C / 입력 종료(EOF)가 와도 안전하게 끝낸다."""
        try:
            while self.running:
                self.show_menu()
                choice = self.read_int("선택: ", 1, 5)
                self.handle_choice(choice)
        except (KeyboardInterrupt, EOFError):
            print("\n⚠️ 입력이 중단되었습니다. 안전하게 종료합니다.")


if __name__ == "__main__":
    QuizGame().run()
