import os

class QuizCreator:
    def __init__(self, save_directory, filename_prefix="Your Quiz"):
        self.save_directory = save_directory
        self.filename_prefix = filename_prefix
        os.makedirs(self.save_directory, exist_ok=True)
        self.version_number = self.get_next_version()
        self.filename = self.get_filename(self.version_number)
        self.quiz_questions = []
        self.possible_answers = []
        self.correct_answers = []
        self.question_scores = []

    def get_filename(self, version):
        return os.path.join(self.save_directory, f"{self.filename_prefix}{version}.txt")

    def get_next_version(self):
        existing_files = [f for f in os.listdir(self.save_directory) if f.startswith(self.filename_prefix)]
        return len(existing_files) + 1

    def add_question(self):
        print(f"Current quiz version: {self.version_number}")
        question = input("Enter your question: ")
        self.quiz_questions.append(question)

        while True:
            try:
                score = float(input("Enter the point value for this question: "))
                self.question_scores.append(score)
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value for the score.")

        while True:
            answers = [input(f"Enter possible answer {chr(97+i)}: ") for i in range(4)]
            if len(set(answers)) == 4:  
                self.possible_answers.append(answers)
                break
            else:
                print("Answers must be unique. Please try again.")

        while True:
            correct = input("Enter the correct answer (must match one of the options): ")
            if correct in answers:
                self.correct_answers.append(correct)
                break
            else:
                print("Correct answer must match one of the provided options. Please try again.")

        self.save_question(question, score, answers, correct)

    def save_question(self, question, score, answers, correct):
        with open(self.filename, "a") as file:
            file.write(f"Question: {question}\n")
            file.write(f"Possible Score: {score}\n")
            for i, answer in enumerate(answers):
                file.write(f"{chr(97+i)}. {answer}\n")
            file.write(f"Correct answer: {correct}\n\n")

    def start_quiz_creation(self):
        while True:
            self.add_question()
            if input("Do you want to enter another question? (yes/no): ").lower() != "yes":
                print(f"Quiz version {self.version_number} has been saved.")
                if input("Do you want to start a new quiz version? (yes/no): ").lower() == "yes":
                    self.version_number += 1
                    self.filename = self.get_filename(self.version_number)
                    self.quiz_questions.clear()
                    self.possible_answers.clear()
                    self.correct_answers.clear()
                    self.question_scores.clear()
                else:
                    print("Thank you! All quiz data has been saved.")
                    break

    def display_quiz(self):
        print("\nFinal Quiz:")
        for i, question in enumerate(self.quiz_questions):
            print(f"{i + 1}. {question}")
            print(f"Possible Score: {self.question_scores[i]}")
            for j, answer in enumerate(self.possible_answers[i]):
                print(f"{chr(97+j)}. {answer}")
            print(f"Correct answer: {self.correct_answers[i]}")


save_directory = r"C:\Users\dustin\Music\quiz_creator\answer_the_quiz\answer_the_quiz"
quiz_creator = QuizCreator(save_directory)
quiz_creator.start_quiz_creation()
quiz_creator.display_quiz()
