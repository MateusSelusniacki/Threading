import threading
import time
from random import uniform

N_PHILOSOPHERS = 5  
eat_flag = [0 for i in range(N_PHILOSOPHERS)]
cutlery = [threading.Lock() for i in range(N_PHILOSOPHERS)]

class philosopher(threading.Thread):
    def __init__(self,id):
        super().__init__()
        self.id = id
        return
    
    def run(self):
        global cutlery

        while(True):
            time.sleep(uniform(2, 3))
            while(True):
                cutlery[self.id].acquire(True)
                locked = cutlery[(self.id + 1)%N_PHILOSOPHERS].acquire(False)
                if(locked):
                    cutlery[self.id].release()
                    break
                time.sleep(1)
                print('filosofo', self.id, 'comeu')
                eat_flag[self.id]

                cutlery[self.id].release()
                try:
                    cutlery[(self.id + 1)%N_PHILOSOPHERS].release()
                except:
                    pass

p = [philosopher(i) for i in range(N_PHILOSOPHERS)]

for i in p:
    i.start()

for i in p:
    i.join()