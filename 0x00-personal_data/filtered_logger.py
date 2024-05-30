#!/usr/bin/env python3
"""
Task 1. Log formatter

Implement class RedactingFormatter
"""

from typing import List
import re
import logging


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """filter_dataum

    This method takes in a list of fields and returns the log message
    obfuscated.

    Arguments:
        fields (List[str]): Representing all fields to obfuscate
        redaction (str): A string by what the field will be obfuscated
        message (str): A string representing the log line
        separator (str): A string representing by which character is
                         separating all fields in the log line (message)

    Return:
        (str): The message after getting obfuscated.
    """
    temp_message = message
    for field in fields:
        temp_message = re.sub(field + '=.*?' + separator,
                              field + '=' + redaction + separator,
                              temp_message)
    return temp_message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """__init__
        
        Constructor of RedactingFormatter
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """format
        
        The formater of the class
        """
        return filter_datum(self.fields, self.REDACTION,
                            super(RedactingFormatter, self).fromat(record),
                            self.SEPARATOR)
