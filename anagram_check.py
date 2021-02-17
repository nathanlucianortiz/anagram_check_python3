#!/usr/bin/env python3
from collections import Counter

def anagram_check(w1, w2):

    if(Counter(w1) == Counter(w2)):
        print("The words are anagrams.")
    else:
        print("The words are not anagrams.")

# test
w1 = "star"
w2 = "rats"
anagram_check(w1, w2)
