# Function to print common characters of two strings
from collections import Counter 
  
def common(a,b): 
      
    # convert both strings into counter dictionary 
    dicta = Counter(a) 
    dictb = Counter(b) 
  
    # take intersection of these dictionaries 
    commondict = dicta & dictb
  
    # if len(commondict) == 0: 
        # print(-1)
    
    return len(commondict)
  
    # get a list of common elements 
    commonchars = list(commonDict.elements()) 
  
    # sort list in ascending order to print resultant  
    # string on alphabetical order 
    # commonChars = sorted(commonChars) 
   
    # join characters without space to produce  
    # resultant string 
    # print(''.join(commonChars))

states = ['Alabama', 'Alaska', 'American Samoa', 'Arizona', 'Arkansas', 
          'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 
          'Florida', 'Georgia', 'Guam', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 
          'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 
          'Michigan', 'Minnesota', 'Minor Outlying Islands', 'Mississippi', 'Missouri', 
          'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 
          'New York', 'North Carolina', 'North Dakota', 'Northern Mariana Islands', 
          'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Puerto Rico', 'Rhode Island', 
          'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'U.S. Virgin Islands', 
          'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']

words = [line.rstrip('\n') for line in open("words.txt")]

# Longest word in the list
print(max(words, key=len))

# Sort words in decreasing order by the number of letters
words.sort(key = lambda s: len(s), reverse = True)

# Create a dictionary for each word from with the list with values representing the states without common letters
mackerels = {}

for w in words:
    key = w
    mackerels.setdefault(key, [])
    for s in states:
        s = s.lower()
        shared = common(w, s)
        
        if shared == 0:
            # print("State: " + s + " word: " + w)
            mackerels[key].append(s)

# Longest key (string) in dictionary
print(max(len(x) for x in mackerels))

# Key with the most values in dictionary
def word_with_most_states(db):
    maxcount = max(len(v) for v in db.values())
    return [k for k, v in db.items() if len(v) == maxcount]

word_with_most_states(mackerels)

# Key with the least (non-zero) values in dictionary
def word_with_one_state(db):
    # mincount = min(len(v) for v in db.values()) # mincount can be zero and we want exactly one
    return [k for k, v in db.items() if len(v) > 0]

matches = word_with_one_state(mackerels)

# Length of the longest word with only one matching state
maxmatch = max(len(x) for x in matches)
solution = [k for k, v in mackerels.items() if len(k) == maxmatch and len(v) == 1]

for n in solution:
    print(n + ' has no words in common with ' + str(mackerels[n]))

# Key with the no values in dictionary
def word_with_no_states(db):
    return [k for k, v in db.items() if len(v) == 0]

print('Do words with that have letters in common with all fifty states exist? ' + str(all(x==0 for x in mackerels.values())))
nonmatches = word_with_no_states(mackerels)

# Extra credit

moremackerels = {}

for s in states:
    s = s.lower()
    key = s
    moremackerels.setdefault(key, [])
    for w in words:
        shared = common(w, s)
        
        if shared == 0:
            # print("State: " + s + " Word: " + w)
            moremackerels[key].append(w)

# Longest key (string) in dictionary
print(max(len(x) for x in moremackerels))

# Key with the most values in dictionary
def state_with_most_words(db):
    maxcount = max(len(v) for v in db.values())
    return [k for k, v in db.items() if len(v) == maxcount]

morematches = state_with_most_words(moremackerels)
    

for m in morematches:
    print(m + ' has ' + len(moremackerels[m])' words that it does not share any matches with.')

print(morematches)