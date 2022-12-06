import pprint
import requests
from config import BASE_URI
from assertpy import assert_that
from Blog.blog_posts import get_token_login
from CMS.Questions.question import id_of_question_list
def test_answer_list():
    r = answer_list()
    pprint.pprint(id_of_answer())
    assert_that(r.status_code).is_equal_to(200)


def answer_list():
    list_URI = f'{BASE_URI}/cms/answer-list/'
    r = requests.get(list_URI)
    return r


def test_answer_create():
    create_URI = f'{BASE_URI}/cms/answer-create/'
    headers = {
        'Authorization': f'JWT {get_token_login()}'
    }
    data = {
        'question': {id_of_question_list()},
        'answer': 'Not your concern'
    }

    r = requests.post(create_URI, data=data, headers=headers)
    #pprint.pprint(r.json())
    assert_that(r.status_code).is_equal_to(201)


def test_answer_detail():
    id = id_of_answer()
    #pprint.pprint(id)
    detail_URI = f'{BASE_URI}/cms/answer-detail/{id}/'
    r = requests.get(detail_URI)
    assert_that(r.status_code).is_equal_to(200)
    #pprint.pprint(r.json())


def id_of_answer():
    id = (answer_list().json())[0]['id']
    return id


def test_answer_delete():
    id = (answer_list().json())[1]['id']
    delete_URI = f'{BASE_URI}/cms/answer-delete/{id}/'
    r = requests.delete(delete_URI)
    assert_that(r.status_code).is_equal_to(204)
    #pprint.pprint(answer_list().json())


def test_answer_update():
    id = id_of_answer()
    update_URI = f'{BASE_URI}/cms/answer-update/{id}/'
    data = {
        "answer": "Next One"
        }
    r = requests.patch(update_URI, data=data)
    assert_that(r.status_code).is_equal_to(200)
    #pprint.pprint(answer_list().json())