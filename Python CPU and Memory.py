'''Here's a Python script that performs CPU and memory stress testing. As with the Bash script, please use it with caution and only on test/staging environments, as it can impact server performance'''

# we will import some libraries

import multiprocessing
import time
import hashlib

# Set the duration for which you want to stress the CPU and memory (in seconds)
duration = 300

# Function to stress CPU
def stress_cpu():
    num_cpus = multiprocessing.cpu_count()
    num_cpu_processes = num_cpus * 2
    processes = []

    for _ in range(num_cpu_processes):
        process = multiprocessing.Process(target=cpu_worker)
        processes.append(process)
        process.start()

    time.sleep(duration)

    for process in processes:
        process.terminate()
        process.join()

# CPU-bound worker function
def cpu_worker():
    while True:
        # This mathematical operation will stress the CPU
        result = 4 * (4 * (4 * (4 * (4 * 1.0))))

# Function to stress memory
def stress_memory():
    # Allocate memory in 100MB chunks until the duration ends
    end_time = time.time() + duration

    while time.time() < end_time:
        # Allocate 100MB
        data = hashlib.md5(b'\0' * (100 * 1024 * 1024))

if __name__ == "__main__":
    # Start the CPU and memory stress functions in the background
    cpu_process = multiprocessing.Process(target=stress_cpu)
    memory_process = multiprocessing.Process(target=stress_memory)

    cpu_process.start()
    memory_process.start()

    cpu_process.join()
    memory_process.join()

#This Python script achieves the same objectives as the Bash script:

'''Stress the CPU by running multiple CPU-bound processes and stress memory by repeatedly allocating and deallocating memory.'''

'''You can adjust the `duration` variable to control how long you want the script to run. 
As before, be cautious when using such scripts, especially in production environments, as they can impact server performance. 
Always test in a controlled environment first.'''