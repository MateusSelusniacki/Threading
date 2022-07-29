import threading
import time

N_READERS = 15
N_WRITERS = 2

lock = threading.Lock()
n_pages = 15
pages_writed = 0

class reader(threading.Thread):
    def __init__(self,id):
        super().__init__()
        self.id = id
        return
 
    def run(self):
        global lock
        page = 0
        while(page != n_pages):
            page += 1
            lock.acquire()
            
            time.sleep(0.3)
            print(self.id,' is reading the page ', page)

            lock.release()
    
class writer(threading.Thread):
    def __init__(self,id):
        super().__init__()
        self.id = id
        return
    
    def run(self):
        global pages_writed
        while(pages_writed != n_pages):
            pages_writed += 1

            lock.acquire()
            
            print('writer ', self.id, 'is writing the page: ', pages_writed)
            time.sleep(1)

            lock.release()

if __name__ == "__main__":
    for i in range(N_WRITERS):
        p = [writer(i) for i in range(N_WRITERS)]

    for i in range(N_READERS):
        r = [reader(i) for i in range(N_READERS)]
    
    for i in p:
        i.start()
    for i in r:
        i.start()

    for i in r:
        i.join()
    for i in p:
        i.join()