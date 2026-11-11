"""QuizGame 클래스: 게임 전체(메뉴, 풀기, 추가, 목록, 점수)를 관리한다."""

from quiz import Quiz


class QuizGame:
    """게임 전체를 관리하는 클래스"""

    LINE = "=" * 40

    def __init__(self):
        # 속성(attribute): 객체가 가지는 데이터
        self.running = True
        self.quizzes = self.default_quizzes()  # 퀴즈 목록 (list)
        self.best_score = None  # 최고 점수 (아직 안 풀었으면 None)
        self.best_total = None  # 최고 점수를 냈을 때의 전체 문제 수
        self.best_correct = None  # 최고 점수를 냈을 때의 정답 수

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

    # ---------- 퀴즈 풀기 ----------
    def play_quiz(self):
        """저장된 퀴즈를 순서대로 출제하고 결과를 보여준다."""
        if not self.quizzes:
            print("⚠️ 등록된 퀴즈가 없습니다. 먼저 퀴즈를 추가하세요.")
            return

        total = len(self.quizzes)
        print(f"\n📝 퀴즈를 시작합니다! (총 {total}문제)\n")
        correct = 0
        for index, quiz in enumerate(self.quizzes, start=1):
            print("-" * 40)
            quiz.display(index)
            user_answer = self.read_int("정답 입력: ", 1, 4)
            if quiz.is_correct(user_answer):
                print("✅ 정답입니다!\n")
                correct += 1
            else:
                print(f"❌ 오답입니다. 정답은 {quiz.answer}번입니다.\n")

        score = correct * 100 // total
        print(self.LINE)
        print(f"🏆 결과: {total}문제 중 {correct}문제 정답! ({score}점)")
        if self.update_best_score(score, correct, total):
            print("🎉 새로운 최고 점수입니다!")
        print(self.LINE)

    # ---------- 점수 확인 ----------
    def update_best_score(self, score, correct, total):
        """최고 점수보다 높으면 갱신하고 True를 반환한다."""
        if self.best_score is None or score > self.best_score:
            self.best_score = score
            self.best_correct = correct
            self.best_total = total
            return True
        return False

    def show_score(self):
        if self.best_score is None:
            print("⚠️ 아직 퀴즈를 풀지 않았습니다. 먼저 퀴즈를 풀어보세요.")
            return
        print(f"\n🏆 최고 점수: {self.best_score}점 "
              f"({self.best_total}문제 중 {self.best_correct}문제 정답)")

    # ---------- 퀴즈 추가 ----------
    def read_text(self, prompt):
        """빈 문자열이 아닌 텍스트를 입력받을 때까지 반복한다."""
        while True:
            text = input(prompt).strip()
            if text:
                return text
            print("⚠️ 빈 입력입니다. 내용을 입력하세요.")

    def add_quiz(self):
        """문제, 선택지 4개, 정답 번호를 입력받아 퀴즈를 추가한다."""
        print("\n📌 새로운 퀴즈를 추가합니다.\n")
        question = self.read_text("문제를 입력하세요: ")
        choices = []
        for number in range(1, 5):
            choices.append(self.read_text(f"선택지 {number}: "))
        answer = self.read_int("정답 번호 (1-4): ", 1, 4)
        self.quizzes.append(Quiz(question, choices, answer))
        print("\n✅ 퀴즈가 추가되었습니다!")

    # ---------- 퀴즈 목록 ----------
    def list_quizzes(self):
        """등록된 퀴즈의 문제 목록을 출력한다."""
        if not self.quizzes:
            print("⚠️ 등록된 퀴즈가 없습니다.")
            return
        print(f"\n📋 등록된 퀴즈 목록 (총 {len(self.quizzes)}개)\n")
        print("-" * 40)
        for index, quiz in enumerate(self.quizzes, start=1):
            print(f"[{index}] {quiz.question}")
        print("-" * 40)

    # ---------- 메뉴 동작 ----------
    def handle_choice(self, choice):
        if choice == 1:
            self.play_quiz()
        elif choice == 2:
            self.add_quiz()
        elif choice == 3:
            self.list_quizzes()
        elif choice == 4:
            self.show_score()
        elif choice == 5:
            print("프로그램을 종료합니다. 안녕히 가세요!")
            self.running = False

    def run(self):
        """메인 루프. Ctrl+C / 입력 종료(EOF)가 와도 안전하게 끝낸다."""
        try:
            while self.running:
                self.show_menu()
                choice = self.read_int("선택: ", 1, 5)
                self.handle_choice(choice)
        except (KeyboardInterrupt, EOFError):
            print("\n⚠️ 입력이 중단되었습니다. 안전하게 종료합니다.")
