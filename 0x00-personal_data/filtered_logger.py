#!/usr/bin/env python3
"""
Task 0. Regex-ing

Filter the data & get them obfuscated.
"""

from typing import List
import re


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
