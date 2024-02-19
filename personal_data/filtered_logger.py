#!/usr/bin/env python3
"""
function called filter_datum that returns the log message obfuscated
"""


import re


def filter_datum(fields, redaction, message, separator):
    for field in fields:
        message = re.sub(f"{field}=[^;]*", f"{field}={redaction}", message)
    return message
