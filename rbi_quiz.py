import datetime
import json
import random
from dataclasses import dataclass, asdict
from typing import List


@dataclass
class Question:
    id: str
    question: str
    options: List[str]
    correct_index: int
    difficulty: str


def generate_question_bank(num_questions: int = 5000) -> List[Question]:
    """Generate a diversified bank of arithmetic questions.

    The random seed is initialised with today's date so a new set of questions
    is produced each day while remaining deterministic for that day.
    """

    random.seed(datetime.date.today().isoformat())
    bank: List[Question] = []
    difficulties = ["Easy", "Medium", "Hard"]
    operations = ["+", "-", "*", "/"]

    for i in range(1, num_questions + 1):
        op = random.choice(operations)
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        if op == "/":
            # ensure divisible numbers for integer results
            a = a * b
        expression = f"{a} {op} {b}"
        correct = eval(expression)

        # create 3 unique incorrect options
        options = [correct]
        while len(options) < 4:
            delta = random.randint(-10, 10)
            option = correct + delta
            if option not in options:
                options.append(option)
        random.shuffle(options)

        difficulty = random.choice(difficulties)
        bank.append(
            Question(
                id=f"Q{i}",
                question=f"What is {expression}?",
                options=[str(o) for o in options],
                correct_index=options.index(correct),
                difficulty=difficulty,
            )
        )

    return bank


QUESTIONS: List[Question] = generate_question_bank()


def generate_quiz(num_questions: int = 10) -> List[Question]:
    random.seed(datetime.date.today().isoformat())
    sample = random.sample(QUESTIONS, k=min(num_questions, len(QUESTIONS)))
    return sample


def main() -> None:
    quiz = generate_quiz()
    data = [asdict(q) for q in quiz]
    print(json.dumps(data, indent=2))


if __name__ == "__main__":
    main()
