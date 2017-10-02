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
