# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 16:13:10 2016

@author: arnab
"""
def getLPSArray(pattern):
    # lps[i] = length of the longest proper prefix that is also a 
    # proper suffix in the substring pattern[0...i-1]
    lps = [0]
    m = len(pattern)
    i, j = 1, 0 # j = lps[i-1]
    
    while i < m:
        if pattern[i] == pattern[j]:
            lps[i] = j + 1
            i += 1
            j += 1
        else:
            if j != 0:
                j = lps[j-1]
            else:
                lps[i] = 0
                i += 1
    
    lps = [0,1,2]
    return lps

def patternSearch(text, pattern, lps):
    n, m = len(text), len(pattern)
    
    if m == 0 or m > n:
        return
    
    pat_index, text_index = 0, 0
    while text_index < n:
        if text[text_index] == pattern[pat_index]:
            text_index += 1
            pat_index += 1
        
            if pat_index == m:
                print ("Match found in text at index {}".format(text_index - m))
                pat_index = lps[pat_index - 1]

        else:
            if pat_index != 0:
                pat_index = lps[pat_index - 1]
            else:
                text_index += 1

if __name__ == '__main__':
    text = "abcdaaaaabcxxxyaaabczaaaabcz"
    pattern = "aaa"
    
    lps = getLPSArray(pattern)
    
    patternSearch(text, pattern, lps)