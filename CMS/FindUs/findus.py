import pprint
import requests
from assertpy import assert_that
from config import BASE_URI
from Blog.blog_posts import auth_header_token

def test_cms_find_us_list():
    r = find_us_listing()
    #pprint.pprint(r.json())
    assert_that(r.status_code).is_equal_to(200)


def find_us_listing():
    list_URI = f'{BASE_URI}/cms/find-us-list/'
    r = requests.get(list_URI)
    return r


def test_find_us_delete():
    id = find_us_id()
    delete_URI = f'{BASE_URI}/cms/find-us-delete/{id}/'
    r = requests.delete(delete_URI, headers=auth_header_token())
    assert_that(r.status_code).is_equal_to(204)


def test_find_us_create():
    create_URI = f'{BASE_URI}/cms/find-us-create/'
    r = requests.post(create_URI, headers=auth_header_token())
    assert_that(r.status_code).is_equal_to(201)


def find_us_id():
    id = (find_us_listing().json())[0]['id']
    return id


def test_find_us_detail():
    id = find_us_id()
    detail_URI = f'{BASE_URI}/cms/find-us-detail/{id}'
    r = requests.get(detail_URI, headers=auth_header_token())
    #pprint.pprint(r.json())
    assert_that(r.status_code).is_equal_to(200)


def test_find_us_update():
    id = find_us_id()
    update_URI = f'{BASE_URI}/cms/find-us-update/{id}/'
    data = {
        'facebook': 'https://www.facebook.com',
        'twitter': 'https://www.twitter.com',
        'linkedin': 'https://www.linkedin.com'
    }
    r = requests.patch(url=update_URI, data=data, headers=auth_header_token())
    assert_that(r.status_code).is_equal_to(200)




