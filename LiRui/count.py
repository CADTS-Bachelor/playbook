# coding=UTF-8

import sys
import re
import string
from collections import defaultdict

NOT_WORD = re.compile(r'\W+')


def count_words(filename):
    with open(filename, 'r') as f:
        count_dict = defaultdict(lambda : 0)
        for line in f:
            words = filter(lambda w: len(w), map(lambda w: NOT_WORD.sub('', w), line.split()))
            for word in words:
                count_dict[word] += 1

    result = map(lambda wc: (wc[1], wc[0]), count_dict.items())
    return reversed(sorted(result))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('USAGE: {0} <FILENAME>'.format(sys.argv[0]))
        exit(1)

    for count, word in count_words(sys.argv[1]):
        print('{0}: {1}'.format(word, count))
