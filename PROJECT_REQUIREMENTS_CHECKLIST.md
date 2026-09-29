# CampusCircle · CodeAlpha Task 2

| Required feature | Working route or model |
| --- | --- |
| Profiles | `/u/<username>/`, `/profile/edit/`, Profile |
| Posts | `/`, `/post/create/`, Post with topics |
| Comments | POST `/post/<id>/comment/`, Comment |
| Likes | POST `/post/<id>/like/`, Like |
| Follows | POST `/u/<username>/follow/`, Follow |
| Database | SQLite with Django User and social models |

Additional features: topic filters, Following feed, Explore, saved posts. Run `python manage.py test` for the core flows.
