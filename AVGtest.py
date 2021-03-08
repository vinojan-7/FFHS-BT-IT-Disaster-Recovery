from textwrap import wrap
from statistics import mean
import math 
import binascii
import os

sourcepath = "./research/images/01/";
#--------------------------------------
# In Datei schreiben
#--------------------------------------
resultspath = "./results/results_avg.txt";
open(resultspath, 'w').close()

def write_file(inhalt):
  with open(resultspath, 'rb') as f:
   f = open(resultspath, "a")
   f.write(inhalt)
   f.close()
  return ""

#--------------------------------------
# Funktion: Alle Dateien im Ordner indexieren
#--------------------------------------
def index_folder(path):
 fileslist = []
 for root, dirs, files in os.walk(path):
   for filename in files:
    if(filename != ".DS_Store"):
        fileslist.append(filename);
 return fileslist

#--------------------------------------
# Funktion: Datei öffnen 
#--------------------------------------
def hex_array(filename):
 with open(filename, 'rb') as f:
  hexdata = binascii.hexlify(f.read())
  content = str(hexdata)
  content = content[2:]
  content = content[:-1]
    
 res = int(content, 16) 
 test = wrap(content, 2)
 temp = [] 

 j = 0;
 for x in test:
  res = int(test[j], 16) 
  temp.append(res) #+1 for 0
  j = j+1;
 return temp

#--------------------------------------
# Average driver
#--------------------------------------
def Average(lst): 
    return mean(lst) 


#--------------------------------------
# Hauptprgramm
#--------------------------------------
folder = sourcepath
foldercontent = index_folder(folder)

for x in foldercontent:
  print(x)
  file = hex_array(folder + x);
  write_file(x + "\n")

  it=1;
  start=4096;
  durchlauf = math.ceil(len(file)/(start))+1
  print("Durchlauf von Cluster: ", durchlauf)

  for x in range(1, durchlauf):
   array1 = file;
   array1 = array1[start*it-start:start*it];
   #print(array1)
   average = Average(array1) 
   averagestring = str(round(average, 2)) 
   write_file(averagestring + "\n")
   it=it+1
  print("Average-Test abgeschlossen")
  write_file("\n")

