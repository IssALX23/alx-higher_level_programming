#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    set12 = []
    found = []

    for word1 in set_1:
        set12.append(word1)
    for word2 in set_2:
        set12.append(word2)

    for word in set12:
        if set12.count(word) == 1:
            found.append(word)

    return found
