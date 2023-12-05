### Technical Documentation For Developers

## Folder Structure
Our Django project, research_match, is separated into three different apps: profilepage, inbox, and search. Each of the Frontend is stored in the static and template folders of each app. The static folder holds css files, and the template folder holds html files.

---
## Profilepage - Main app

- `admin.py` registers StudentProfile model
- `apps.py` is a configuration file
- `decorators.py` restricts access to views or "pages" in accordance to which group user is in.
- `forms.py` stores all form code.
- `models.py` stores the StudentProfile model for labs and students.
- `signals.py` sets up signal handlers for the User model. When a new User instance is created, it automatically creates a corresponding StudentProfile instance (create_profile function) and saves it (save_profile function).
- `tokens.py` holds TokenGenerator. This creates a one time token that is generate for every newly created users, which is unique and static.
- `urls.py` holds the paths to matching functions in views.py
- `views.py` holds views where views are Python functions or classes that receive a web request and return a web response. This file holds functions of user registration, log in, update user profile, matching/unmatching, and a matching algorithm.

## Templates/HTML files

- `activation_failed.html`: Activation Failed Page
- `document.html`:
- `editprofilepic.html`:
- `email_confirmation.html`: Welcome and Confirmation Email to newly registered Users
- `form_new_message_match`:
- `get_skills.html`:
- `home.html`:
- `LabMain.html`:
- `match_profile.html`:
- `match.html`:
- `matchedstudents.html`:
- `mentoredit.html`:
- `navbar.html`: Navigation Bar Page
- `picture.html`:
- `Settings.html`:
- `skill.html`:
- `StudentMain.html`:
- `test.html`:

- ## /password-reset
    - `password_reset.html`: This allows users to enter email to reset password  
    - `password_reset_sent.html`: This displays text that email has been sent.  
    - `ChangePassword.html`:This allows users to reset their password. 
    - `password_reset_done.html`:This allows displays text that password is reset, and the user can log in.

- ## /registration
    - `loginpage.html`: Login/Sign up Page
  
## static
-`style.css`:

---
## Inbox

- `admin.py` registers InboxMessage and Conversation model
- `forms.py` stores all form code.
- `models.py` stores the InboxMessage and Conversation model for users.
- `urls.py` holds the paths to matching functions in views.py
- `views.py` holds views where views are Python functions or classes that receive a web request and return a web response. This file holds functions of searching for users and messaging them.

## Templates/HTML files
- `conversation.html`:
- `form_newmessage.html`:
- `form_newreply.html`:
- `form_searchuser.html`:
- `inbox.html`:
- `list_searchuser.html`:
- `my_conversations.html`:
- `notify_icon.html`:

## static
-`SSTYLE.css`: style for all html files in Inbox

---
## Search
- `admin.py` registers SearchQuery and SearchQueryAdmin model
- `forms.py` stores all form code.
- `models.py` stores the SearchQuery model for users.
- `urls.py` holds the paths to matching functions in views.py
- `views.py` holds views where views are Python functions or classes that receive a web request and return a web response.

## media/documents
In the database, this is where the documents will be stored.

## media/profile_pics
In the database, this is where the profile pictures of the users will be stored.


