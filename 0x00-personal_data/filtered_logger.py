#!/usr/bin/env python3
"""
Task 3. Connect to secure database

Get a secure connection to a database
"""

from typing import List
import re
import logging
from mysql.connector import connection
from os import environ

PII_FIELDS = ('name', 'email', 'password', 'ssn', 'phone')


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


def get_logger() -> logging.Logger:
    """get_logger

    """
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(stream_handler)
    return logger


def get_db() -> connection.MySQLConnection:
    """get_db

    Connects to the secure database and returns the connector.

    Return:
        (MySQLConnection): The database connector
    """
    username = environ.get('PERSONAL_DATA_DB_USERNAME', 'root')
    password = environ.get('PERSONAL_DATA_DB_PASSWORD', '')
    host = environ.get('PERSONAL_DATA_DB_HOST', 'localhost')
    db_name = environ.get('PERSONAL_DATA_DB_NAME')

    connector = connection.MySQLConnection(
        user=username,
        password=password,
        host=host,
        database=db_name)
    return connector


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
                            super(RedactingFormatter, self).format(record),
                            self.SEPARATOR)
