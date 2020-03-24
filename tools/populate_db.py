#!/usr/bin/env python3
from load_dataframe import *

from sqlalchemy import create_engine

cols = ['sample_name'] + cdr3_v_j

def populate_db(f, tablename, engine):
    load_dataframe(f)[cols].to_sql(tablename, engine, if_exists='append')

import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', type=argparse.FileType('r'))
    parser.add_argument('tablename')
    parser.add_argument('database')

    args = parser.parse_args()
    engine = create_engine(args.database)
    populate_db(args.data_file, args.tablename, engine)

if __name__ == '__main__':
    main()
