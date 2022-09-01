import multiprocessing
import os
# Creating the tuple of all the processes
all_processes = ('tagdb1.py', 'tagdb2.py', 'tagdb3.py', 'tagdb4.py', 'tagdb5.py', 'tagdb6.py')


# This block of code enables us to call the script from command line.
def execute(process):
    os.system(f'python {process}')


process_pool = multiprocessing.Pool(processes=6)
process_pool.map(execute, all_processes)