#! /usr/bin/env python
"""
Extract Syslog Message Matching Pattern
"""
import argparse
import re
import os.path
import json
import pandas as pd
import paramiko
from scp import SCPClient

__author__ = "Charles Stolz"

PATTERN = r"^([A-z]{3}\s\d{2}\s\d{2}:\d{2}:\d{2}\stan-[A-z0-9]{24}\sTetration\sAlert\[\d+\]:\s\[[A-Z]+\]\s)({.+})$"
REGEX = re.compile(PATTERN, re.MULTILINE)


def get_syslog_messages(server: str, port: str, user_name: str, password: str) -> None:
    """
    retrieve syslog messages from server
    """
    ssh = create_ssh_client(server, port, user_name, password)
    scp = SCPClient(ssh.get_transport())
    scp.get(r"/var/log/syslog", r"./syslog")


def create_ssh_client(server: str, port: str, user: str, password: str) -> object:
    """
    Create ssh client to enable scp of syslog file form server
    """
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server, port, user, password)
    return client


def create_csv():
    """
    TODO
    """


if __name__ == "__main__":
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument(
        "--server", type=str, default="172.16.101.195", help="Syslog Server"
    )
    ARGS = PARSER.parse_args()

    SERVER = ARGS.server

    # check if server ssh credentials exist if not use test data
    if os.path.isfile("./creds_file.json"):
        # Load Syslog Credentials
        with open("creds_file.json", "r") as fh:
            creds_dict = json.loads(fh.read())

        # Retreive messages from Syslog Server using scp
        get_syslog_messages(
            SERVER, "22", creds_dict["user_name"], creds_dict["password"]
        )

    # Load Syslog Messages
    with open("syslog", "r") as fh:
        s = fh.read()

    # Printing for debugging
    matches = re.finditer(REGEX, s)
    for match_num, match in enumerate(matches, start=1):
        print(
            f"Match {match_num} was found at {match.start()}-{match.end()}: {match.group()}"
        )
        for group_num in range(0, len(match.groups())):
            print(
                "Group {group_num} found at {start}-{end}: {group}".format(
                    group_num=group_num + 1,
                    start=match.start(group_num),
                    end=match.end(group_num),
                    group=match.group(group_num),
                )
            )
