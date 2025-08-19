import random

# Python version:
# Python 3.12.9

# A particular task that needs to be
# stored in the priority queue.
class Job:
    """
    Represents a job to be processed in the priority queue.

    Attributes:
        name (str): The name or identifier of the job.
        priority (int): The priority level of the job (higher value = higher priority).
        time (int): The amount of time the job requires for execution.
    """
    def __init__(self, name, priority, time):
        """
        Initializes a new Job instance.

        Args:
            name (str): The name of the job.
            priority (int): The priority of the job.
            time (int): The execution time required for the job.
        """
        
        # Name/identifier for the job
        self.name = name

        # Priority of the job (higher = more important)
        self.priority = priority
        
        # Time units needed for execution
        self.time = time
        
        # Time the job waited before execution
        self.waiting_time = 0


class PriorityQueue:
	"""
	A priority queue for managing Job instances based on their priority.

	Methods:
		is_empty(): Returns True if the queue is empty.
		enqueue(job): Adds a job to the queue and sorts it by priority.
		dequeue(): Removes and returns the job with the highest priority.
	"""
	
	# Stores Job objects in order of execution.
	def __init__(self):
		# The square brackets [] indicate that a Python list
		# data structure is being created upon .
		# self.queue is empty, so len(self.queue) will return 0.

		# This will change as elements/items are enqueued
		# or inserted into priority queue object.
		self.queue = []

	def is_empty(self):
		# Returns True if self.queue is empty.
		return len(self.queue) == 0

	def enqueue(self, job):
		"""
		Adds a job to the queue and sorts the queue by priority.

		Args:
			job (Job): The job instance to be added.
		"""
		
		# Appending the object of the Job class
		# to self.queue list data structure.
		self.queue.append(job)
		
		# Sort jobs so that highest priority job comes first.
		self.queue.sort(key=lambda x: x.priority, reverse=True)

	def dequeue(self):
		"""
		Removes and returns the highest priority job from the queue.

		Returns:
			Job or None: The job with the highest priority, or None if
			the queue is empty.
		"""
		
		if self.is_empty():
			return None

		# Remove and return the first element located
		# in index zero.

		# Removes and returns the job with highest priority.
		return self.queue.pop(0)


def simulate_jobs(input_jobs, simulate_random_arrivals=False):
	"""
	Simulates job execution using a priority queue.

	Jobs are executed in order of priority. Optionally, random jobs
	can be generated during the simulation.

	Args:
		input_jobs (list of str): List of job descriptions in the
		format "Name Priority Time".
		
		simulate_random_arrivals (bool): If True, random jobs may
		arrive during the simulation.

	Returns:
		list of Job: List of completed jobs with updated waiting times.
	"""
	
	# Declare an object of the PriorityQueue class called "job_queue".
	job_queue = PriorityQueue()

	# Parse and enqueue each job from input.
	for job_data in input_jobs:
		# name, priority, time = "N 3 11"
		# name would be assigned "N",
		# priority would be assigned "3"
		# time would be assigned "11".    
		name, priority, time = job_data.split()
		
		# print('type(priority):', type(priority))

		# Cast the variables "priority" and "time"
		# as integers.
		job = Job(name, int(priority), int(time))
	
		# Insert the "job" object into the PriorityQueue
		# object called "job_queue".
		job_queue.enqueue(job)

	current_time = 0
	result = []

	while not job_queue.is_empty():
		current_job = job_queue.dequeue()
		
		# Assign the value of "current_time" to the
		# the instance attribute "waiting_time"
		# that belongs to the object of the Job
		# class called "current_job".
		current_job.waiting_time = current_time

		# while current_job.time > 0
		
		# First iteration for the first element
		# in the "input_jobs" list.
		# while 11 > 0:
		while current_job.time > 0:
			current_time += 1

			current_job.time -= 1

			if simulate_random_arrivals and random.randint(1, 100) < 3:
				new_priority = random.randint(1, 10)
				new_time = random.randint(1, 50)
				new_name = f"W{len(job_queue.queue) + 1}"
				new_job = Job(new_name, new_priority, new_time)
				job_queue.enqueue(new_job)

		result.append(current_job)

	return result


# Example input
input_jobs = [
	"N 3 11",
	"E 4 30",
	"T 6 15",
	"A 7 21",
	"F 8 25",
	"H 5 18"
]

# Additional input with at least 10 lines.
additional_input = [
	"J 2 10",
	"K 5 15",
	"L 8 20",
	"M 3 25",
	"P 7 30",
	"Q 6 35",
	"R 4 40",
	"S 9 45",
	"U 1 50",
	"V 10 5"
]

# Print header for the first simulation
# (static input, no random arrivals).
print("Output for example input:")

# Run the simulation on the predefined
# input without random job arrivals.
results = simulate_jobs(
	input_jobs,
	simulate_random_arrivals=False
)

# Iterate over the results and
# print job details.
for i, job in enumerate(results, 1):
	print(
    	f"{i} {job.name} {job.priority}"
		f"{job.time + job.waiting_time - job.waiting_time}"
		f"{job.waiting_time}")

# Print header for the second simulation
# (includes random job arrivals).
print("\nOutput for additional input:")

# Run the simulation on a different input
# with random job arrivals enabled.
results = simulate_jobs(
	additional_input,
	simulate_random_arrivals=True
)

# Iterate and print details for
# each job that was executed.
for i, job in enumerate(results, 1):
  print(
    f"{i} {job.name} {job.priority}"
	f"{job.time + job.waiting_time - job.waiting_time}"
	f"{job.waiting_time}")