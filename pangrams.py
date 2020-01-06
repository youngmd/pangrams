#!/usr/bin/env python
import os, sys

dict_file = sys.argv[1]


# Find all words that contain 7 unique characters (no S)

def get_unique(word):
    unique = []
    for char in word[::]:
        if char not in unique:
            unique.append(char)
    return sorted(unique)


def readWords(dict_file):
    word_list = []
    with open(dict_file) as fp:
        line = fp.readline()
        while line:
            word = line.strip()
            if('s') not in word and len(word) > 3:
                word_list.append(word)
            line = fp.readline()
    return word_list

def slist2str(slist):
    string = ''
    for s in slist:
        string += s
    return string

def getCandidateSets(word_list):
    candidate_sets = []
    for word in word_list:
        if len(word) < 7:
            continue
        else:
            unique = get_unique(word)
            uniq_str = slist2str(unique)
            if len(uniq_str) == 7 and uniq_str not in candidate_sets:
                candidate_sets.append(uniq_str)
    return candidate_sets

def match(word, candidate):
    for w in word:
        if w not in candidate:
            return False
    return True

def findMembers(word_list, candidate):
    members = []
    for word in word_list:
        if match(word, candidate):
            members.append(word)
    return members

def isPangram(cl, word):
    for c in cl:
        if c not in word:
            return False
    return True

def score_set(cl, wl):
    best_score = 0
    best_center = ''
    best_list = []
    for c in cl:
        cscore = 0
        pangram_cnt = 0
        word_list = []
        for w in wl:
            if c not in w:
                continue
            word_list.append(w)
            wscore = len(w)
            if wscore > 6 and isPangram(cl, w):
                wscore += 7
                pangram_cnt += 1
            cscore += wscore

        if cscore > best_score and pangram_cnt:
            best_score = cscore
            best_center = c
            best_list = word_list
    return (best_center, best_score, pangram_cnt, best_list)

word_list = readWords(dict_file)
candidate_sets = getCandidateSets(word_list)

master_list = {}

for c in candidate_sets:
    members = findMembers(word_list, c)
    if len(members) > 500:
        print('New large set found: %s' % c)
        master_list[str(c)] = members

print("Number of large sets: %s" % len(master_list))
print("Testing and scoring possible centers in master_lists")

best_set = ''
best_result = None
best_score = 0

for cand, words in master_list.iteritems():
    result = score_set(cand, words)
    if result[1] > best_score:
        best_set = cand
        best_result = result
        best_score = result[1]

print("")
print("###########################")
print("")
print(best_set, best_result[0], best_score, best_result[2], len(best_result[3]))
print("")
print("###########################")
print("")
print(best_result[3])


