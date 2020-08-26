#!/usr/bin/python3

def PatternCount(text, pattern):
    diff = len(text) - len(pattern)
    count = 0
    for i in range(diff+1):
        if(text[i:i+len(pattern)] == pattern):
            count += 1
    return count


print(PatternCount("GCGCG", "GCG"))
