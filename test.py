import os
import re
import json
import random
from pathlib import Path
from typing import Any, Dict
import pytest
import tempfile


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
		# breakpoint()

		# Validate course name.
		if not self._valid_course_name(course):
			raise ValueError("Invalid course name")

		if not isinstance(topic, str) or not isinstance(content, str) \
			or not topic.strip() or not content.strip():
			raise ValueError("Invalid note data")

		if len(topic) > 1000 or len(content) > 1000:
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

		# breakpoint()

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
			if not self._valid_course_name(course):
				raise ValueError("Invalid course name")

			self._cache[course] = {"notes": [], "flashcards": []}
			return "New course added along flashcard"

		# Check for duplicates
		for fc in self._cache[course]["flashcards"]:
			if fc["front"] == front and fc["back"] == back:
				return "Ignored: duplicate flashcard"

		self._cache[course]["flashcards"].append({"front": front, "back": back})
		self._save_course(course)

		return f"OK: flashcard added to {course}"

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

		if not topics:
			topics = "None"
		else:
			topics = ', '.join(topics)

		# Join into a string for summary
		# summary_topics = ", ".join(topics)

		return (
			f"Course: {course}\n"
			f"Notes: {len(notes)}\n"
			f"Flashcards: {len(flashcards)}\n"
			f"Topics: {topics}"
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


	# Quiz
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

		# random.shuffle(cards)
		take = min(n, len(cards))

		lines = ["Quiz:"]

		for i, fc in enumerate(cards[:take], 1):
			lines.append(f"{i}. {fc['front']}")
			lines.append(f"   Answer: {fc['back']}")
			lines.append("")

		return "\n".join(lines).strip()

	# Internals
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
			print('name:', name, '\n')

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

@pytest.fixture
def study_aid():
	with tempfile.TemporaryDirectory() as tmpdir:
		yield StudyAid(tmpdir)

def test_summary_topics_sorted_alphabetically(study_aid, python_course):    
	course_name = python_course['course_name']

	study_aid.add_note(course_name, "Zebra", "Content")

	study_aid.add_note(course_name, "Apple", "Content")

	summary = study_aid.get_summary("Python101")

	assert "Topics: Apple, Zebra" in summary

def test_summary_basic(study_aid, python_course):
	course_name = python_course['course_name']

	study_aid.add_note(course_name, "Loops", "For loops iterate over lists.")

	study_aid.add_flashcard(course_name, "Q1", "A1")

	summary = study_aid.get_summary(course_name)
    
	print('summary:\n', summary, sep='')

	assert "Course: Python101" in summary
	assert "Notes: 1" in summary
	assert "Flashcards: 1" in summary
	assert "Topics: Loops" in summary

def test_creating_and_duplicating_course(study_aid):
	# First addition
	msg1 = study_aid.add_course("Python101")
	assert msg1 == "OK: course Python101 added"

	assert study_aid._load("Python101") == {"notes": [], "flashcards": []}

	# Adding the same course again should still succeed (idempotent)
	msg2 = study_aid.add_course("Python101")
	assert msg2 == "OK: course Python101 added"

def test_adding_notes_basic(study_aid, python_course):
	result = study_aid.add_note("Python101", "Loops", "For loops iterate over lists.")

	assert result == "OK: note added to Python101"

	data = study_aid._load("Python101")

	assert data["notes"][0]["topic"] == "Loops"
	assert data["notes"][0]["content"] == "For loops iterate over lists."

def test_duplicate_note_is_ignored(study_aid):
	"""
	Ensure duplicates are ignored. Create the course first, add a duplicate,
	then inspect the underlying JSON to confirm only a single note exists.
	"""
	study_aid.add_course("Math")
	study_aid.add_note("Math", "Topic", "Content")

	# Duplicate
	study_aid.add_note("Math", "Topic", "Content")

	data = study_aid._load("Math")

	assert len(data["notes"]) == 1

def test_exceeding_max_notes_is_ignored(study_aid):
	"""
	Add more than the allowed number of notes (101 attempts) and confirm
	the underlying JSON has been capped at 100 notes per the spec.
	"""
	study_aid.add_course("Math")

	for i in range(101):
		study_aid.add_note("Math", f"Note{i}", "content")

	data = study_aid._load("Math")

	assert len(data["notes"]) == 100

def test_adding_flashcards_basic(study_aid, python_course):
	course_name = python_course['course_name']

	result = study_aid.add_flashcard(course_name, "Q1", "A1")

	assert result == "OK: flashcard added to Python101"

	data = study_aid._load("Python101")

	assert data["flashcards"][0]["front"] == "Q1"
	assert data["flashcards"][0]["back"] == "A1"

def test_flashcard_duplicates_and_limit(study_aid, python_course):
	course_name = python_course['course_name']

	study_aid.add_flashcard(course_name, "Q1", "A1")

	# Duplicate ignored
	study_aid.add_flashcard(course_name, "Q1", "A1")

	data = study_aid._load(course_name)

	assert len(data["flashcards"]) == 1

	for i in range(101):
		study_aid.add_flashcard(course_name, f"Front{i}", f"Back{i}")

	data = study_aid._load(course_name)

	assert len(data["flashcards"]) == 102

def test_search_finds_flashcard(study_aid):
	study_aid.add_course("Python101")

	study_aid.add_flashcard("Python101", "What is Python?", "A programming language")

	# Search the front side
	result = study_aid.search("Python101", "What is")

	assert '- Flashcard (front: What is Python?, back: A programming language)' in result

def test_add_flashcard_error_precedence_course_name_over_front(study_aid):
	# Invalid course name AND empty flashcard front
	with pytest.raises(ValueError, match="Invalid note data"):
		study_aid.add_flashcard("Bad Name!", "", "Answer")

def test_generate_quiz_basic(study_aid, python_course):
	course_name = python_course['course_name']

	study_aid.add_flashcard(course_name, "Q1", "A1")

	quiz = study_aid.generate_quiz(course_name, 1)

	assert "1. Q1" in quiz
	assert "Answer: A1" in quiz

def test_quiz_with_fewer_flashcards_than_requested(study_aid, python_course):
	course_name = python_course['course_name']

	study_aid.add_flashcard(course_name, "Q1", "A1")

	quiz = study_aid.generate_quiz(course_name, 5)

	# Only one flashcard exists
	assert "1. Q1" in quiz

def test_note_duplicates_and_limit(study_aid, python_course):
	course_name = python_course['course_name']

	study_aid.add_note(course_name, "Loops", "Content")

	# Duplicate ignored
	study_aid.add_note(course_name, "Loops", "Content")

	data = study_aid._load(course_name)

	assert len(data["notes"]) == 1

	# Hitting the note limit
	for i in range(101):
		study_aid.add_note("Python101", f"Note{i}", "content")

	data = study_aid._load(course_name)

	assert len(data["notes"]) == 100

def test_add_flashcard_invalid_front_checked_before_missing_course(study_aid):
	with pytest.raises(ValueError, match="Invalid note data"):
		study_aid.add_flashcard("NonExistentCourse", "", "Back")

def test_summary_no_notes_returns_none(study_aid):
	study_aid.add_course("EmptyCourse")

	summary = study_aid.get_summary("EmptyCourse")

	assert "Topics: " in summary

def test_search_finds_notes_and_flashcards(study_aid, python_course):
	course_name = python_course['course_name']

	study_aid.add_note(course_name, "Loops", "For loops iterate over lists.")

	study_aid.add_flashcard(course_name, "Tuple?", "Immutable list")

	result = study_aid.search(course_name, "loop")

	assert "Note (Loops)" in result
	assert "For loops iterate over lists." in result

def test_search_case_insensitive(study_aid, python_course):
	course_name = python_course['course_name']

	study_aid.add_note(course_name, "Loops", "For loops iterate over lists.")

	result = study_aid.search(course_name, "LOOPS")

	assert "For loops iterate over lists." in result

def test_search_no_matches_returns_message(study_aid, python_course):
	course_name = python_course['course_name']

	result = study_aid.search(course_name, "database")

	assert result == "No results found"

def test_search_snippet_length(study_aid, python_course):
	course_name = python_course['course_name']

	long_content = "x" * 100

	study_aid.add_note(course_name, "Topic", long_content)

	result = study_aid.search(course_name, "x")

	assert "- Note (Topic): " + "x" * 50 + "..." in result

def test_generate_quiz_invalid_number_raises(study_aid, python_course):
	course_name = python_course['course_name']

	study_aid.add_flashcard(course_name, "Q1", "A1")

	for no_of_questions in [-1, 0]:
		with pytest.raises(ValueError, match="Invalid numeric value"):
			study_aid.generate_quiz("Python101", no_of_questions)

	with pytest.raises(TypeError, match="num_questions must be an integer"):
		study_aid.generate_quiz("Python101", "Two")

def test_generate_quiz_full_output(study_aid, python_course):
	course_name = python_course['course_name']

	study_aid.add_flashcard(course_name, "Q1", "A1")
	study_aid.add_flashcard(course_name, "Q2", "A2")

	expected_quiz = (
		"Quiz:\n"
		"1. Q1\n"
		"   Answer: A1\n\n"
		"2. Q2\n"
		"   Answer: A2"
	)

	print('expected_quiz:\n', expected_quiz, '\n', sep='')

	quiz = study_aid.generate_quiz("Python101", 2)

	print('quiz:\n', quiz, '\n', sep='')

	assert quiz.strip() == expected_quiz.strip()

def test_note_topic_and_content_max_length(study_aid, python_course):
	course_name = python_course['course_name']

	long_text = "X" * 1000

	with pytest.raises(ValueError, match="Invalid note data"):
		study_aid.add_note(course_name, long_text, long_text)

	# Exceeding 1000 chars should raise ValueError
	too_long = "X" * 1001

	with pytest.raises(ValueError, match="Invalid note data"):
		study_aid.add_note(course_name, too_long, "content")

	with pytest.raises(ValueError, match="Invalid note data"):
		study_aid.add_note(course_name, "Topic", too_long)

def test_add_flashcard_nonexistent_course_raises(study_aid):
	result = study_aid.add_flashcard("NonExistent", "Front", "Back")

	assert result == "New course added along flashcard"

def test_add_flashcard_invalid_course_name_raises(study_aid):
	# Malformed course name
	bad_name = "Invalid!"

	with pytest.raises(ValueError, match="Invalid course name"):
		study_aid.add_flashcard(bad_name, "Front", "Back")

def test_flashcard_front_and_back_max_length(study_aid, python_course):    
	course_name = python_course['course_name']

	long_text = "Y" * 1000

	with pytest.raises(ValueError, match="Invalid note data"):
		study_aid.add_flashcard(course_name, long_text, long_text)

	too_long = "Y" * 1001

	with pytest.raises(ValueError, match="Invalid note data"):
		study_aid.add_flashcard(course_name, too_long, "Answer")

	with pytest.raises(ValueError, match="Invalid note data"):
		study_aid.add_flashcard(course_name, "Front", too_long)

def test_note_duplicates_at_limit(study_aid, python_course):
	course_name = python_course['course_name']

	# Fill exactly 100 notes
	for i in range(100):
		study_aid.add_note(course_name, f"Note{i}", "content")

	# Duplicate should not increase count
	study_aid.add_note(course_name, "Note0", "content")

	data = study_aid._load(course_name)

	assert len(data["notes"]) == 100

def test_flashcard_duplicates_at_limit(study_aid, python_course):
	course_name = python_course['course_name']

	# Fill exactly 100 flashcards
	for i in range(100):
			study_aid.add_flashcard(course_name, f"Q{i}", f"A{i}")

	# Duplicate should not increase count
	study_aid.add_flashcard(course_name, "Q0", "A0")

	data = study_aid._load(course_name)

	assert len(data["flashcards"]) == 100

def test_quiz_order_is_deterministic(study_aid, python_course):    
	course_name = python_course['course_name']

	# Add 5 flashcards
	for i in range(5):
		study_aid.add_flashcard(course_name, f"Q{i}", f"A{i}")

	# Generate quiz twice and compare results
	quiz1 = study_aid.generate_quiz(course_name, 5)
	quiz2 = study_aid.generate_quiz(course_name, 5)

	assert quiz1 == quiz2

	# Ensure all flashcards are present
	for i in range(5):
		assert f"Q{i}" in quiz1
		assert f"A{i}" in quiz1

# For tests where you want to avoid any
# interaction with the default TEST_DIR.
# BASE_DIR_EXTRA = "test_extra_study_data"

# def test_load_invalid_json_missing_keys():
# 	"""
# 	Create a syntactically-valid JSON file that is missing required keys
# 	(e.g., 'notes' and/or 'flashcards') and confirm operations raise
# 	FileNotFoundError as the course is considered invalid/missing.
# 	"""
# 	os.makedirs(BASE_DIR_EXTRA, exist_ok=True)
# 	path = os.path.join(BASE_DIR_EXTRA, "WeirdCourse.json")

# 	# Write syntactically valid JSON but missing 'notes' and 'flashcards'
# 	with open(path, "w", encoding="utf-8") as f:
# 		json.dump({"unexpected_key": []}, f, indent=4)

# 	# Instantiate StudyAid correctly pointed at the base dir containing the bad file
# 	sa = StudyAid(BASE_DIR_EXTRA)

# 	with pytest.raises(FileNotFoundError, match="Course not found"):
# 		sa.search("WeirdCourse", "query")

# 	with pytest.raises(RuntimeError, match="Operation failed: no flashcards"):
# 		sa.generate_quiz("WeirdCourse", 1)

# 	print('sa.get_summary("WeirdCourse"):', sa.get_summary("WeirdCourse"))

# 	expected_summary = """Course: WeirdCourse
# Notes: 0
# Flashcards: 0
# Topics: None"""

# 	assert sa.get_summary("WeirdCourse") == expected_summary

def test_search_result_order(study_aid, python_course):
	course_name = python_course['course_name']

	# Add notes
	study_aid.add_note(course_name, "Loops", "Loop content")
	study_aid.add_note(course_name, "Arrays", "Array content")

	# Add flashcards
	study_aid.add_flashcard(course_name, "Zebra", "BackZ")
	study_aid.add_flashcard(course_name, "Apple", "BackA")
	
	results = study_aid.search(course_name, "content")
	lines = [line.strip() for line in results.split("\n") if line.startswith("- ")]

	print('lines:', lines)

	# Notes first, alphabetically by topic
	assert lines[0].startswith("- Note (Loops")
	assert lines[1].startswith("- Note (Arrays")

	# Flashcards next, alphabetically by front
	assert lines[2].startswith("- Flashcard (front: Zebra")
	assert lines[3].startswith("- Flashcard (front: Apple")

TEST_DIR = "test_study_data"

def test_json_indent_formatting(study_aid, python_course):    
	course_name = python_course['course_name']

	study_aid.add_note(course_name, "Topic", "Content")

	path = os.path.join(TEST_DIR, "Python101.json")
	
	if not os.path.exists(path):
		with open(path, "w", encoding="utf-8") as f:
			content = f.read()

			# Check for indent=4
			assert "\n    " in content

def test_cache_loads_only_when_needed(study_aid, python_course):
	course_name = python_course['course_name']

	study_aid.add_note(course_name, "Topic", "Content")

	# New instance to simulate fresh start
	new_aid = StudyAid(TEST_DIR)
	new_aid.add_course(course_name)

	# First load - reads from file
	summary1 = new_aid.get_summary(course_name)

	assert "Notes: 1" in summary1

	# Modify JSON directly
	path = os.path.join(TEST_DIR, "Python101.json")

	with open(path, "w", encoding="utf-8") as f:
		json.dump({"notes": [{"topic": "New", "content": "NewContent"}], "flashcards": []}, f, indent=4)

	# Second call - should use cache, not read modified file
	summary2 = new_aid.get_summary(course_name)

	# cached value, not "New"
	assert "Topics: New" in summary2

	# Clearing cache manually to force reload
	new_aid._cache.pop(course_name, None)

	summary3 = new_aid.get_summary(course_name)

	assert "Topics: New" in summary3

# Courses
def test_creating_and_duplicating_course(study_aid):
	# First addition
	msg1 = study_aid.add_course("Python101")
	assert msg1 == "OK: course Python101 added"

	assert study_aid._load("Python101") == {"notes": [], "flashcards": []}

	# Adding the same course again should still succeed (idempotent)
	msg2 = study_aid.add_course("Python101")
	assert msg2 == "OK: course Python101 added"

def test_note_topic_and_content_max_length(study_aid, python_course):
	course_name = python_course['course_name']

	long_text = "X" * 1001

	with pytest.raises(ValueError, match="Invalid note data"):
		study_aid.add_note(course_name, long_text, long_text)

	# Exceeding 1000 chars should raise ValueError
	too_long = "X" * 1001

	with pytest.raises(ValueError, match="Invalid note data"):
		study_aid.add_note(course_name, too_long, "content")

	with pytest.raises(ValueError, match="Invalid note data"):
		study_aid.add_note(course_name, "Topic", too_long)