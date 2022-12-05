import pprint
import json
import requests
from assertpy import assert_that
from config import BASE_URI
from Blog.blog_posts import auth_header_token

def test_question_list():
    r = question_list()
    pprint.pprint(r.json())
    assert_that(r.status_code).is_equal_to(200)


def question_list():
    list_URI = f'{BASE_URI}/cms/question-list/'
    r = requests.get(list_URI)
    return r

def id_of_question_list():
    return question_list().json()[0]['id']

def test_question_update():
    id = id_of_question_list()
    update_URI = f'{BASE_URI}/cms/question-update/{id}/'
    data = {
        'question': 'This is changed question??'
    }
    r = requests.patch(update_URI, data=data, headers=auth_header_token())
    assert_that(r.status_code).is_equal_to(200)


def test_question_create():
    create_URL = f'{BASE_URI}/cms/question-create/'
    data = {
        'question': 'This is new question?'
    }
    r = requests.post(create_URL, data=data, headers=auth_header_token())
    assert_that(r.status_code).is_equal_to(201)
    #pprint.pprint(question_list().json())

def test_question_delete():
    id = id_of_question_list()
    delete_URL = f'{BASE_URI}/cms/question-delete/{id}/'
    r = requests.delete(delete_URL, headers=auth_header_token())
    assert_that(r.status_code).is_equal_to(204)




