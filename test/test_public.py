import os, shlex, subprocess, sys

app = os.environ['APP_COMMAND']

def test_sample1():
    '''Test sample 1'''
    assert(8 == int(subprocess.check_output(shlex.split(app) + ['2'])))

def test_sample2():
    '''Test sample 2'''
    assert(8646911284551352320 == int(subprocess.check_output(shlex.split(app) + ['30'])))