#!/bin/bash
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-k", "--key")
parser.add_argument("-m", "--message")
parser.add_argument("-e", "--encrypted")


def encrypt(raw_message, key):
    key = str(key * int(len(raw_message) / len(key) + 1))[
        : len(raw_message)
        ]
    encrypted = ""
    for i in range(len(raw_message)):
        result = (ord(raw_message[i]) + ord(key[i])) % 1_114_112
        encrypted += chr(result)
    return encrypted


def decrypt(encrypted_message, key):
    key = str(key * int(len(encrypted_message) / len(key) + 1))[
        : len(encrypted_message)
    ]
    dencrypted = ""
    for i in range(len(encrypted_message)):
        result = (ord(encrypted_message[i]) - ord(key[i])) % 1_114_112
        dencrypted += chr(result)
    return dencrypted


args = parser.parse_args()

message = None
key = None
encrypted = None

for arg in args._get_kwargs():
    if arg[0] == "message":
        message = arg[1]
    if arg[0] == "key":
        key = arg[1]
    if arg[0] == "encrypted":
        encrypted = arg[1]


def main():
    if not bool(key):
        print("Use --key")
        return
    if bool(message) == bool(encrypted):
        print("Use either --message or --encrypted")
        return
    if bool(message) and bool(key):
        print(encrypt(message, key))
        return
    if bool(encrypted) and bool(key):
        print(decrypt(encrypted, key))
        return
    parser.print_help()


main()
