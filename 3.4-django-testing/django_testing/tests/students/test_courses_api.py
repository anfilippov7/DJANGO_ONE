import pytest
from rest_framework.test import APIClient
from model_bakery import baker
from students.models import Student, Course
from django.conf import settings

@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)

    return factory


@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)

    return factory


@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)

    return factory

@pytest.mark.django_db
def test_get_course(client, course_factory):
    # Arrange
    courses = course_factory(_quantity=10)

    # Act
    response = client.get('/api/v1/courses/1/')
    data = response.json()

    # Assert
    assert response.status_code == 200
    assert data['id'] == 1


@pytest.mark.django_db
def test_get_courses(client, course_factory):
    # Arrange
    courses = course_factory(_quantity=10)

    # Act
    response = client.get('/api/v1/courses/')
    data = response.json()

    # Assert
    assert response.status_code == 200
    assert len(data) == len(courses)


@pytest.mark.django_db
def test_get_id(client, course_factory):
    # Arrange
    courses = course_factory(_quantity=100)

    # Act
    response = client.get(f'/api/v1/courses/?id=100')
    data = response.json()

    # Assert
    assert response.status_code == 200
    assert data[0]['id'] == 100


@pytest.mark.django_db
def test_get_name(client, course_factory):
    # Arrange
    courses = baker.make(Course, name='Python-разработчик')

    # Act
    response = client.get('/api/v1/courses/?name=Python-разработчик')
    data = response.json()

    # Assert
    assert response.status_code == 200
    assert data[0]['name'] == 'Python-разработчик'



@pytest.mark.django_db
def test_post_course(client):
    # Arrange

    # Act
    response = client.post('/api/v1/courses/', {'name': 'DevOps-инженер'}, format='json')
    data = response.json()

    # Assert
    assert response.status_code == 201
    assert data['name'] == 'DevOps-инженер'


@pytest.mark.django_db
def test_patch_name(client, course_factory):
    # Arrange
    courses = baker.make(Course, id=1, name='Python-разработчик')

    # Act
    response = client.patch('/api/v1/courses/1/', {'name': 'DevOps-инженер'}, format='json')
    data = response.json()

    # Assert
    assert response.status_code == 200
    assert data['name'] == 'DevOps-инженер'


@pytest.mark.django_db
def test_delete_name(client, course_factory):
    # Arrange
    courses = baker.make(Course, id=1, name='Python-разработчик')

    # Act
    response = client.delete('/api/v1/courses/1/')

    # Assert
    assert response.status_code == 204


@pytest.mark.parametrize('test_input, expected', [('21', settings.MAX_STUDENTS_PER_COURSE),
                                                  ('20', settings.MAX_STUDENTS_PER_COURSE)])
def test_students_specific_settings(test_input, expected):
    assert eval(test_input) <= expected




























