#!/usr/bin/python3

"""Implements the user's model"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    Inherits from the BaseModel class and add user's functionalities

    Args:
        email (str): email of the user
        password (str): password of the user
        first_name (str): first name of the user
        last_name (str): last name of the user
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
