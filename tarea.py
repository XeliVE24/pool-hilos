
import time 
import logging
from concurrent.futures import ThreadPoolExecutor
logging.basicConfig(level=logging.DEBUG,format='%(threadName)s:%(message)s')
def contadorDos(inicio,fin):
    logging.info(f'funcion con rango:{inicio}-{fin}')
    for i in range(inicio,fin+1,1):
        globalArrayNum.append(i)
        time.sleep(0.01)
    return 0

t0=time.time()

globalArrayNum=[]
rangos=[(1,50),(51,100),(101,150),(151,200)]
rango=len(rangos)
with ThreadPoolExecutor(max_workers=min(rango,2)) as executor:
    for rango in rangos:
        t=executor.submit(contadorDos, rango[0],rango[1])
  
tf=time.time()-t0
print(f"tiempo total de ejecucion:{tf}")
print(globalArrayNum)
