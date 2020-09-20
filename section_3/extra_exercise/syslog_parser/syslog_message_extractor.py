#! /usr/bin/env python
"""
Extract Syslog Message Matching Pattern
"""
import argparse
import json

import pandas as pd

__author__ = 'cstolz'


def get_syslog_messages(url: str) -> str:
    """
    retrieve syslog messages from server
    """
    return


if __name__ == '__main__':
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument('--server', type=str,
                        default='172.16.101.195',
                        help='Syslog Server')

    ARGS = PARSER.parse_args()

    with open(f'syslog', 'r') as fh:
        s = fh.read()
    print(s)