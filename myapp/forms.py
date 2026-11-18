# app - forms.py file new

from django import forms
from django.contrib.auth.password_validation import validate_password

from .models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(
        max_length=128,
        strip=False,
        widget=forms.PasswordInput,
    )

    class Meta:
        model = User
        fields = (
            "name",
            "photo",
            "email",
            "password",
            "mobile_number",
            "date_of_birth",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._existing_password = (
            self.instance.password if self.instance.pk else None
        )
        self._keep_password = False
        if self.instance.pk:
            self.fields["password"].required = False
            self.fields["password"].help_text = (
                "Leave blank to keep the current password."
            )
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"

    def clean_password(self):
        password = self.cleaned_data.get("password")
        if not password and self._existing_password:
            self._keep_password = True
            return self._existing_password
        if password:
            validate_password(password, self.instance)
        return password

    def save(self, commit=True):
        user = super().save(commit=False)
        if not self._keep_password:
            user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
            self.save_m2m()
        return user
