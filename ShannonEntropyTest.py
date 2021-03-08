# In Anlehnung an
# Quelle: http://blog.dkbza.org/2007/05/scanning-data-for-entropy-anomalies.html
# Für die Thesis ensprechend modifziert für eine Untersuchung auf Blockgrösse

import math, string, sys, fileinput
from textwrap import wrap
import math


f = open("./research/word/01e/shannondata.txt", "r")

#--------------------------------------
# In Datei schreiben
#--------------------------------------
resultspath = "./results/results_entropy.txt";
open(resultspath, 'w').close()

def write_file(inhalt):
  with open(resultspath, 'rb') as f:
   f = open(resultspath, "a")
   f.write(inhalt)
   #print("Write file: " + inhalt)
   f.close()
  return ""
#--------------------------------------
# Datei öffnen --------
#--------------------------------------
data1 = f.read()
blocksize = 256 #Blockgrösse 256
cluster = wrap(data1, blocksize ) #Blockgrösse 256

durchlauf = math.ceil(len(data1)/(blocksize))+1
print (durchlauf)

#Zeilenumbrüche entfernen -------- 
#data1 = data1.replace("\n", " ")
#print(data1)

#Doppelte Zeichen aus Untersuchungsbreiech entfernen für Vergleich -------- 
tempdata1 = data1
result = "".join(dict.fromkeys(tempdata1))
#print(result)


def range_bytes (): return range(256)

def range_printable(): return (ord(c) for c in result)

def H(data, iterator=range_bytes):
    if not data:
        return 0
    entropy = 0
    for x in iterator():
        p_x = float(data.count(chr(x)))/len(data)
        #print (chr(x))
        if p_x > 0:
            entropy += - p_x*math.log(p_x, 2)
            #print (chr(x), p_x) # mit einzelnen Chars ausgeben
            #print (p_x) # Nur die
    return entropy

it = 0
#Entropie ausrechnen für die eingelesene Datei -------- 
print ("Entropy")
for x in range(1, durchlauf):
  for str in [cluster[it]]:
      floatString = round((H(str, range_printable)), 4)
      blockentropy = "{:.4f}".format(floatString)
      write_file(blockentropy + "\n")
  it = it+1



