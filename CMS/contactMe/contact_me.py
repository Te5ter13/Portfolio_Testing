import pprint
import random
import requests
from assertpy import assert_that
from config import BASE_URI
from Blog.blog_posts import auth_header_token


def test_contact_me_list():
    r = contact_me_list()
    assert_that(r.status_code).is_equal_to(200)


def contact_me_list():
    list_URI = f'{BASE_URI}/cms/contact-me-list/'
    r = requests.get(list_URI)
    #pprint.pprint(r.json())
    return r

def test_contact_me_create():
    create_URI = f'{BASE_URI}/cms/contact-me-create/'
    data = {
        'name': 'Mail Test',
        'message': 'Testyourmsg',
        'email': 'email@yahoo.com',
        'subject': 'VIVA',
        'phone_number': '98'
    }
    r = requests.post(url=create_URI, data=data)
    assert_that(r.status_code).is_equal_to(201)
    #pprint.pprint(contact_me_list().json())


def test_contact_me_delete():
    i = id_of_contact_list()
    #pprint.pprint(id)
    id = random.choice(i)
    delete_URI = f'{BASE_URI}/cms/contact-me-delete/{id}/'
    #pprint.pprint(delete_URI)
    r = requests.delete(url=delete_URI, headers=auth_header_token())
    assert_that(r.status_code).is_equal_to(204)


def id_of_contact_list():
    list_of_contacts = contact_me_list().json()
    id = [id_value['id'] for id_value in list_of_contacts['Results']]
    return id


def test_contact_me_detail():
    i = id_of_contact_list()
    id = random.choice(i)
    detail_URI = f'{BASE_URI}/cms/contact-me-detail/{id}/'
    r = requests.get(detail_URI)
    #pprint.pprint(r.json())
    assert_that(r.status_code).is_equal_to(200)


def test_contact_me_update():
    data = {
        'name': 'NameField',
        'message': 'MessageField',
        'email': 'newemail@gmail.com',
        'subject': 'SubjectField',
        'phone_number': 'Invalid Number',
        'address': 'Laapataaa'
    }
    i = id_of_contact_list()
    id = random.choice(i)
    update_URI = f'{BASE_URI}/cms/contact-me-update/{id}/'
    r = requests.patch(url=update_URI, data=data)
    assert_that(r.status_code).is_equal_to(200)
    #pprint.pprint(contact_me_list().json())




