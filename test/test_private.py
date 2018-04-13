import glob, os, shlex, subprocess, sys
from operator import itemgetter

app = os.environ['APP_COMMAND']

def main(filename):
    segments = []
    with open(filename, 'r') as fp:
        fp.readline()
        segments = [[int(p) for p in s.strip().split(' ')] for s in fp.readlines()]
    segments.sort(key=itemgetter(0))
    ret = []
    for seg in segments:
        for r in ret:
            if (seg[0] <= r[1]) and (seg[1] >= r[1]):
                r[1] = seg[1]
                break
            elif (seg[0] <= r[0]) and (seg[1] >= r[0]):
                r[0] = seg[0]
                break
        else:
            ret.append(list(seg))
    return max(map(lambda r: r[1] - r[0], ret))

def check(prob):
    assert main(prob) == int(subprocess.check_output(shlex.split(app) + [prob]))

def random_test():
    '''Random test'''
    for prob in glob.glob('./input/test_*.txt'):
        yield check, prob

def test_bridge():
    '''Bridge test'''
    prob = './input/bridge.txt'
    assert main(prob) == int(subprocess.check_output(shlex.split(app) + [prob]))
