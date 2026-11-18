from django.contrib.auth.hashers import identify_hasher, is_password_usable, make_password
from django.db import migrations, models


def hash_existing_passwords(apps, schema_editor):
    User = apps.get_model("myapp", "User")
    database = schema_editor.connection.alias
    users = User.objects.using(database).only("pk", "password").iterator()

    for user in users:
        password = user.password
        if not password:
            encoded = make_password(None)
        elif not is_password_usable(password):
            continue
        else:
            try:
                identify_hasher(password)
            except ValueError:
                encoded = make_password(password)
            else:
                continue
        User.objects.using(database).filter(pk=user.pk).update(password=encoded)


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0002_user_delete_employee"),
    ]

    operations = [
        migrations.RunPython(
            hash_existing_passwords,
            migrations.RunPython.noop,
        ),
        migrations.AlterField(
            model_name="user",
            name="password",
            field=models.CharField(max_length=128),
        ),
    ]
