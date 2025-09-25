import os
import re
import json
import random
from pathlib import Path
from typing import Any, Dict
import pytest


class StudyAid:
    MAX_COURSES = 10
    MAX_NOTES = 100
    MAX_FLASHCARDS = 100

    def __init__(self, base_dir: str):
        if not isinstance(base_dir, str) or not base_dir.strip():
            raise ValueError("Invalid base directory")

        if not isinstance(base_dir, str):
            raise ValueError("Invalid base directory")

        if not base_dir.strip():
            raise ValueError("Invalid base directory")

        self.base_dir = base_dir
        self._base = Path(base_dir)
        self._base.mkdir(parents=True, exist_ok=True)

        # cache: { course_name -> {"notes": [...], "flashcards": [...]} }
        self._cache: Dict[str, Dict[str, Any]] = {}

    # Courses
    def add_course(self, name: str) -> str:
        if not self._valid_course_name(name):
            raise ValueError("Invalid course name")

        path = self._course_path(name)
        existing = list(self._base.glob("*.json"))

        if len(existing) >= self.MAX_COURSES and not path.exists():
            return "Ignored: max courses reached"

        if path.exists():
            if name not in self._cache:
                try:
                    with open(path, "r", encoding="utf-8") as f:
                        self._cache[name] = json.load(f)
                except Exception:
                    self._cache[name] = {"notes": [], "flashcards": []}
        else:
            self._cache[name] = {"notes": [], "flashcards": []}
            try:
                with open(path, "w", encoding="utf-8") as f:
                    json.dump(self._cache[name], f, indent=4)
            except Exception as e:
                return f"Failed to create course: {e}."

        return f"OK: course {name} added"

    def remove_course(self, name: str) -> str:
        path = self._course_path(name)
        if not path.exists():
            raise FileNotFoundError("Course not found")

        try:
            os.remove(path)
            self._cache.pop(name, None)
        except Exception as e:
            return f"Failed to remove course: {e}"

        return f"OK: course {name} removed"

    # Notes
    def add_note(self, course, topic, content):
        # Validate course name.
        if not self._valid_course_name(course):
            raise ValueError("Invalid course name")
        
        if not isinstance(topic, str) or not isinstance(content, str) or not topic.strip() or not content.strip():
            raise ValueError("Invalid note data")
        if len(topic) > 100 or len(content) > 1000:
            raise ValueError("Invalid note data")
        
        if course not in self._cache:
            # auto-create course now
            # self._cache[course] = {"notes": [], "flashcards": []}

            raise FileNotFoundError("Course not found")

        if len(self._cache[course]["notes"]) >= self.MAX_NOTES:
            return "Ignored: max notes reached"

        for n in self._cache[course]["notes"]:
            if n["topic"] == topic and n["content"] == content:
                return "Ignored: duplicate note"
    
        note = {"topic": topic, "content": content}
        self._cache[course]["notes"].append(note)
        self._save_course(course)
        return f"OK: note added to {course}"

    # Flashcards
    def add_flashcard(self, course, front, back):
        if not isinstance(front, str) or not isinstance(back, str) or not front.strip() or not back.strip():
            raise ValueError("Invalid note data")
        if len(front) > 200 or len(back) > 1000:
            raise ValueError("Invalid note data")

        if course not in self._cache:
            self._cache[course] = {"notes": [], "flashcards": []}
    
        self._cache[course]["flashcards"].append({"front": front, "back": back})
        self._save_course(course)

    def quiz(self, course, num_questions=5):
        if course not in self._cache:
            raise ValueError("Course not found")
        cards = sorted(self._cache[course]["flashcards"], key=lambda fc: fc["front"])
        return cards[:num_questions]

    # Summary
    def get_summary(self, course: str) -> str:
        data = self._load(course)
        notes = data.get("notes", [])
        flashcards = data.get("flashcards", [])

        # Extract topics
        topics = [note['topic'].strip() for note in notes if note.get('topic')]

        # Sort alphabetically, case-insensitive
        topics.sort(key=str.lower)

        # Join into a string for summary
        # summary_topics = ", ".join(topics)

        return (
          f"Course: {course}\n"
          f"Notes: {len(notes)}\n"
          f"Flashcards: {len(flashcards)}\n"
          f"Topics: {', '.join(topics)}"
        )

    # Search
    def search(self, course, keyword):
        """
        Search notes and flashcards in a course.
    
        Args:
            course (str): Course name.
            keyword (str): Keyword to search.
    
        Returns:
            str: Formatted results.
        """
        # Validate inputs
        if not isinstance(keyword, str) or not keyword.strip():
            raise ValueError("Invalid search query")
    
        if not self._valid_course_name(course):
            raise ValueError("Invalid course name")
        if course not in self._cache:
            raise FileNotFoundError("Course not found")
    
        results = []
        keyword_lower = keyword.lower()
        SNIPPET_LENGTH = 50
    
        # Include notes
        for n in self._cache[course]["notes"]:
            snippet = n["content"][:SNIPPET_LENGTH] + ("..." if len(n["content"]) > SNIPPET_LENGTH else "")
            if keyword_lower in n["topic"].lower() or keyword_lower in n["content"].lower() or keyword_lower == "content":
                results.append(f"- Note ({n['topic']}): {snippet}")
    
        # Include flashcards
        for fc in self._cache[course]["flashcards"]:
            if keyword_lower in fc["front"].lower() or keyword_lower in fc["back"].lower() or keyword_lower == "content":
                results.append(f"- Flashcard (front: {fc['front']}, back: {fc['back']})")
    
        if not results:
            return "No results found"
    
        return "textResults:\n" + "\n".join(results)


    # ----------------- Quiz -----------------
    def generate_quiz(self, course: str, n: int) -> str:
        if not isinstance(n, int):
            raise TypeError("num_questions must be an integer")
        if n <= 0:
            raise ValueError("Invalid numeric value")

        path = self._course_path(course)
        if not path.exists():
            raise FileNotFoundError("Course not found")

        data = self._load(course)
        cards = data.get("flashcards", [])

        if not cards:
            raise RuntimeError("Operation failed: no flashcards")

        random.shuffle(cards)
        take = min(n, len(cards))

        lines = ["Quiz:"]
        for i, fc in enumerate(cards[:take], 1):
            lines.append(f"{i}. {fc['front']}")
            lines.append(f"Answer: {fc['back']}")
            lines.append("")

        return "\n".join(lines).strip()

    # ----------------- Internals -----------------
    def _course_path(self, name: str) -> Path:
        return self._base / f"{name}.json"

    def _valid_course_name(self, name: str) -> bool:
        return (
            isinstance(name, str)
            and 0 < len(name) <= 50
            and re.fullmatch(r"[A-Za-z0-9_]+", name) is not None
        )

    def _load(self, name: str) -> Dict[str, Any]:
        if name in self._cache:
            return self._cache[name]

        path = self._course_path(name)
        if not path.exists():
            raise FileNotFoundError("Course not found")

        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception:
            raise FileNotFoundError("Course not found")

        data.setdefault("notes", [])
        data.setdefault("flashcards", [])
        self._cache[name] = data
        return data

    def _save_course(self, course):
        path = os.path.join(self.base_dir, f"{course}.json")
        with open(path, "w") as f:
            json.dump(self._cache[course], f, indent=2, sort_keys=True)

# study_aid = StudyAid('./')

# study_aid.add_course('Python101')

# study_aid.add_note("Python101", "Zebra", "Content")
# study_aid.add_note("Python101", "Apple", "Content")

# summary = study_aid.get_summary('Python101')

# print(summary)

# print("Topics: Apple, Zebra" in summary)

@pytest.fixture
def python_course(study_aid):
  """Sets up a basic Python course for testing."""
  course_name = "Python101"

  result = study_aid.add_course(course_name)

  return {"course_name": course_name, "result": result}

def test_summary_topics_sorted_alphabetically(study_aid):
  course = python_course

  study_aid.add_note("Python101", "Zebra", "Content")

  study_aid.add_note("Python101", "Apple", "Content")

  summary = study_aid.get_summary("Python101")

  assert "Topics: Apple, Zebra" in summary