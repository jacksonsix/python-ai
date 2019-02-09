#f = open("data.txt", "r")
#print(f.read()) 
import csv

with open('data.txt', 'rb') as csvfile:
     spamreader = csv.reader(csvfile, delimiter=',')
     print(type(spamreader))
     mlist = list(spamreader)
     print(mlist[0][10])
     mlist[0].pop()
     floatlist = [float(i) for i in mlist[0]]
     print(type(floatlist[10]))
     print(len(mlist[0]))
     #for item in mlist[0]:
     #  print(float(item)*3)
