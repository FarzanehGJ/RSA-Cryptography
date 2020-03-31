# Write Python3 code here 
from decimal import Decimal
import tkinter as tk
import time

def _result_(value):

    print(*value)
    "value.configure(text = ""Result: "" + str(eval(entry.get())))"


"Encryption Function"
def __encryption__():

    Start_time = time.time()
    print(Start_time)
    
    Plait_text = e3.get()
    p = int(e1.get())
    q = int(e2.get())

    Plait_text = Plait_text.lower()
    output = []
    pt_ascci = []

    for character in Plait_text:
        "converting characters to ASCII number"
        number = En[character]
        print(number)
        "number = ord(character) - 96"
        "print(number)"

        "Genetaring Keys"
        n = p*q 
        t = (p-1)*(q-1)

        for e in range(2,t): 
                if gcd(e,t)== 1: 
                        break

        for i in range(1,10): 
                x = 1 + i*t 
                if x % e == 0: 
                        d = int(x/e) 
                        break

        "Computing Cipher Text"
        ctt = Decimal(0) 
        ctt =pow(number,e) 
        ct = ctt % n

        ctx = De[ct]
        "ctx = chr(ct + 96)"
        pt_ascci.append(ctx)

    "Find the execution time"
    Finish_time = time.time()
    print(Finish_time)
    execution_time = Finish_time - Start_time
    print(execution_time)

    tk.Label(r, text="Result of Encryption").grid(row=6)
    tk.Label(r, text=(pt_ascci)).grid(row=7,column=0)
    tk.Label(r, text=(execution_time)).grid(row=8,column=0)

    
       
"Decryption Function"
def __decryption__():

    Start_time = time.time()
    print(Start_time)

    Cipher_text = e3.get()
    p = int(e1.get())
    q = int(e2.get())

    Cipher_text = Cipher_text.lower()
    output = []
    pt_ascci = []

    for character in Cipher_text:
        "converting characters to ASCII number"
        number = En[character]
        print(number)
        "number = ord(character) - 96"

        "Genetaring Keys"
        n = p*q 
        t = (p-1)*(q-1) 

        for e in range(2,t): 
                if gcd(e,t)== 1: 
                        break

        for i in range(1,10): 
                x = 1 + i*t 
                if x % e == 0: 
                        d = int(x/e) 
                        break
        
        "Computing Decrypted Text"
        dtt = Decimal(0) 
        dtt = pow(number,d) 
        dt = dtt % n
        print(dt)
        dtx = De[dt]
        "dtx = chr(dt + 96)"
        pt_ascci.append(dtx)

    "Find the execution time"
    Finish_time = time.time()
    print(Finish_time)
    execution_time = Finish_time - Start_time
    print(execution_time)
        
    tk.Label(r, text="Result of Decryption").grid(row=6)
    tk.Label(r, text=(pt_ascci)).grid(row=7,column=0)
    tk.Label(r, text=(execution_time)).grid(row=8,column=0)

def gcd(a,b): 
	if b==0: 
		return a 
	else: 
		return gcd(b,a%b)


"Main part of the code"

"Encrypthion Dictionary"
En={'-': 0, 'a': 1, 'A': 1, 'b': 2, 'B': 2, 'c': 3, 'C': 3, 'd': 4, 'D': 4, 'e': 5, 'E': 5, 'f': 6,
'F': 6, 'g': 7, 'G': 7, 'h': 8, 'H': 8, 'i': 9, 'I': 9, 'j': 10, 'J': 10, 'k': 11, 'K': 11,
'l': 12, 'L': 12, 'm': 13, 'M': 13, 'n': 14, 'N': 14, 'o': 15, 'O': 15, 'p': 16, 'P': 16,
'q': 17, 'Q': 17, 'r': 18, 'R': 18, 's': 19, 'S': 19, 't': 20, 'T': 20, 'u': 21, 'U': 21,
'v': 22, 'V': 22, 'w': 23, 'W': 23, 'x': 24, 'X': 24, 'y': 25, 'Y': 25, 'z': 26, 'Z': 26,
'0': 27, '1': 28, '2': 29, '3': 30, '4': 31, '5': 32, '6': 33, '7': 34, '8': 35, '9': 36,
'.': 37, '?': 38, ',': 39, '_': 40, ' ':41}

De = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k',
12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u',
22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z', 27: '0', 28: '1', 29: '2', 30: '3', 31: '4',
32: '5', 33: '6', 34: '7', 35: '8', 36: '9', 37: '.', 38: '?', 39: ',', 40: '-', 41:' '}

r = tk.Tk()
r.geometry('380x200')
r.title('RSA Algorithm')

tk.Label(r, text="Enter p:").grid(row=0)
tk.Label(r, text="Enter q:").grid(row=1)
tk.Label(r, text="Enter Your Text:").grid(row=2)
e1 = tk.Entry(r)
e2 = tk.Entry(r)
e3 = tk.Entry(r)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)


tk.Label(r, text="Choose Encryption or Decryption").grid(row=3)

button1 = tk.Button(r, text='Encription', width=25, command=__encryption__).grid(row=4,column=0)
button2 = tk.Button(r, text='Decryption', width=25, command=__decryption__).grid(row=4,column=1)

r.mainloop()

       
