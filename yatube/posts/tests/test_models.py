from django.test import TestCase

from ..models import Group, Post, User


class PostModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='auth')
        cls.group = Group.objects.create(
            title='Тестовая группа',
            slug='Тестовый слаг',
            description='Тестовое описание',
        )
        cls.post = Post.objects.create(
            author=cls.user,
            text='Тестовая пост',
        )

    def test_post_have_correct_object_names(self):
        """Проверяем, что у моделей корректно работает __str__."""
        values = {
            self.post.text[:15]: str(self.post),
        }
        for value, expected in values.items():
            with self.subTest(value=value):
                self.assertEqual(value, expected)

    def test_group_have_correct_object_names(self):
        values = {
            self.group.title: str(self.group),
        }
        for value, expected in values.items():
            with self.subTest(value=value):
                self.assertEqual(value, expected)
