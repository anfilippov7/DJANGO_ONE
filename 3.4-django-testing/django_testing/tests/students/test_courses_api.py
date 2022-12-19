import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from model_bakery import baker

from students.models import Student, Course


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def user():
    return Student.objects.create_user('admin')


@pytest.fixture
def message_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)

    return factory



@pytest.mark.django_db
def test_get_messages(client, user, message_factory):
    # Arrange
    messages = message_factory(_quantity=10)

    # Act
    response = client.get('/messages/')

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert len(data) == len(messages)
    for i, m in enumerate(data):
        assert m['text'] == messages[i].text


@pytest.mark.django_db
def test_create_message(client, user):
    count = Course.objects.count()

    response = client.post('/messages/', data={'user': user.id, 'text': 'test text'})

    assert response.status_code == 201
    assert Course.objects.count() == count + 1

























# def test_example():
#     assert False, "Just test example"


# def test_something():
#     assert True


# test_api.py
# создание клиента для запросов
# import pytest
# from rest_framework.reverse import reverse
# from rest_framework.status import HTTP_200_OK
# from rest_framework.test import APIClient
# def test_ping():
#       client = APIClient()
#       url = reverse("/courses/")
#       resp = client.get(url)
#       assert resp.status_code == HTTP_200_OK
#       resp_json = resp.json()
#       assert resp_json["status"] == "Ok"




# from students.models import Course
#
#
# @pytest.mark.django_db
# def test_product_create():
#           product = Course.objects.create(name="Test", students='fdf')
#           assert product.id
#           assert product.name == "Test"