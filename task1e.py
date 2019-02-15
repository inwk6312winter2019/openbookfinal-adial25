with open('book1.txt') as infile:
    for line in infile:
        wordslist1=line.split()
        if wordslist1[0] in 'aeiou':
            print(wordslist1)

with open('book2.txt') as infile:
    for line in infile:
        wordslist2=line.split()
        if wordslist2[0] in 'aeiou':
            print(wordslist2)

with open('book3.txt') as infile:
    characters1=0
    for line in infile:
        wordslist3=line.split()
        if wordslist3[0] in 'aeiou':
            print(wordslist3)
            
