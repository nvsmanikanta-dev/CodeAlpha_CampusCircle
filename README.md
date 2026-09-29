# CampusCircle

### A Community Platform for Student Makers

CampusCircle is a full-stack social media platform developed as **Task 2 – Social Media Platform** for the **CodeAlpha Full Stack Development Internship**.

The platform is designed for students to share projects, learning updates, events, questions, and opportunities while connecting with other members through posts, comments, likes, follows, bookmarks, and profiles.

---

## Project Demo

Watch the complete CampusCircle project demonstration on LinkedIn:

### [▶ View CampusCircle Demo on LinkedIn](https://www.linkedin.com/feed/update/urn:li:activity:7510747080848461824/)

The demo showcases:

- User registration and login
- Personalized feed
- User profiles
- Creating posts
- Comments
- Likes
- Follow / unfollow
- Saved posts
- Explore section
- Search
- Responsive interface
- Application workflow

---

## Project Overview

CampusCircle is a community-focused social platform built around student interaction and collaboration.

Users can create profiles, publish updates, interact with posts, follow other members, save useful content, search for people, and explore posts by topic.

The application combines frontend design, backend logic, authentication, database relationships, media uploads, and responsive layouts into a complete full-stack project.

---

## Key Features

### User Authentication

- User registration
- Sign in
- Sign out
- Django authentication
- User-specific sessions

### User Profiles

Each member has a profile containing:

- Name
- Bio
- Location
- Avatar
- User posts
- Followers count
- Following count

Users can edit their own profile information.

### Community Feed

CampusCircle includes a structured social feed with topic-based filtering.

Available topics include:

- Build
- Learn
- Events
- Ask
- Opportunities

Users can also switch to a **Following** feed to view posts from people they follow.

### Posts

Users can:

- Create text posts
- Add uploaded images
- Add an image using a URL
- Select a topic
- View posts in the community feed
- Delete their own posts

### Comments

Members can comment on posts and participate in conversations.

### Likes

Users can like and unlike posts.

The like relationship is stored in the database to maintain interaction state.

### Follow System

Users can:

- Follow other members
- Unfollow members
- View follower and following counts
- Access posts from followed users

### Saved Posts

Important posts can be bookmarked and revisited later through the saved-posts section.

### Search

CampusCircle includes people search to help users discover other members.

### Explore

The Explore section provides topic-based content discovery across the platform.

### Image Uploads

Posts support image uploads.

Uploaded files are validated as images and limited to **5 MB**.

### Admin Panel

Django Admin is available for:

- User management
- Profile inspection
- Post moderation
- Comment management
- Database administration

---

## Tech Stack

### Frontend

- HTML5
- CSS3
- JavaScript
- Django Templates

### Backend

- Python
- Django 5.2

### Database

- SQLite
- Django ORM

### Media

- Pillow
- Django media handling

### Development Tools

- Visual Studio Code
- Git
- GitHub

---

## Application Flow

```text
User
 │
 ├── Register / Login
 │
 ▼
CampusCircle Feed
 │
 ├── Create Post
 ├── Browse Topics
 ├── View Following Feed
 │
 ▼
Social Interaction
 │
 ├── Like
 ├── Comment
 ├── Follow
 ├── Save Post
 │
 ▼
Explore / Search
 │
 ▼
Profiles & Community
```

---

## Project Structure

```text
CodeAlpha_CampusCircle/
│
├── campuscircle_core/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── social/
│   ├── management/
│   │   └── commands/
│   │       └── seed_demo.py
│   │
│   ├── migrations/
│   ├── admin.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── ...
│
├── templates/
│   ├── feed
│   ├── explore
│   ├── search
│   ├── profile
│   ├── saved
│   └── authentication pages
│
├── static/
│   ├── css/
│   └── js/
│
├── START.bat
├── manage.py
├── requirements.txt
├── PROJECT_REQUIREMENTS_CHECKLIST.md
└── README.md
```

---

## Database Design

CampusCircle uses Django models to manage the platform's social relationships.

### Profile

Extends the Django user account with additional profile information.

### Post

Stores:

- Author
- Content
- Topic
- Optional media
- Creation information

### Comment

Connects users with conversations under posts.

### Like

Stores post-like relationships between users and posts.

### Follow

Manages follower and following relationships between members.

### Bookmark

Stores saved posts for each user.

---

## Installation & Setup

### Option 1 — Quick Start on Windows

After cloning or downloading the project, run:

```text
START.bat
```

The setup script prepares the local environment, installs dependencies, initializes the database, loads demo content, and starts the application.

---

## Manual Setup

### 1. Clone the Repository

