import pytest
import requests
from config import BASE_URI
import pprint
from assertpy.assertpy import assert_that
from Auth.auth import get_token_login


def test_blog_post_list():
    blog_list, r = blog_post_list()
    #pprint.pprint(blog_list)
    assert_that(r.status_code).is_equal_to(200)
    title = [blog_title for blog_title in blog_list['Results']]
    assert_that(title).is_not_empty()


def blog_post_list():
    BLOG_LIST_API = f'{BASE_URI}/blog/post-list/'
    r = requests.get(BLOG_LIST_API)
    blog_list = r.json()
    return blog_list, r


def test_creating_blog_post():
    r = creating_blog_post()
    #pprint.pprint(r.text)
    assert_that(r.status_code).is_equal_to(201)


def creating_blog_post():
    POST_URI = f'{BASE_URI}/blog/post-create/'
    body = {
        'title': 'New Title',
        'content': 'New Content of the blog ',
        'author': 'JohnVonNewmann'
    }
    headers = auth_header_token()
    r = requests.post(url=POST_URI, data=body, headers=headers)
    return r


def auth_header_token():
    headers = {
        'Authorization': f'JWT {get_token_login()}'
    }
    return headers


def test_blog_delete():
    created_blogs = creating_blog_post()
    slug = created_blogs.json()['slug']
    #pprint.pprint(slug)
    DELETE_URI = f'{BASE_URI}/blog/post-delete/{slug}/'
    r = requests.delete(url=DELETE_URI, headers=auth_header_token())
    assert_that(r.status_code).is_equal_to(204)


def test_blog_post_detail():
    slug = creating_blog_post().json()['slug']
    #pprint.pprint(slug)
    detail_URI = f'{BASE_URI}/blog/post-detail/{slug}/'
    r = requests.get(detail_URI)
    assert_that(r.status_code).is_not_none()


def test_blog_post_update():
    blog_post, _ = blog_post_list()
    slug = blog_post['Results'][0]['slug']
    #pprint.pprint(slug)
    update_URI = f'{BASE_URI}/blog/post-update/{slug}/'
    data = {
        'title': 'Updated Title',
        'content': 'Updated Content',
        'author': 'New Author'
    }
    r = requests.patch(url=update_URI, data=data, headers=auth_header_token())
    assert_that(r.status_code).is_equal_to(200)



