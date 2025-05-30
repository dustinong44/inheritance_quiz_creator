from quiz_creator import QuizCreator
from quiz_runner import QuizRunner

class QuizCompile(QuizCreator, QuizRunner):
    def __init__(self, quiz_directory, filename_prefix="Your Quiz"):
        QuizCreator.__init__(self, quiz_directory, filename_prefix)
        QuizRunner.__init__(self, quiz_directory, filename_prefix)

    def manage_quiz(self):
        choice = input("Do you want to create a new quiz or take one? (create/take): ").strip().lower()
        if choice == "create":
            self.start_quiz_creation()
        elif choice == "take":
            self.run_quiz()
        else:
            print("Invalid option. Please enter 'create' or 'take'.")


quiz_directory = r"C:\Users\dustin\Music\quiz_creator\answer_the_quiz\answer_the_quiz"
quiz_manager = QuizManager(quiz_directory)
quiz_manager.manage_quiz()
