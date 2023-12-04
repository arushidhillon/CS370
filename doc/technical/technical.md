### Technical Documentation

## Folder Structure
Our Django project, research_match, is separated into three different apps: profilepage, inbox, and search. Each of the Frontend is stored in the static and template folders of each app. The static folder holds css files, and the tamplate folder holds html files.

---
## Profilepage - Main app
[admin.py] registers StudentProfile model
- apps.py is a configuration file
- decorators.py restricts access to views or "pages" in accordance to which group user is in.
- forms.py stores all form code.
- models.py stores the StudentProfile model for labs and students.
- signals.py sets up signal handlers for the User model. When a new User instance is created, it automatically creates a corresponding StudentProfile instance (create_profile function) and saves it (save_profile function).
- tokens.py holds TokenGenerator. This creates a one time token that is generate for every newly created users, which is unique and static.
- urls.py holds the paths to matching functions in views.py
- views.py holds views where views are Python functions or classes that receive a web request and return a web response. This file holds functions of user registration, log in, update user profile, matching/unmatching, and a matching algorithm.


