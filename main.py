import sys

def main(N):
    # BEGIN_CHALLENGE
    print N * (4 ** (N-1))
    # END_CHALLENGE

main(int(sys.argv[1]))
