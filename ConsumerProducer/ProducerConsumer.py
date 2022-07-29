import threading
import time

CAPACITY = 5
buffer_production = [i for i in range(CAPACITY)]

mutex = threading.Semaphore()
empty = threading.Semaphore(CAPACITY) 
full = threading.Semaphore(0)

in_buf = 0
out_buf = 0

class producer(threading.Thread):
    def run(self):
        global CAPACITY
        global mutex, empty, full
        global buffer_production, in_buf, out_buf
        produced = 0

        while(produced < 50):
            empty.acquire()
            mutex.acquire()

            produced += 1
            buffer_production[in_buf] = produced
            in_buf = (in_buf + 1)%CAPACITY
            print('produzido ',produced)

            mutex.release()
            full.release()

class consumer(threading.Thread):
    def run(self):
        consumed = 0
        global CAPACITY
        global mutex, empty, full
        global buffer_production, in_buf, out_buf

        while(consumed < 50):
            full.acquire()
            mutex.acquire()

            consumed += 1
            cons = buffer_production[out_buf]
            out_buf = (out_buf + 1)%CAPACITY
            print('consumido ',cons)

            mutex.release()
            empty.release()

if __name__ == "__main__":
    p = consumer()
    c = producer()

    p.start()
    c.start()

    p.join()
    c.join()