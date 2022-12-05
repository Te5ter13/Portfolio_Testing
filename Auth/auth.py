import pprint

import requests
from assertpy import assert_that
from config import BASE_URI


def test_auth_login():
    r = auth_login()
    assert_that(r.status_code).is_equal_to(200)


def auth_login():
    login_URI = f'{BASE_URI}/auth/login/'
    data = {
        'username': 'admin1',
        'password': 'admin1'
    }
    r = requests.post(login_URI, data=data)
    return r


def get_token_login():
    return (auth_login().json())['access']


def get_refresh_login():
    return (auth_login().json())['refresh']


def test_auth_email_verify():
    verify_URI = f'{BASE_URI}/auth/email-verify/'
    #pprint.pprint(token)
    headers = {
        'Authorization': 'JWT '+get_refresh_login()
    }
    r = requests.get(verify_URI, headers=headers)
    assert_that(r.status_code).is_equal_to(200)


def test_auth_logout():
    logout_URI = f'{BASE_URI}/auth/logout/'
    headers = {
        'Authorization': f'JWT {get_token_login()}'
    }
    data = {
        'refresh': get_refresh_login()
    }
    pprint.pprint(data)
    pprint.pprint(headers)
    r = requests.post(url=logout_URI, headers=headers, data=data)
    assert_that(r.status_code).is_equal_to(200)


def test_auth_register():
    register_URI = f'{BASE_URI}/auth/register/'
    data = {
        'email': 'email@gmail.com',
        'username': 'emailMan',
        'password': 'Password'
    }
    r = requests.post(url=register_URI, data=data)
    assert_that(r.status_code).is_equal_to(201)