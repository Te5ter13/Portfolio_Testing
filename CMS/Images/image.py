import os
import pprint
import requests
from config import BASE_URI
from assertpy import assert_that
from PIL import Image


def test_cms_image_list():
    r = listing_images()
    pprint.pprint(r.json())
    assert_that(r.status_code).is_equal_to(200)


def listing_images():
    list_URI = f'{BASE_URI}/cms/image-list/'
    r = requests.get(list_URI)
    return r


def test_cms_image_update():
    id = images_list_id()
    update_URI = f'{BASE_URI}/cms/image-update/{id}/'
    with open(os.getcwd()+"/photos/bibek_bro.png", "rb") as image_file:
        files = {
            'image1': image_file
        }
        r = requests.patch(update_URI, files=files)
        assert_that(r.status_code).is_equal_to(200)


def images_list_id():
    id = listing_images().json()[0]['id']
    return id


def test_logo_image_list():
    r = list_logo_image()
    id_of_logo_image()
    assert_that(r.status_code).is_equal_to(200)


def id_of_logo_image():
    id = list_logo_image().json()[0]['id']
    return id


def list_logo_image():
    list_URI = f'{BASE_URI}/cms/logo-image-list/'
    r = requests.get(list_URI)
    return r


def test_logo_image_update():
    id = id_of_logo_image()
    logo_update_URI = f'{BASE_URI}/cms/logo-image-update/{id}/'
    with open(os.getcwd()+"/photos/.....jpg", "rb") as logo_image:
        data = {
            'image': logo_image
        }
        r = requests.get(logo_update_URI, files=data)
        assert_that(r.status_code).is_equal_to(200)


def test_publish_video_list():
    list_URI = f'{BASE_URI}/cms/publish-video-list/'
    r = requests.get(list_URI)
    pprint.pprint(r.json())
    assert_that(r.status_code).is_equal_to(200)