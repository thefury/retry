#!/usr/bin/env python

import sys
import time
import getopt
import subprocess 

DEFAULT_INTERVAL=60
DEFAULT_DURATION=3600

def print_help():
    print "usage: retry.py [options] -- command"

def parse_args(argv):
    interval = DEFAULT_INTERVAL
    duration = DEFAULT_DURATION

    try:
        opts, args = getopt.getopt(argv, "hi:d:", ["interval=","duration="])
    except getopt.GetoptError:
        print_help()
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print_help()
            sys.exit()
        elif opt in ['-i', '--interval']:
            interval = arg
        elif opt in ['-d', '--duration']:
            duration = arg

    return int(interval), int(duration), args


def main():
    interval, duration, command = parse_args(sys.argv[1:])
    success = False

    while (not success) or duration > 0: 
        returncode = subprocess.call(command)
        
        if returncode == 0:
            break

        time.sleep(interval)
        duration -= interval

if __name__ == "__main__":
    main()

