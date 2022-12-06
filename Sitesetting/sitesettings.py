import pprint
from Blog.blog_posts import auth_header_token
import requests
from assertpy import assert_that
from config import BASE_URI

def test_sitesettings_smtp():
    r = smtp_detail()
    pprint.pprint(id)
    assert_that(r.status_code).is_equal_to(200)


def get_smtp_id():
    id = smtp_detail().json()[0]['id']
    return id


def smtp_detail():
    smtp_URI = f'{BASE_URI}/sitesettings/smtp/'
    r = requests.get(smtp_URI)
    return r


def test_post_sitesettings_smtp():
    smtp_URI = f'{BASE_URI}/sitesettings/smtp/'
    data = {
        'email_host_user': 'user@gmail.com',
        'email_host_password': 'ktglwcqxrbtmyxzv',
        'email_port': 587
    }
    r = requests.post(smtp_URI, data=data)
    assert_that(r.status_code).is_equal_to(201)
    pprint.pprint(r.json())


def test_sitesetting_smtp_detail():
    id = get_smtp_id()
    detail_URI = f'{BASE_URI}/sitesettings/smtp-detail/{id}'
    r = requests.get(detail_URI)
    assert_that(r.status_code).is_equal_to(200)


def test_patch_sitesetting():
    id = get_smtp_id()
    patch_URI = f'{BASE_URI}/sitesettings/smtp-detail/{id}/'
    data = {
        'email_host_user': 'user123@gmail.com',
        'email_host_password': 'ktglwcqxrbtmyxzv',
        'email_port': 587
    }
    r = requests.patch(patch_URI, data=data)
    assert_that(r.status_code).is_equal_to(200)


def test_delete_sitesettings():
    id = get_smtp_id()
    delete_URI = f'{BASE_URI}/sitesettings/smtp-detail/{id}/'
    r = requests.delete(delete_URI)
    assert_that(r.status_code).is_equal_to(204)