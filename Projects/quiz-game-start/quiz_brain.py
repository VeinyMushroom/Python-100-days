class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_question(self):

        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]

        user_answer = input(f"Q.{self.question_number + 1} {current_question.text} (True/False): ")
        return user_answer

    def check_answer(self, user_answer):
        if user_answer == self.question_list[self.question_number].answers:
            self.score += 1
            print(f"Correct! Your sore is {self.score}/{len(self.question_list)}")
        else:
            print(f"Incorrect! Your score is {self.score}/{len(self.question_list)}")
        print("\n")
