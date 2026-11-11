"""Quiz 클래스: 개별 퀴즈 1개를 표현한다."""


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
