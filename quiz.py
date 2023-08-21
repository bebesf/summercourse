class Question:
    def __init__(self, question, options, correct_option):
        self.question = question
        self.options = options
        self.correct_option = correct_option
        self.answer_value = options[correct_option - 1]

    def check_answer(self, user_choice):
        return user_choice == self.correct_option

def run_quiz(questions):
    score = 0
    total_questions = len(questions)

    for index, question in enumerate(questions, start=1):
        print(f"Question {index}: {question.question}")
        for option_num, option in enumerate(question.options, start=1):
            print(f"{option_num}. {option}")

        user_choice = int(input("Your answer (enter option number): "))

        if 1 <= user_choice <= len(question.options):
            if question.check_answer(user_choice):
                print("\n")
                print("=========================================")
                print("Wow!\U0001F603 correct you just got 1 point")
                print("=========================================")
                score += 1
            else:
                print("******************************************************")
                print(f"Wrong!\U0001F612 The correct answer is {question.answer_value}")
                print("******************************************************")
        else:
            print("Invalid option\U0001F61C Skipping this question.\n")

    print(f"Quiz completed! You scored {score} out of {total_questions}.")

if __name__ == "__main__":
    question1 = Question("What year did the Titanic sink in the Atlantic Ocean on 15 April, on its maiden voyage from Southampton?", ["1912", "1820", "1949"], 1)
    question2 = Question("Which planet is known as the Red Planet?", ["Mars", "Venus", "Jupiter"], 1)
    question3 = Question("What is the doll Barbie's full name?", ["Athena Williams", "Barbara Roberts", "Bluey Dave"], 2)
    question4 = Question("What is the largest continent?", ["Asia", "Europe", "Africa"], 1)

    quiz_questions = [question1, question2, question3, question4]

    print("Welcome to the Quiz Game!")
    run_quiz(quiz_questions)
