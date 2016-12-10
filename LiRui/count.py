# coding=UTF-8

import sys
import re
import string
from collections import defaultdict

WORD_PATTERN = re.compile(r'[0-9a-zA-Z]+')


def compare_tuple(a, b):
    word1, count1 = a
    word2, count2 = b
    c = cmp(count1, count2)
    if c != 0:
        # reversed
        return -c
    c = cmp(word1, word2)
    return c


def find_interval(items, pos, length):
    count = items[pos][0]
    pos += 1
    while pos < length:
        if items[pos][0] != count:
            break
        else:
            pos += 1

    return pos - 1


def count_words(filename):
    with open(filename, 'r') as f:
        count_dict = defaultdict(lambda : 0)
        for line in f:
            for word in WORD_PATTERN.findall(line):
                count_dict[word] += 1

    # custom sort cmp function, simple but slower
    # return sorted(count_dict.items(), cmp=compare_tuple)

    # custom return, complex but faster
    items = map(lambda w: (w[1], w[0]), count_dict.items())
    items = sorted(items, reverse=True)
    begin = 0
    length = len(items)
    while begin < length:
        end = find_interval(items, begin, length)
        pos = end
        while pos >= begin:
            count, word = items[pos]
            yield word, count
            pos -= 1
        begin = end + 1


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('USAGE: {0} <FILENAME>'.format(sys.argv[0]))
        exit(1)

    for word, count in count_words(sys.argv[1]):
        print('{0}: {1}'.format(word, count))
