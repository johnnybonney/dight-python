"""
Created on Tue Oct 10 18:24:47 2017

@author: johnf

DIGHT360 - Homework 5 - text analysis
"""

import os
import re
from glob import glob
from nltk import word_tokenize

os.chdir(r'C:\Users\johnf\Downloads\Mini-CORE\Mini-CORE')

master = []
for file in glob('*[0-9].txt'):
    register = file.split('+')[1]
    print(register)
    text_length = 0
    pronouns = 0
    modals = 0
    puncts = 0
    # pronouns
    regex1 = re.compile('it?|s?he|you|we|they|what|whom?|me|him|her|us')
    # modal verbs
    regex2 = re.compile('can|s?[hcw]ould|may|might|will|shall|must')
    # punctuation
    regex3 = re.compile(',|\.|\?|!')
    with open(file) as f:
        for line in f:
            if re.search('<[hp]>', line):
                words = word_tokenize(line.lower())
                for word in words:
                    if re.search(regex1, word):
                        pronouns += 1
                    elif re.search(regex2, word):
                        modals += 1
                    elif re.search(regex3, word):
                        puncts += 1
                text_length += len(words)
        prn_rate = round((pronouns/text_length)*1000, 1)
        mod_rate = round((modals/text_length)*1000, 1)
        pctn_rate = round((puncts/text_length)*1000, 1)
        master.append([file, register, prn_rate, mod_rate, pctn_rate])

with open('master_output.txt', 'w') as s:
    s.write('filename' + '\t\t\t\t\t\t' + 'register' + '\t' + 'pronouns' +
            '\t' + 'modals' + '\t\t' + 'punctuation' + '\n')
    for t in master:
        s.write(t[0] + '\t' + t[1] + '\t\t' + str(t[2]) + '\t\t' + str(t[3]) +
                '\t\t' + str(t[4]) + '\n')
