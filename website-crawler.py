#!/usr/bin/env python

import requests

target_url = "example.com"

with open("/username/Downloads/common.txt", "r") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        test_url = target_url + "/" + word
        response = request(test_url)
        if response:
            print("[+] Discovered URl --> " + test_url)
