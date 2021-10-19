import sys
f = open('wordfrequency.txt', 'r')
def word_count(str):
  words = str.split() 
  counts = dict() 
  for word in words:
    if word in counts:
      counts[word] += 1
    else:
      counts[word] = 1
  return counts 
file_contents = f.read()
print(word_count(file_contents))












  






























