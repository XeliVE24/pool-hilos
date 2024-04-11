
import time 
import logging
from concurrent.futures import ThreadPoolExecutor

def contadorDos(inicio,fin):
    logging.info(f'funcion con rango:{inicio}-{fin}')
    for i in range(inicio,fin+1,1):
        globalArrayNum.append(i)
        time.sleep(0.01)
    return 0

t0=time.time()

globalArrayNum=[]
rangos=[(1,50),(51,100),(101,150),(151,200)]
with ThreadPoolExecutor(max_workers=2) as executor:
    for i ,rango in enumerate (rangos):
        t=executor.submit(contadorDos, rango)
  
tf=time.time()-t0
print(f"tiempo total de ejecucion:{tf}")
print(globalArrayNum)