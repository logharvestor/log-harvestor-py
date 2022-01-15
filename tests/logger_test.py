import pytest

from forwarder.logger import Logger
from forwarder import API_URL


valid_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImZvcndhcmRlciJ9.eyJfaWQiOiI2MTI4OTIwYjNjMzQyNTAwMjFkZGQyMTciLCJpYXQiOjE2MzAwNDg3ODN9.sb8lfpp01CC-y0T9Z5XiIEdy-JBeDHSBD8Gd05bZYaQ"
valid_token_local = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImZvcndhcmRlciJ9.eyJfaWQiOiI2MDk5Mzg5Mjg4MWQ0MzAwMjkxNzY2MGUiLCJpYXQiOjE2Mjc3MzAzOTZ9.uEY-6s8hK8HX6qy-5Su8Esb-iRXewc9hXYhRLIlALCo"
invalid_token = "123ABC"
valid_api_url = API_URL
valid_api_url_local = "http://localhost:3001/api/log"
invalid_api_url = "tcp://localhost:3001"


"""
Utility Function  - Send Log
"""


def send_log(type, msg, url=valid_api_url, token=valid_token, **kwargs):
    lh = Logger(token=token, api_url=url)
    success, res = lh.log(type, msg)
    return success, res


def test_connection_valid():
    lh = Logger(token=valid_token, api_url=valid_api_url)
    success, res = lh.test_conn()
    print(res.content)
    assert success == True


def test_connection_invalid():
    lh = Logger(token=invalid_token, api_url=valid_api_url)
    success, res = lh.test_conn()
    print(res.content)
    assert success == False
    assert res.status_code in [401, 403]


def test_log_msg_string():
    """Msg should allow a single string"""
    success, res = send_log('test', msg="Hello World!")
    print(res.content)
    assert success == True


def test_log_msg_number():
    """Msg should allow a single number"""
    success, res = send_log('test', msg=123)
    print(res.content)
    assert success == True


def test_log_msg_object():
    """Msg should allow a single object"""
    success, res = send_log('test', msg={"a": 123, "b": "456", "c": "hello"})
    print(res.content)
    assert success == True


def test_log_msg_object_nested():
    """Msg should allow a nested object"""
    success, res = send_log('test', msg={"a": {"b": "123"}})
    print(res.content)
    assert success == True


def test_log_msg_object_nested_mixed():
    """Msg should allow a nested mix"""
    success, res = send_log('test', msg={"a": 123, "b": {"c": "123", "d": {}}})
    print(res.content)
    assert success == True


def test_log_msg_array_string():
    """Msg should allow array of strings"""
    success, res = send_log(
        'test', msg=["hello", "mars", "goodbye", "world"])
    print(res.content)
    assert success == True


def test_log_msg_array_number():
    """Msg should allow array of numbers"""
    success, res = send_log('test', msg=[1, 2, 34, 567, 8, 90])
    print(res.content)
    assert success == True


def test_log_msg_array_objects():
    """Msg should allow array of objects"""
    success, res = send_log('test', msg=[{"question": "Hello?", "answer": "World!"}, {
                            "question": "So long?", "answer": "Thanks for all the fish!"}])
    print(res.content)
    assert success == True


def test_log_msg_array_mixed():
    """Msg should allow array of mixed"""
    success, res = send_log('test', msg=[123, "abc", [1, 2, 3], {"question": "Hello?", "answer": "World!"}, {
                            "question": "So long?", "answer": "Thanks for all the fish!"}])
    print(res.content)
    assert success == True

def test_log_msg_empty():
    """Msg should allow a an empty value"""
    success, res = send_log('test', msg={})
    print(res.content)
    assert success == True

def test_log_msg_null_fail():
    """Msg should not allow a null value"""
    success, res = send_log('test', msg=None)
    print(res.status_code)
    print(res.content)
    assert res.status_code in [400, 404]
    assert res.status_code.__str__()[:2] != "50"
    assert success == False


