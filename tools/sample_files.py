#!/usr/bin/env python3
import argparse
import os
import random
import re

def sample_file(f, lim, ignore_header = False):
    # assumes every line ends in a newline (inc. last line)
    if ignore_header:
        f.readline()
    lines = f.readlines()
    used = 0
    while len(lines) > 0:
        i = random.randrange(0, len(lines))
        line = lines[i]
        if used + len(line) > lim:
            break
        os.write(1, line)
        used += len(line)
        del lines[i]
    return used

def sample_files(files, lim, ignore_headers = False):
    for i,f in enumerate(files):
        lim -= sample_file(f, lim // (len(files) - i), ignore_headers)
    return lim

def read_byte_size(size_str):
    m = re.match('(\d+)(b|[kmg]b)?', size_str, re.IGNORECASE)
    count = int(m[1])
    suffix = m[2] or 'b'
    return count * 1000 ** ['b','kb','mb','gb'].index(suffix.lower())

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('size', type=read_byte_size)
    parser.add_argument('files', nargs='+', type=argparse.FileType('rb'))
    parser.add_argument('--ignore_headers', action='store_true')

    args = parser.parse_args()
    sample_files(args.files, args.size, args.ignore_headers)

if __name__ == '__main__':
    main()