```bash
git clone https://github.com/nvsmanikanta-dev/CodeAlpha_CampusCircle.git
```

### 2. Open the Project Folder

```bash
cd CodeAlpha_CampusCircle
```

### 3. Create a Virtual Environment

```bash
py -3 -m venv .venv
```

### 4. Activate the Environment

#### PowerShell

```powershell
.\.venv\Scripts\Activate.ps1
```

#### Command Prompt

```cmd
.venv\Scripts\activate.bat
```

### 5. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 6. Apply Database Migrations

```bash
python manage.py migrate
```

### 7. Load Demo Content

```bash
python manage.py seed_demo
```

This step is optional.

The command creates fictional demo users and sample content for local testing.

### 8. Start the Server

```bash
python manage.py runserver
```

### 9. Open CampusCircle

```text
http://127.0.0.1:8000/
```

To create your own account:

```text
http://127.0.0.1:8000/register/
```

---

## Admin Setup

Create a Django superuser:

```bash
python manage.py createsuperuser
```

Start the server:

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/admin/
```

---

## Verify the Project

Run Django's system checks:

```bash
python manage.py check
```

Run the test suite:

```bash
python manage.py test
```

---

## CodeAlpha Task 2

### Social Media Platform

This project was developed to satisfy the requirements of **CodeAlpha Task 2 – Social Media Platform**.

### Task Coverage

| CodeAlpha Requirement | CampusCircle Implementation |
|---|---|
| User Profiles | Editable member profiles with bio, location, avatar, posts, followers and following |
| Posts | Topic-based posts with text and optional media |
| Comments | Comment threads under posts |
| Like System | Like / unlike functionality |
| Follow System | Follow / unfollow relationships |
| Frontend | HTML, CSS and JavaScript |
| Backend | Django |
| Database | SQLite with Django ORM |
| Users | Django authentication and Profile model |
| Posts | Post model |
| Comments | Comment model |
| Followers | Follow relationship model |

---

## Topics

CampusCircle organizes community discussions into five categories:

### Build

Share projects, development progress, prototypes, and technical work.

### Learn

Share learning experiences, resources, concepts, and useful information.

### Events

Post information related to workshops, meetups, hackathons, and campus events.

### Ask

Ask questions and receive help from the community.

### Opportunities

Share internships, competitions, jobs, programs, and other opportunities.

---

## Demo Data

CampusCircle provides an optional demo-data command:

```bash
python manage.py seed_demo
```

The generated demo accounts and sample content are fictional and are intended only for local testing.

Demo users are not intended to be used as normal login accounts.

---

## Media Handling

User-uploaded post images are stored locally under:

```text
media/posts/
```

Uploaded media and the local SQLite database are generated at runtime and are excluded from Git where appropriate.

---

## Local Development Notes

The repository is configured for local development.

Before deploying the project publicly, production configuration should include:

- A secure Django secret key
- `DEBUG=False`
- Correct `ALLOWED_HOSTS`
- Production-ready database configuration
- Secure media storage
- HTTPS
- Proper static-file deployment
- Moderation and security review

---

## Learning Outcomes

Through CampusCircle, I gained practical experience in:

- Full-stack application development
- Django architecture
- User authentication
- Django ORM
- Database relationships
- Social-media workflows
- Profile management
- Posts and comments
- Like systems
- Follow relationships
- Search functionality
- Media uploads
- Responsive frontend design
- Git and GitHub version control

---

## Project Links

### GitHub Repository

[**CodeAlpha_CampusCircle**](https://github.com/nvsmanikanta-dev/CodeAlpha_CampusCircle)

### LinkedIn Project Demo

[**View CampusCircle Project Demo**](https://www.linkedin.com/feed/update/urn:li:activity:7510747080848461824/)

### LinkedIn Profile

[**Nunna Venkata Sai Manikanta**](https://www.linkedin.com/in/nunna-venkata-sai-manikanta-6a5506356/)

---

## Author

### Nunna Venkata Sai Manikanta

**Full Stack Development Intern**

GitHub:  
[github.com/nvsmanikanta-dev](https://github.com/nvsmanikanta-dev)

LinkedIn:  
[linkedin.com/in/nunna-venkata-sai-manikanta-6a5506356](https://www.linkedin.com/in/nunna-venkata-sai-manikanta-6a5506356/)

---

## Internship

This project was completed as part of the **CodeAlpha Full Stack Development Internship**.

**Task:** Task 2 – Social Media Platform  
**Project:** CampusCircle

---

<p align="center">
  <b>CampusCircle</b><br>
  A Community for Student Makers<br><br>
  CodeAlpha Full Stack Development Internship · Task 2
</p>
