#!/usr/bin/python

from os import path
import urllib3
import re 
import bs4
import nltk
import wordcloud as wc
import matplotlib.pyplot as plt
import pylab

wrk_dir = path.dirname(__file__)

print ('-') * 30
print ("   M A I N - M E N U")
print ('-') * 30
print ("1. Text File")
print ("2. Web page")
print ('-') * 30

is_valid=0
 
while not is_valid :
    try :
        choice = int (input('Enter your choice [1 or 2]: '))
        is_valid = 1 ## set it to 1 to validate input and to terminate the while..not loop
    except ValueError, e :
        print ("'%s' is not a valid integer." % e.args[0].split(": ")[1])

### Take action as per selected menu-option ###
if choice == 1:
    dirty_file = input('Please enter a file name: ') ##getting file
    print ("%s will be uploaded, cleaned and frequencies of words generated.") % dirty_file
    text = open(path.join(wrk_dir, dirty_file)).read()
    print (len(text))
    tokens = [tok for tok in text.split()]
    print ("Number of individual words: %s") % len(tokens)
    print (tokens [:10]) ##visually checking to see that file is clean
    Freq_dist_nltk=nltk.FreqDist(tokens)
    #print Freq_dist_nltk
    stopwords =[ word.strip().lower() for word in open(path.join(wrk_dir, "english.stop.txt"))]
    clean_tokens =[ tok for tok in tokens if len(tok.lower())>1 and (tok.lower() not in stopwords)]
    Freq_dist_nltk = nltk.FreqDist(clean_tokens)
    print ()"Removing stopwords and re-calculating totals")
    #print Freq_dist_nltk
    Freq_dist_nltk.plot(50, cumulative=False)
    wordcloud = wc.WordCloud().generate(text)
    plt.axis("off")
    plt.imshow(wordcloud)
    pylab.show()
    
elif choice == 2:
    dirty_www = input("Please enter a web page address - don't forget the http://: ")
    print ("%s will be uploaded, cleaned and frequencies of words generated.") % dirty_www
    response = urllib2.urlopen(dirty_www)
    web = response.read()
    print ("Number of words read in: %s") % len(web)
    soup = bs4.BeautifulSoup(web, 'html.parser')
    clean_www = soup.get_text()
    tokens = re.split('\\W+', clean_www)
    print ("Number of individual words: %s") % len(tokens)
    print (tokens [:100])
    Freq_dist_nltk=nltk.FreqDist(tokens)
    print (Freq_dist_nltk)
    stopwords = [word.strip().lower() for word in open(path.join(wrk_dir, "english.stop.www.txt"))]
    clean_tokens = [tok for tok in tokens if len(tok.lower())>1 and (tok.lower() not in stopwords)]
    Freq_dist_nltk = nltk.FreqDist(clean_tokens)
    print ("Removing stopwords and re-calculating totals")
    print (Freq_dist_nltk)
    Freq_dist_nltk.plot(50, cumulative=False)
    wordcloud = wc.WordCloud().generate(clean_www)
    plt.axis("off")
    plt.imshow(wordcloud)
    pylab.show()
else:
    print ("Invalid number. Try again...")
