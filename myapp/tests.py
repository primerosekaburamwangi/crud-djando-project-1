from datetime import date

from django.test import TestCase

from .forms import UserForm
from .models import User


class UserPageTests(TestCase):
    def create_user(self, email="test@example.com"):
        user = User(
            name="Test User",
            email=email,
            mobile_number="123456789",
            date_of_birth=date(2000, 1, 1),
        )
        user.set_password("BlueHorizon!93")
        user.save()
        return user

    def test_user_list_shows_table_and_add_link(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Your directory starts here")
        self.assertContains(response, "Add a person")

    def test_directory_shows_profile_card_and_local_avatar(self):
        self.create_user()

        response = self.client.get("/")

        self.assertContains(response, "Test User")
        self.assertContains(response, "avatar-1.svg")
        self.assertContains(response, "data-user-search")
        self.assertContains(response, "myapp/css/app.css")

    def test_add_user_page_renders_form(self):
        response = self.client.get("/Add/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "<form")
        self.assertContains(response, "csrfmiddlewaretoken")

    def test_add_user_hashes_submitted_password(self):
        response = self.client.post(
            "/Add/",
            {
                "name": "New User",
                "email": "new@example.com",
                "password": "BlueHorizon!93",
                "mobile_number": "123456789",
                "date_of_birth": "2000-01-01",
            },
        )

        self.assertRedirects(response, "/")
        user = User.objects.get(email="new@example.com")
        self.assertTrue(user.check_password("BlueHorizon!93"))
        self.assertNotEqual(user.password, "BlueHorizon!93")

    def test_edit_page_uses_tracked_template_name(self):
        user = self.create_user()

        response = self.client.get(f"/Edit/{user.pk}/")

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "edit.html")
        self.assertTrue(user.check_password("BlueHorizon!93"))

    def test_password_is_hashed_and_not_displayed(self):
        user = self.create_user()

        response = self.client.get("/")

        self.assertNotEqual(user.password, "BlueHorizon!93")
        self.assertTrue(user.check_password("BlueHorizon!93"))
        self.assertNotContains(response, "BlueHorizon!93")
        self.assertNotContains(response, user.password)

    def test_edit_form_keeps_password_when_left_blank(self):
        user = self.create_user()
        existing_password = user.password
        form = UserForm(
            {
                "name": user.name,
                "email": user.email,
                "password": "",
                "mobile_number": user.mobile_number,
                "date_of_birth": "2000-01-01",
            },
            instance=user,
        )

        self.assertTrue(form.is_valid(), form.errors)
        updated_user = form.save()
        self.assertEqual(updated_user.password, existing_password)
