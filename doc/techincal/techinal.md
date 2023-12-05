# Technical Documentation For Developers

## Folder Structure
Our Django project, research_match, is separated into two different apps: profilepage and inbox. The Frontend files, such as html and css, are stored in the static and template folders of each app. The static folder holds css files, and the template folder holds html files.

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
- `document.html`: Displays the form for users to add a document. 
- `editprofilepic.html`: Displays the form for users to edit their profile name, skill, biography, and courses.
- `email_confirmation.html`: Welcome and Confirmation Email to newly registered Users
- `form_new_message_match`:
- `home.html`: Home Page
- `LabMain.html`: Lab Profile Page. Displays the profile page that the lab sees which includes name, skills, courses, etc.
- `match_profile.html`:
- `match.html`: All Students page for Labs and Opportunities Page for Students
- `matchedstudents.html`:
- `mentoredit.html`: Displays the form for labs to edit all their information at once.
- `navbar.html`: Navigation Bar
- `picture.html`: Displays the form for users to add a picture.
- `Settings.html`: Settings Page
- `skill.html`: Displays the form for students to edit all their information at once.
- `StudentMain.html`: Student Profile Page. Displays the profile page that the student sees which includes name, skills, courses, etc.
- `test.html`:

- ## /password-reset
    - `password_reset.html`: This allows users to enter email to reset password  
    - `password_reset_sent.html`: This displays text that email has been sent.  
    - `ChangePassword.html`:This allows users to reset their password. 
    - `password_reset_done.html`:This allows displays text that password is reset, and the user can log in.

- ## /registration
    - `loginpage.html`: Login/Sign up Page
  
## Static
-`style.css`:

---
## Inbox

- `admin.py` registers InboxMessage and Conversation model
- `forms.py` stores all form code.
- `models.py` stores the InboxMessage and Conversation model for users.
- `urls.py` holds the paths to matching functions in views.py
- `views.py` holds views where views are Python functions or classes that receive a web request and return a web response. This file holds functions of searching for users and messaging them.

## Templates/HTML files
- `conversation.html`: Displays a specific conversation thread
- `form_newmessage.html`: Form for creating and sending a new message
- `form_newreply.html`: Form for replying to an existing message in a conversation
- `form_searchuser.html`: Search form for finding users within the database
- `inbox.html`: Main inbox view
- `list_searchuser.html`: Displays the list of users as search results
- `my_conversations.html`: Shows the user's conversations list
- `notify_icon.html`: Notification icon component




## Static
-`SSTYLE.css`: style for all html files in Inbox

---

## Media/Documents
In the database, this is where the documents will be stored.

## Media/Profile_pics
In the database, this is where the profile pictures of the users will be stored.


