import threading
import time 
import logging
from concurrent.futures import ThreadPoolExecutor

logging.basicConfig(level=logging.DEBUG,format='%(threadName)s:%(message)s')
print("--------------dos hilos----------")

globalArrayNum=[]
def contadorDos(inicio,fin):
    logging.info(f'funcion con rango:{inicio}-{fin}')
    for i in range(inicio,fin+1,1):
        globalArrayNum.append(i)
        time.sleep(0.01)
    return 0
t0=time.time()
listaHilos=[]


t=threading.Thread(target=contadorDos,args=(1,50))
listaHilos.append(t)
t.start()
t=threading.Thread(target=contadorDos,args=(51,100))
listaHilos.append(t)
t.start()

t0=time.time()

for t in listaHilos:
    t.join()
    
tf=time.time()-t0
print(f"tiempo total de ejecucion:{tf}")
print(globalArrayNum)
print("----------------pool hilos--------------------")
def printHW():
    logging.info(f'funcion HW:')
    print("holamundo")
t0=time.time()
globalArrayNum=[]
with ThreadPoolExecutor(max_workers=2) as executor:
    executor.submit(contadorDos, 1,50)
    executor.submit(contadorDos, 51,100)
    executor.submit(contadorDos, 101,150)
    executor.submit(contadorDos, 151,200)
    executor.submit(printHW)
    
tf=time.time()-t0
print(f"tiempo total de ejecucion:{tf}")
print(globalArrayNum)