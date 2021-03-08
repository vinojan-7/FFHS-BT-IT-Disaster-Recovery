from scipy.stats import chisquare
# -*- coding: utf-8 -*-
from textwrap import wrap
import numpy as np
import math
import binascii
import os

sourcepath = "./research/aes/03a/";

#--------------------------------------
# In Datei schreiben
#--------------------------------------
resultspath = "./results/results_chi2.txt";
open(resultspath, 'w').close()

def write_file(inhalt):
  with open(resultspath, 'rb') as f:
   f = open(resultspath, "a")
   f.write(inhalt)
   #print("Write file: " + inhalt)
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
# Funktion: Arrayinhalt zählen
#--------------------------------------
def organize_array(arrayname):
 z = arrayname
 indexarray =[]
 arr = []
 # Array erstellen, Werte zählen und zuweisen
 i = 0;
 
 for x in range(0, 256):
  anzahl = z.count(i);
  if anzahl > 0:
   indexarray.append(i);
   arr.append(anzahl);
  i = i+1;
 #print( indexarray) #Indexe anzeigen
 return arr
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
   array1 = organize_array(array1[start*it-start:start*it]);
   #print(array1)
   chi2 = chisquare(array1)
   chi2string = str(chi2).split('=')[1].lstrip().split(',')[0]
   chi2string = float(chi2string)
   chi2string = str(round(chi2string, 2)) 
   #print ("N: ", len(array1))
   write_file(chi2string + "\n")
   it=it+1
  print("Chi-Test abgeschlossen")
  write_file("\n")
