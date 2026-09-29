from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from social.models import Follow, Post


DEMO_USERS = [
    ('anjali_builds', 'Anjali', 'Rao', 'Building small products and sharing the process.', 'Vijayawada'),
    ('arjun_codes', 'Arjun', 'Dev', 'Backend, data and a little design.', 'Hyderabad'),
    ('meera_creates', 'Meera', 'K', 'I turn ideas into useful interfaces.', 'Bengaluru'),
]
DEMO_POSTS = [
    ('anjali_builds', 'BUILD', 'We finished the first version of our campus event board today. The best part was watching someone outside our team find an event in seconds. What would you improve next?'),
    ('arjun_codes', 'LEARN', 'A small habit that helped me: write down one bug, the actual cause and the fix after each coding session. The notes become your own troubleshooting guide.'),
    ('meera_creates', 'EVENTS', 'Our design and development meetup is this Saturday. Bring a project you are working on, even if it is unfinished. We will share feedback and ideas.'),
    ('anjali_builds', 'ASK', 'For a student project with a Django backend, would you start with SQLite and move to PostgreSQL later? I am collecting practical advice.'),
    ('arjun_codes', 'OPPORTUNITIES', 'Looking for one teammate to help test an open source study planner. If you enjoy finding edge cases, message me in person at our next campus meetup.'),
]


class Command(BaseCommand):
    help = 'Create fictional local-only CampusCircle members and posts'

    def handle(self, *args, **kwargs):
        for username, first, last, bio, location in DEMO_USERS:
            user, created = User.objects.get_or_create(username=username, defaults={
                'first_name': first, 'last_name': last, 'email': f'{username}@example.invalid',
            })
            if created:
                user.set_unusable_password()
                user.save(update_fields=['password'])
            user.profile.bio = bio
            user.profile.location = location
            user.profile.save(update_fields=['bio', 'location'])
        for username, topic, content in DEMO_POSTS:
            author = User.objects.get(username=username)
            Post.objects.get_or_create(author=author, topic=topic, content=content)
        Follow.objects.get_or_create(follower=User.objects.get(username='anjali_builds'), following=User.objects.get(username='arjun_codes'))
        self.stdout.write(self.style.SUCCESS('CampusCircle demo community is ready. Demo users cannot log in.'))
