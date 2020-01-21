#!/usr/bin/env python3
import argparse
import os
import random
import re

def sample_file_lines(f, lim, ignore_header = False):
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

def sample_file_seek(f, lim, ignore_header = False):
    # does not select between all lines with equal probability
    if ignore_header:
        f.readline()
    start = f.tell()
    f.seek(0, 2)
    f_len = f.tell()

    if f_len == 0:
        return 0

    used = 0
    while 1:
        pos = random.randrange(start, f_len)
        f.seek(pos)
        # backtrack to last newline
        while pos > start and f.read(1) != b'\n':
            pos -= 1
            f.seek(pos)
        line = f.readline()
        if used + len(line) < lim:
            os.write(1, line)
            used += len(line)
        else:
            break

    return used

def sample_files(files, lim, sample_file, ignore_headers = False):
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
    parser.add_argument('--seek', action='store_true')

    args = parser.parse_args()
    sample_files(args.files, args.size, sample_file_seek if args.seek else sample_file_lines, args.ignore_headers)

if __name__ == '__main__':
    main()
