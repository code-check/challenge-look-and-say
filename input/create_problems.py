#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random, sys

def __create_problem():
    segs = []
    for j in xrange(random.randint(1, 10000)):
        seg = [random.randrange(-10000, 10000), random.randint(-10000, 10000)]
        segs.append(seg if seg[0] <= seg[1] else seg[::-1])
    return segs

if __name__ == '__main__':
    for i in xrange(int(sys.argv[1])):
        with open('test_{0:04d}.txt'.format(i), 'w') as fp:
            probs = __create_problem()
            fp.write('{0}\n'.format(len(probs)))
            fp.write('\n'.join(['{0} {1}'.format(p[0], p[1]) for p in probs]))
