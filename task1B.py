from collections import Counter
wordlist = open('book1.txt','r').read()
c = Counter(wordlist)
print (c)
# split() returns list of all the words in the string 

  
# Pass the split_it list to instance of Counter class. 
Counter = Counter(c) 
  
# most_common() produces k frequently encountered 
# input values and their respective counts. 
most_occur = Counter.most_common(20) 
  
print(most_occur)
