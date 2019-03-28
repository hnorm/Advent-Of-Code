key = "bgvyzdsv"

import hashlib
from multiprocessing import Process, Queue
import time
import cProfile, pstats, io

def part_one(key):
    i = 0
    while True:
        i += 1
        m = hashlib.md5(f"{key}{i}".encode('utf-8'))
        if m.hexdigest()[:6] == "000000":
            return i

def miner_process(result, start, step):
    i = start
    while True:
        i += step
        if hashlib.md5(f"{key}{i}".encode('utf-8')).hexdigest()[:6] == "000000":
            result.put(i)
            return i

def part_two(key):
    result = Queue()
    procs = []
    procs.append(Process(target=miner_process, args=(result, 0, 4)))
    procs.append(Process(target=miner_process, args=(result, 1, 4)))
    procs.append(Process(target=miner_process, args=(result, 2, 4)))
    procs.append(Process(target=miner_process, args=(result, 3, 4)))

    for proc in procs:
        proc.start()

    while True:
        if not result.empty():
            for proc in procs:
                proc.terminate()
                proc.join()
            return result.get()

if __name__ == '__main__':
    print(part_one(key))
    print(part_two(key))