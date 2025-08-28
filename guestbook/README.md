# Django Guestbook

A minimal Django guestbook where users must be logged in to post messages. Includes login, signup, and logout views and templates. All pages inherit from a modern, responsive `base.html`.

## Quickstart

1) Create and activate a virtual environment

```powershell
cd guestbook
py -m venv .venv
. .venv\\Scripts\\activate
```

2) Install Django

```powershell
pip install Django
```

3) Initialize the database

```powershell
python manage.py migrate
```

4) (Optional) Create an admin user

```powershell
python manage.py createsuperuser
```

5) Run the server

```powershell
python manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser.

## App Structure

- Project: `core`
- App: `guestbook`
- Model: `Message(user, content, created_at)`
- Auth: `LoginView`, `LogoutView`, custom `signup_view`

## Key URLs

- `/` — Guestbook list and post form (post requires login)
- `/add/` — Post a message (POST only, login required)
- `/accounts/login/` — Login
- `/accounts/signup/` — Sign up
- `/accounts/logout/` — Logout

## Notes

- Static styles in `static/css/styles.css` provide a clean, modern look.
- Update `SECRET_KEY` in `core/settings.py` for production.
- `DEBUG=True` is for development only.
