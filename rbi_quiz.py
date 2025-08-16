import datetime
import json
import random
from dataclasses import dataclass, asdict
from typing import List

import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.rbi.org.in/scripts/bs_circularindexdisplay.aspx"
DETAIL_PREFIX = "https://www.rbi.org.in/scripts/"


@dataclass
class Question:
    id: str
    circular_number: str
    subject: str
    question: str
    options: List[str]
    correct_index: int
    difficulty: int


def scrape_circulars(limit: int = 20) -> List[dict]:
    """Scrape the RBI circular listing page for recent circulars."""
    res = requests.get(BASE_URL, timeout=30)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "html.parser")
    table = soup.find("table", class_="tablebg")
    rows = table.find_all("tr")[1:limit+1]
    circulars = []
    for row in rows:
        cells = row.find_all("td")
        if not cells:
            continue
        circ_num = cells[0].get_text(strip=True)
        link = cells[0].find("a")
        href = DETAIL_PREFIX + link["href"] if link else None
        date = cells[1].get_text(strip=True)
        dept = cells[2].get_text(strip=True)
        subject = cells[3].get_text(strip=True)
        circulars.append(
            {
                "circular_number": circ_num,
                "date": date,
                "department": dept,
                "subject": subject,
                "url": href,
            }
        )
    return circulars


def generate_quiz(num_questions: int = 10) -> List[Question]:
    """Generate a daily quiz of multiple-choice questions."""
    circulars = scrape_circulars(limit=max(20, num_questions * 2))
    dates = [c["date"] for c in circulars]

    # Seed random to current date so everyone gets the same quiz daily
    random.seed(datetime.date.today().isoformat())
    questions: List[Question] = []
    for i, circ in enumerate(circulars[:num_questions]):
        correct = circ["date"]
        distractors = random.sample([d for d in dates if d != correct], k=3)
        options = distractors + [correct]
        random.shuffle(options)
        qtext = (
            f"On which date was the circular titled '{circ['subject']}'\n"
            f"({circ['circular_number']}) issued?"
        )
        questions.append(
            Question(
                id=f"Q{i+1}",
                circular_number=circ["circular_number"],
                subject=circ["subject"],
                question=qtext,
                options=options,
                correct_index=options.index(correct),
                difficulty=i + 1,
            )
        )
    return questions


def main() -> None:
    quiz = generate_quiz()
    data = [asdict(q) for q in quiz]
    print(json.dumps(data, indent=2))


if __name__ == "__main__":
    main()
