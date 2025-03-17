import random
import time

class GilmoreGirlsTrivia:
    def __init__(self):
        self.questions = [
            {
                "question": "What is the name of Kirk's cat?",
                "answers": ["cat kirk", "kirk"]
            },
            {
                "question": "What is the name of the town where Gilmore Girls is set?",
                "answers": ["stars hollow", "stars-hollow"]
            },
            {
                "question": "What is the name of Lorelai's inn?",
                "answers": ["dragonfly inn", "dragonfly", "the dragonfly inn"]
            },
            {
                "question": "What is Rory's real first name?",
                "answers": ["lorelai"]
            },
            {
                "question": "What is Paris Geller's college roommate's name?",
                "answers": ["janet", "rory"]
            },
            {
                "question": "What is the name of Lane's band?",
                "answers": ["hep alien"]
            }
            # Add more questions here
        ]
        self.score = 0

    def play(self):
        print("\nWelcome to the Gilmore Girls Trivia Game!")
        print("Answer these questions about Stars Hollow and its residents.")
        print("Type your answer or 'quit' to end the game.\n")

        random.shuffle(self.questions)

        for question in self.questions:
            print(question["question"])
            answer = input("Your answer: ").strip().lower()

            if answer == 'quit':
                break

            if answer in question["answers"]:  # This is the corrected line
                print("Correct! Oy with the poodles already!\n")
                self.score += 1
            else:
                print(f"Sorry, the correct answers were: {' or '.join(question['answers'])}\n")

            time.sleep(1)

        self.show_results()

    def show_results(self):
        print("\nGame Over!")
        print(f"Your final score: {self.score} out of {len(self.questions)}")
        
        if self.score == len(self.questions):
            print("Perfect score! You're a true Gilmore Girls fan!")
        elif self.score >= len(self.questions) * 0.7:
            print("Great job! Almost as quick as a Gilmore girl!")
        elif self.score >= len(self.questions) * 0.5:
            print("Not bad! You might need another coffee at Luke's!")
        else:
            print("Time to binge-watch the series again!")

# Run the game
if __name__ == "__main__":
    game = GilmoreGirlsTrivia()
    game.play()
