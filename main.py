from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_bank.append(Question(question["question"], question["correct_answer"]))

quiz_brain = QuizBrain(question_bank)

# for question in quiz_brain.question_list:
#     quiz_brain.ask_question()

while quiz_brain.any_more_questions():
    quiz_brain.ask_question()

print("You've completed the quiz.")
print(f"Your final score is: {quiz_brain.score}/{quiz_brain.question_number}")
