from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from school.models import Lesson
from users.models import User


class SchoolTestCase(APITestCase):

    def setUp(self) -> None:
        # User_1
        self.user_1 = User.objects.create(
            email="user1@test.com",
            is_staff=False,
            is_active=True,
        )
        self.user_1.set_password('test')
        self.user_1.save()

    def test_create_lesson(self):

        """Зоздание урока"""

        self.client.force_authenticate(user=self.user_1)

        data = {
            'title': 'create_lesson_test',
        }
        response = self.client.post(
            reverse("school:lesson_create"),
            data=data
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEquals(
            response.json(),
            {
                'id': 1,
                'title': 'create_lesson_test',
                'img': None,
                'video': None,
                'description': None,
                'course': None,
                'owner': 1
            }
        )

        self.assertTrue(
            Lesson.objects.all().exists()
        )

    def test_list_lessons(self):

        """Вывод списка уроков"""

        self.client.force_authenticate(user=self.user_1)

        Lesson.objects.create(
            title='title_list_lesson'
        )

        response = self.client.get(
            reverse("school:lesson_list")
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEquals(
            response.json(),
            {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    {
                        'id': 3,
                        'title': 'title_list_lesson',
                        'img': None,
                        'video': None,
                        'description': None,
                        'course': None,
                        'owner': None
                    }
                ]
            }
        )

    def test_retrieve_lesson(self):

        """Вывод урока"""

        self.client.force_authenticate(user=self.user_1)

        lesson = Lesson.objects.create(
            title='title_retrieve_lesson',
            owner=self.user_1
        )

        response = self.client.get(
            reverse("school:lesson_retrieve", kwargs={'pk': lesson.id})
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEquals(
            response.json(),
            {
                'id': 4,
                'title': 'title_retrieve_lesson',
                'img': None,
                'video': None,
                'description': None,
                'course': None,
                'owner': 4
            }
        )

    def test_update_lesson(self):

        """Редактирование урока"""

        self.client.force_authenticate(user=self.user_1)

        lesson = Lesson.objects.create(
            title='title_retrieve_lesson',
            owner=self.user_1
        )

        data = {
            'title': 'title_update_lesson',
        }

        response = self.client.patch(
            reverse("school:lesson_update", kwargs={'pk': lesson.id}),
            data=data

        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEquals(
            response.json(),
            {
                'id': 5,
                'title': 'title_update_lesson',
                'img': None,
                'video': None,
                'description': None,
                'course': None,
                'owner': 5
            }
        )

        self.assertTrue(
            Lesson.objects.all().exists()
        )

    def test_destroy_lesson(self):

        """Удаление урока"""

        self.client.force_authenticate(user=self.user_1)

        lesson = Lesson.objects.create(
            title='title_destroy_lesson',
            owner=self.user_1
        )

        response = self.client.delete(
            reverse("school:lesson_destroy", kwargs={'pk': lesson.id})
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
