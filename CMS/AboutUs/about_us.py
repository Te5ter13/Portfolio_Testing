import requests
import pprint
from assertpy import assert_that
from config import BASE_URI


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
        'Authorization': 'JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjcwMjI4MTQ5LCJpYXQiOjE2NzAxNDE3NDksImp0aSI6ImI1ZWUzMzdlMDJlZDRjMGVhZjdhNTliOGEzYTdlYTlkIiwidXNlcl9pZCI6OSwidXNlcm5hbWUiOiJhZG1pbjEiLCJlbWFpbCI6ImFkbWluMUBnbWFpbC5jb20ifQ.caZGOXNl7ZWrJ7YnArJQj36lqAvEMsUL3JLutHWi83E'
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
        'Authorization': 'JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjcwMjI2ODEwLCJpYXQiOjE2NzAxNDA0MTAsImp0aSI6IjUwMDhkNjBiMzdiZDRjOWRhOTE3M2E3NGIwZDk4NDc4IiwidXNlcl9pZCI6OSwidXNlcm5hbWUiOiJhZG1pbjEiLCJlbWFpbCI6ImFkbWluMUBnbWFpbC5jb20ifQ.zOOpNLFnWGnKLgs4JBM9Dc_SvjblRqectlXwf4Gt7NU'
    }
    r = requests.post(create_URI, data=data, headers=headers)
    assert_that(r.status_code).is_equal_to(201)


def test_aboutus_detail():
    about_id = id_of_aboutus()
    headers = {
        'Authorization': 'JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjcwMjI4MTQ5LCJpYXQiOjE2NzAxNDE3NDksImp0aSI6ImI1ZWUzMzdlMDJlZDRjMGVhZjdhNTliOGEzYTdlYTlkIiwidXNlcl9pZCI6OSwidXNlcm5hbWUiOiJhZG1pbjEiLCJlbWFpbCI6ImFkbWluMUBnbWFpbC5jb20ifQ.caZGOXNl7ZWrJ7YnArJQj36lqAvEMsUL3JLutHWi83E'
    }
    detail_URI = f'{BASE_URI}/cms/aboutus-detail/{about_id}/'
    r = requests.get(detail_URI, headers=headers)
    #pprint.pprint(r.json())
    assert_that(r.status_code).is_equal_to(200)


def test_aboutus_update():
    aboutus_id = id_of_aboutus()
    updated_URI = f'{BASE_URI}/cms/aboutus-update/{aboutus_id}/'
    headers = {
        'Authorization': 'JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjcwMjI4MTQ5LCJpYXQiOjE2NzAxNDE3NDksImp0aSI6ImI1ZWUzMzdlMDJlZDRjMGVhZjdhNTliOGEzYTdlYTlkIiwidXNlcl9pZCI6OSwidXNlcm5hbWUiOiJhZG1pbjEiLCJlbWFpbCI6ImFkbWluMUBnbWFpbC5jb20ifQ.caZGOXNl7ZWrJ7YnArJQj36lqAvEMsUL3JLutHWi83E'
    }
    data = {
        'content': 'Here we see the changed content'
    }
    r = requests.patch(updated_URI, data=data, headers=headers)
    assert_that(r.status_code).is_equal_to(200)
    #pprint.pprint(list_aboutus().json())

