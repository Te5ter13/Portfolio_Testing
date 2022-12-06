import requests
import pprint
from assertpy import assert_that
from config import BASE_URI
from Blog.blog_posts import get_token_login

def test_aboutus_list():
    r = list_aboutus()
    assert_that(r.status_code).is_equal_to(200)


def list_aboutus():
    list_URI = f'{BASE_URI}/cms/aboutus-list/'
    r = requests.get(list_URI)
    return r


def test_about_us_delete():
    id = id_of_aboutus()
    #pprint.pprint(id)
    delete_URI = f'{BASE_URI}/cms/aboutus-delete/{id}/'
    headers = {
        'Authorization': f'JWT {get_token_login()}'
    }
    r = requests.delete(delete_URI, headers=headers)
    assert_that(r.status_code).is_equal_to(204)


def id_of_aboutus():
    about_us = list_aboutus().json()
    id = about_us[0]['id']
    return id


def test_aboutus_create():
    create_URI = f'{BASE_URI}/cms/aboutus-create/'
    data = {
        'content': 'This is my first content'
    }
    headers = {

    }
    r = requests.post(create_URI, data=data, headers=headers)
    assert_that(r.status_code).is_equal_to(201)


def test_aboutus_detail():
    about_id = id_of_aboutus()
    headers = {
        'Authorization': f'JWT {get_token_login()}'
    }
    detail_URI = f'{BASE_URI}/cms/aboutus-detail/{about_id}/'
    r = requests.get(detail_URI, headers=headers)
    #pprint.pprint(r.json())
    assert_that(r.status_code).is_equal_to(200)


def test_aboutus_update():
    aboutus_id = id_of_aboutus()
    updated_URI = f'{BASE_URI}/cms/aboutus-update/{aboutus_id}/'
    headers = {
        'Authorization': f'JWT {get_token_login()}'
    }
    data = {
        'content': 'Here we see the changed content'
    }
    r = requests.patch(updated_URI, data=data, headers=headers)
    assert_that(r.status_code).is_equal_to(200)
    #pprint.pprint(list_aboutus().json())

