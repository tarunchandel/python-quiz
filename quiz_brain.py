class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def any_more_questions(self):
        return self.question_number < len(self.question_list)



    def ask_question(self):
        self.user_answer = input(f"Q. {self.question_number+1}: {self.question_list[self.question_number].text} (True/False): ")
        self.check_answer()
        self.question_number += 1



    def check_answer(self):
        if self.user_answer.lower() == self.question_list[self.question_number].answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer is: {self.question_list[self.question_number].answer}")
        print(f"Your current score is: {self.score}/{self.question_number+1}")
        print("\n")
