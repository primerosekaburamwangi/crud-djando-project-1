# Primobackend

## Local development

Use the project virtual environment and start Django:

```powershell
.\venv\Scripts\python.exe -m pip install -r requirements.txt
.\venv\Scripts\python.exe manage.py migrate
.\venv\Scripts\python.exe manage.py runserver
```

Open `http://127.0.0.1:8000/`. Development defaults use the local MySQL database
`primobackend` with the `root` account and no password. Override these defaults
with environment variables if your local database differs.

The directory uses bundled illustrated avatars when a profile has no uploaded
photo. Uploaded images replace the fallback, and the add/edit form previews a
selected image before saving.

## Production configuration

Set these environment variables before starting the application:

- `DJANGO_DEBUG=False`
- `DJANGO_SECRET_KEY` to a unique, randomly generated secret
- `DJANGO_ALLOWED_HOSTS` to the actual host names, comma-separated
- `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, and `DB_PORT`
- `MAILER_HOST` and, when required by the mail provider, `MAILER_USERNAME` and
  `MAILER_PASSWORD`
- `DEFAULT_FROM_EMAIL`
- `DEFAULT_FROM_EMAIL`

Back up an existing database before applying migrations. The password migration
converts previously stored plaintext values to one-way hashes; they cannot be
recovered as plaintext afterward.

Production mode enforces HTTPS redirects, secure session and CSRF cookies, and
HSTS. Terminate TLS at the application server or a correctly configured HTTPS
reverse proxy. Run `manage.py migrate`, `manage.py collectstatic`, and
`manage.py check --deploy` as part of deployment. Serve static and uploaded
media through a production web server or object storage; do not use Django's
development server for production.

Only enable `SECURE_HSTS_INCLUDE_SUBDOMAINS` or `SECURE_HSTS_PRELOAD` if every
affected subdomain is permanently HTTPS-capable.

The user-management pages are intentionally public at present. Anyone who can
reach the site can view, add, edit, and delete records, so do not put private
personal data on a public deployment until access control is added.
