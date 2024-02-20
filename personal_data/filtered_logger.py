#!/usr/bin/env python3
"""
function called filter_datum that returns the log message obfuscated
"""


import logging
import re
from typing import List

PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        returns the log message obfuscated from the record
        """
        filter_message = filter_datum(
            self.fields, self.REDACTION, record.msg, self.SEPARATOR)
        record.msg = filter_message
        return super().format(record)


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """
    Arguments:
        fields: a list of strings representing all fields to obfuscate
        redaction: a string representing by what the field will be obfuscated
        message: a string representing the log line
        separator: a string representing by which character is separating
        all fields in the log line (message)
    """
    for field in fields:
        message = re.sub(field + "=.*?" + separator,
                         field + "=" + redaction + separator, message)
    return message


def get_logger() -> logging.Logger:
    """
    get_logger: function that takes no arguments and
        returns a logging.Logger object
    """
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False

    formater = RedactingFormatter(PII_FIELDS)
    streamHandler = logging.StreamHandler()
    streamHandler.setFormatter(formater)

    logger.addHandler(streamHandler)
    return logger
