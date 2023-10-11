import os.path, subprocess
import random
from subprocess import STDOUT, PIPE
import time


def compile_java(java_file):
    subprocess.check_call(['javac', java_file])


def execute_java(java_file):
    stdin = None

    start_time = time.time()

    java_class, ext = os.path.splitext(java_file)
    cmd = ['java', java_class]
    proc = subprocess.Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
    stdout, stderr = proc.communicate(stdin)

    end_time = time.time()
    return end_time - start_time

compile_java('Search.java')

times = []
number_of_tests = 1
total_time = 0

for i in range(number_of_tests):
    times.append(execute_java('Search'))
    total_time += times[i]

print("Average time:", total_time / number_of_tests)
print("Max time:", max(times))
print("Min time:", min(times))