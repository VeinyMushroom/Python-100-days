from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for dict_ in question_data:
    q = Question(dict_["text"], dict_["answer"])
    question_bank.append(q)


brain = QuizBrain(question_bank)
while brain.still_has_question():
    nxt_q = brain.next_question()
    brain.check_answer(nxt_q)
    brain.question_number += 1
print(f"Your final score is {brain.score}/{len(brain.question_list)}")
