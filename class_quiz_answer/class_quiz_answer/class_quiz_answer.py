import os
import random

class QuizAnswer:
    def __init__(self, quiz_directory, filename_prefix="Your Quiz"):
        self.quiz_directory = quiz_directory
        self.filename_prefix = filename_prefix
        self.quiz_data = []
        self.latest_quiz_file = self.get_latest_quiz_file()

    def get_latest_quiz_file(self):
        existing_files = [f for f in os.listdir(self.quiz_directory) if f.startswith(self.filename_prefix) and f.endswith(".txt")]
        if not existing_files:
            return None  
        latest_file = sorted(existing_files, key=lambda x: int(x.replace(self.filename_prefix, "").replace(".txt", "")), reverse=True)[0]
        return os.path.join(self.quiz_directory, latest_file)

    def load_quiz(self):
        if not self.latest_quiz_file:
            print("Error: No valid quiz files found.")
            return []
        
        quiz_data = []
        try:
            with open(self.latest_quiz_file, "r") as file:
                lines = file.readlines()
                question_data = {}
                for line in lines:
                    if line.startswith("Question:"):
                        question_data = {"question": line.strip("Question: ").strip(), "answers": [], "correct": None}
                    elif line.startswith(("a.", "b.", "c.", "d.")):
                        question_data["answers"].append(line.strip())
                    elif line.startswith("Correct answer:"):
                        question_data["correct"] = line.strip("Correct answer: ").strip()
                        quiz_data.append(question_data)
            return quiz_data
        except FileNotFoundError:
            print(f"Error: {self.latest_quiz_file} not found.")
            return []

    def ask_question(self, question_data):
        print(f"\nQuestion: {question_data['question']}")
        for answer in question_data["answers"]:
            print(answer)

        while True:
            user_answer = input("Your answer (enter a, b, c, or d): ").strip().lower()
            if user_answer in ["a", "b", "c", "d"]:
                return user_answer
            else:
                print("Invalid input. Please enter a, b, c, or d.")

    def check_answer(self, user_answer, question_data):
        correct_text = question_data["correct"]
        correct_letter = None

        for answer in question_data["answers"]:
            if correct_text == answer[3:].strip():  
                correct_letter = answer[0]  
                break

        if user_answer == correct_letter:
            print("Correct!")
            return True
        else:
            print(f"Incorrect! The correct answer was {correct_letter}: {correct_text}")
            return False

    def run_quiz(self):
        self.quiz_data = self.load_quiz()
        if not self.quiz_data:
            return

        score = 0
        total_questions = len(self.quiz_data)
        random.shuffle(self.quiz_data)  

        for question_data in self.quiz_data:  
            user_answer = self.ask_question(question_data)
            if self.check_answer(user_answer, question_data):
                score += 1

        print(f"\nQuiz Complete! Your final score: {score}/{total_questions}")

# Usage Example
quiz_directory = r"C:\Users\dustin\Music\quiz_creator\answer_the_quiz\answer_the_quiz"
quiz_runner = QuizAnswer(quiz_directory)
quiz_runner.run_quiz()
