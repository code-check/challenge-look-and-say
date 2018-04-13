import os, shlex, subprocess, sys

app = os.environ['APP_COMMAND']

def test_sample1():
    '''Test sample 1'''
    assert(1 == int(subprocess.check_output(shlex.split(app) + ['./input/sample1.txt'])))

def test_sample2():
    '''Test sample 2'''
    assert(3 == int(subprocess.check_output(shlex.split(app) + ['./input/sample2.txt'])))

def test_sample3():
    '''Test sample 3'''
    assert(20000 == int(subprocess.check_output(shlex.split(app) + ['./input/sample3.txt'])))
