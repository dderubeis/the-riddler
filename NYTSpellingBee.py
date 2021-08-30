#!/usr/bin/env python
# coding: utf-8

# In this game, seven letters are arranged in a honeycomb lattice, with one letter in the center.
# 
# The goal is to identify as many words as possible that meet the following criteria:
# 1. The word must be at least four letters long.
# 2. The word must include the central letter.
# 3. The word cannot include any letter beyond the seven given letters.
# 
# Letters can be repeated.
# 
# Points are awarded based on the number of letters in the word. If the submission includeds all seven letters in the honeycomb, it is known as a pangram and gets 15 points: 8 regular points plus 7 bonus points.

# In[212]:


import re
import string
import requests
from bs4 import BeautifulSoup
import json

def is_valid(word) -> bool:
    """is word 4 or more letters, not including 'S', and no more than 7 distinct letters"""
    return len(word) >=4 and not word.endswith('S') and len(set(word)) <= 7

def word_list(text) -> List[str]:
    """All the valid words in uppercase text"""
    return [w for w in text.upper().split() if is_valid(w)]

def is_pangram(word) -> bool:
    return len(set(word)) == 7

def word_score(word) -> int:
    """The points for this word, including a bonus if it's a pangram"""
    return 1 if len(word) == 4 else len(word) + 7 * is_pangram(word)

words = word_list(open("words.txt").read().replace('\n', ' '))
URL = "https://www.nytimes.com/puzzles/spelling-bee"

def get_honeycomb(url):
    """Collects the Honeycomb of the day from the NYT website"""
    page = requests.get(URL, headers= {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'})
    soup = BeautifulSoup(page.text, "html.parser")
    script = soup.findAll('script')[0].string
    jsvar, _, jsvalue = script.partition('=')
    data = json.loads(jsvalue)
    return data

outer_letters = [l.upper() for l in data["today"]["outerLetters"]]
valid_letters = ''.join([l.upper() for l in data["today"]["validLetters"]])
center_letter = data["today"]["centerLetter"].upper()

def check_word(word, valid_letters, center_letter):
    """Returns TRUE if word contains only letters from the Honeycomb"""
    rest_of_alphabet = re.sub(f'[{valid_letters_str}]', '', string.ascii_uppercase)
    if center_letter not in word:
        return False
    if re.search(f'[{rest_of_alphabet}]', word):
        return False
    return True

def solve_puzzle(words):
    qualifying_words = []
    points = 0
    for w in words:
        if check_word(w, valid_letters, center_letter) == True:
            points += word_score(w)
            qualifying_words.append(w)
    return qualifying_words, points

def check_submission(todays_submission, todays_points):
    status_report = ""
    todays_answers = [x.upper() for x in data["today"]["answers"]]
    status_report += '\nPuzzle Date: {todays_date}'.format(todays_date=data["today"]["displayDate"])
    if todays_submission == todays_answers:
        status_report += '\nYou win!'
    else:
        status_report += '\nThe NYT vs. You: '
        status_report += str(list(set(todays_answers) - set(todays_submission)))
        status_report += '\nYou vs. The NYT: '
        status_report += str(list(set(todays_submission) - set(todays_answers)))
    status_report += '\nYour points: {todays_points}'.format(todays_points=str(todays_points))
    status_report += '\nThe NYT points: {possible_points}'.format(possible_points=str(sum([word_score(w) for w in todays_answers])))
    return status_report

todays_submission, todays_points = solve_puzzle(words)

with open("NYTSpellingBee.txt", "w") as text_file:
    text_file.write('\n' + check_submission(todays_submission, todays_points))
    text_file.close()


# In[ ]:




