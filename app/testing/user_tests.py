import pytest
import sys
sys.path.insert(0, '../../db/')

import os
from model.user import User
from tinydb import TinyDB

#NOTE we remove loginInfo.json (created locally in testing directory) after each run to ensure test reproducability in future runs

def test_verify_constructor():
    user = User("TEST_USER", "password")
    assert user.name == "TEST_USER"
    assert user.password == "password"

def test_add_user():
    db = TinyDB("loginInfo.json")
    user = User("TEST_USER", "password")
    user.add_user()
    assert db.all()[0]['username'] == "TEST_USER"
    assert db.all()[0]['status'] == "False"
    os.remove("loginInfo.json")

def test_verify_login():
    db = TinyDB("loginInfo.json")
    user = User("TEST_USER", "password")
    user.add_user()
    user.verify_login()
    assert db.all()[0]['status'] == "True"
    os.remove("loginInfo.json")

def test_logout():
    db = TinyDB("loginInfo.json")
    user = User("TEST_USER", "password")
    user.add_user()
    user.verify_login()
    user.logout()
    assert db.all()[0]['status'] == "False"
    os.remove("loginInfo.json")
