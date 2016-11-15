#!/usr/bin/python

from os import path
import urllib2
import re 
import bs4
import nltk
#import wordcloud
#import matplotlib

wrk_dir = path.dirname(__file__)

print (30 * '-')
print ("   M A I N - M E N U")
print (30 * '-')
print ("1. Text File")
print ("2. Web page")
print (30 * '-')

is_valid=0
 
while not is_valid :
    try :
        choice = int (raw_input('Enter your choice [1-3] : '))
        is_valid = 1 ## set it to 1 to validate input and to terminate the while..not loop
    except ValueError, e :
        print ("'%s' is not a valid integer." % e.args[0].split(": ")[1])

### Take action as per selected menu-option ###
if choice == 1:
    dirty_file = raw_input('Please enter a file name: ')
    print "%s will be uploaded, cleaned and frequencies of words generated." % dirty_file
    text = open(path.join(wrk_dir, dirty_file)).read()
    print len(text)
elif choice == 2:
    dirty_www = raw_input("Please enter a web page address - don't forget http://: ")
    print "%s will be uploaded, cleaned and frequencies of words generated." % dirty_www
    response = urllib2.urlopen(dirty_www)
    web = response.read()
    print len(web)
    tokens = re.split('\W+',web)
else:
    print "Invalid number. Try again..."
