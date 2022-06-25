import time
from celery import Celery
import json
palindrom = Celery('service', broker='redis://127.0.0.1:6379/0', backend='redis://127.0.0.1:6379/0')

palindrom.conf.task_routes = {
    'palindrom.getpalindrom': {'queue': 'palindrom'}
}

def palindromm(a):
  angka = a
  angka2 = angka
  hasil = 0    
  while(angka > 0):    
      penghitung = angka %10    
      hasil = (hasil *10) + penghitung   
      angka = angka //10    
  if hasil == angka2:
      return True
  else:
      return False

def prima(a):
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


    
@palindrom.task
def getpalindrom(a, b):
    result = []
    count = 0
    c = 1
    while(count<a):
        if(prima(c) & palindromm(c)):
            count = count + 1
        if count < a:
            c = c + 1
            
    result = {
        "result" : c
    }
    return result