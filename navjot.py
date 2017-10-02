import date, import time
fin=open("README.md")
def file_fn(fin):
 word2=list()
 for line in fin:
  word=line.strip()
  word2.append(word.split("!"))
 for item in word2:
  if "crime" in str(item):
   print(item)
  if "date" in str(item):
   print(item)
file_fn(fin)

fin2=open("Crime.csv")
def file_fn(fin2):
 word1=list()
 list=['crime Type', 'crime ID', 'crime Count']
 for line in fin2:
  word=line.strip()
  word1.append(word.split("!"))
 for item in word1:
  if "crime Type" in str(item):
   print(item)
  if "crime ID" in str(item):
   print(item)
file_fn(fin2)


def list_crimes(crimes):
 incidents=make_requests()
 for i in incidents:
  crimes.point(float(incident['y']), float(incident['x']),0,0) 
 crimes.save()
