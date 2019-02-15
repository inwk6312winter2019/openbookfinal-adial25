
from collections import Counter
from string import punctuation


def content_text(text):
    stopwords = set(nltk.corpus.stopwords.words('english')) 
    with_stp = Counter()
    without_stp  = Counter()
    with open("book1.txt","r") as f:
        for line in f:
            spl = line.split()
            with_stp.update(w.lower().rstrip(punctuation) for w in spl if w.lower() in stopwords)
            without_stp.update(w.lower().rstrip(punctuation)  for w in spl if w  not in stopwords)
    return [x for x in with_stp.most_common(10)],[y for y in without_stp.most_common(10)]
wth_stop, wthout_stop = content_text(...)
