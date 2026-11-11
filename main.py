"""파이썬 기초 퀴즈 게임 (터미널 프로그램)"""


class QuizGame:
    """게임 전체를 관리하는 클래스"""

    LINE = "=" * 40

    def __init__(self):
        # 속성(attribute): 객체가 가지는 데이터
        self.running = True

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
