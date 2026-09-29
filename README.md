# CampusCircle — a community for student makers

**CodeAlpha Full Stack Development · Task 2**  
**Adapted and developed by Nunna Venkata Sai Manikanta**

CampusCircle is a mobile-first social application built around student projects and learning. Members can publish updates under five topics — Build, Learn, Events, Ask and Opportunities — follow one another, comment, like, and save conversations to revisit later. The desktop layout offers a focused feed and member suggestions; mobile screens use bottom navigation.

## Features

- Registration, sign in/out and editable profiles with name, bio, location and avatar URL.
- A community feed with topic filters and a Following view.
- Text posts with an optional uploaded image or image URL.
- Comments, likes, follow/unfollow, profile stats and your own post deletion.
- Saved posts, people search and a topic-based Explore grid.
- Django admin for moderation and data inspection.
- Fictional local demo community via `seed_demo`, with unusable passwords for sample accounts.

Uploads are limited to 5 MB and checked as images. The demo seed command is optional; create a normal account to interact with sample posts.

## Stack

Python, Django 5.2, Pillow, Django templates, HTML, CSS, JavaScript and SQLite. JavaScript handles the composer and a few interface actions; posts and relationships are saved by Django views in the database. The local design uses Google Fonts when online and system fonts when offline.

## Quick start on Windows

Extract the ZIP and double-click **`START.bat`** inside the project folder. It creates `.venv`, installs packages, prepares the database, loads fictional demo content, and starts the server. Use one project at a time on port 8000.

To run the steps manually, open a terminal inside the project folder:

Extract the ZIP and open a terminal **inside `CodeAlpha_CampusCircle`**:

```powershell
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py seed_demo
python manage.py runserver
```

Open <http://127.0.0.1:8000/register/> to make your account. Sample users cannot sign in. To use the admin, run `python manage.py createsuperuser` and open <http://127.0.0.1:8000/admin/>. If PowerShell blocks activation, use Command Prompt with `.venv\Scripts\activate.bat` or call `.\.venv\Scripts\python.exe` directly.

Verify the project:

```powershell
python manage.py check
python manage.py test
```

## Project layout

```text
CodeAlpha_CampusCircle/
├── campuscircle_core/             Django settings and root routes
├── social/                        Profiles, posts, topics, relationships, admin
│   ├── management/commands/seed_demo.py
│   └── migrations/
├── templates/                     Feed, explore, search, profile, saved, auth
├── static/css/                    Responsive visual system
├── static/js/                     Composer and small interface actions
├── START.bat                    Windows one-click local setup
├── manage.py
├── requirements.txt
└── README.md
```

## Data and behavior

`Profile` extends each Django user. `Post` stores author, content, topic and optional media. `Comment`, `Like`, `Follow` and `Bookmark` link members to posts or each other with unique constraints where appropriate. User uploads go to `media/posts/`, which is created at runtime and excluded from Git. The local SQLite database is also created at runtime.

## Internship task coverage

| Task 2 requirement | CampusCircle implementation |
| --- | --- |
| User profiles | Profile page, edit form, posts and relationship counts |
| Posts and comments | Topic posts and comment threads |
| Like/follow system | Toggle endpoints with database relationships |
| HTML/CSS/JavaScript and Django | Responsive templates, styling, composer interactions, server views |
| Database | SQLite-backed users, posts, comments and follows |

## Local development note

The bundled defaults are for local development. Before public hosting, set `DJANGO_SECRET_KEY`, set `DJANGO_DEBUG=0`, configure `DJANGO_ALLOWED_HOSTS`, review moderation needs, and serve uploaded files safely. The sample content and usernames are fictional.

For CodeAlpha submission, create a repository named `CodeAlpha_CampusCircle`, upload this source, and record your own explanation video. The source archive contains no previous Git history, user database, or another person's images.
