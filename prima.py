import time
from celery import Celery
import json
prima = Celery('service', broker='redis://127.0.0.1:6379/0', backend='redis://127.0.0.1:6379/0')

prima.conf.task_routes = {
    'prima.getprima': {'queue': 'prima'}
}

def primaa(a):
    angka = a
    konfirmasi = 0
    for x in range(1,angka+1):
        angka2 = angka % x
        if angka2 == 0:
            konfirmasi = konfirmasi + 1

    if konfirmasi == 2:
        return True
    else:
        return False

@prima.task
def getprima(a, b):
    result = []
    time.sleep(2) 
    count = 0
    c = 1
    while(count<a):
        if(primaa(c)):
            count = count + 1
        if count < a:
            c = c + 1

    result = {
        "result" : c
    }
    return result
        

    

