#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    maxi = max(a_dictionary.values())
    maxK = None
    for key, value in a_dictionary.items():
        if value == maxi:
            maxK = key
    return maxK
