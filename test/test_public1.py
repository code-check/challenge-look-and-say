import glob, os, shlex, subprocess, sys

app = os.environ['APP_COMMAND']

def main(N):
    return N * (4 ** (N-1))

def check(prob):
    assert main(int(prob)) == int(subprocess.check_output(shlex.split(app) + [prob]))

def random_test():
    '''Random test'''
    for prob in range(1,31):
        yield check, '{}'.format(prob)