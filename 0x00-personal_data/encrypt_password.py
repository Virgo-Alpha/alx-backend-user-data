#!/usr/bin/env python3
"""
A hash_password function to return a hashed password
"""
import bcrypt
from bcrypt import hashpw


def hash_password(password: str) -> bytes:
    """
    Returns a hashed password
    Args:
        password (str): password to be hashed
    """
    b = password.encode()
    hashed = hashpw(b, bcrypt.gensalt())
    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Checks whether a password is valid or not
    Args:
        hashed_password (bytes): hashed password
        password (str): password in string
    Return:
        boolean
    """
    return bcrypt.checkpw(password.encode(), hashed_password)
