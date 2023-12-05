# README: Student Search Function for Lab Users

## Introduction
This document details the student search function in our Django web application, designed for lab users to search for and view student profiles.

## Dependencies
- **Django**: The primary Python web framework used for development.

## Models

### StudentProfile
Represents individual student profiles. Key fields include:
- `user`: Links to the User model, associating each profile with a specific user.
- `matches`: Represents connections to other student profiles.
- Additional fields like `gpa`, `skill`, `course`, and `biography` provide detailed information about each student.

## Views

### 1. `students`
- **Purpose**: Displays the main interface for lab users to access student functionalities.
- **Access Control**: Restricted to 'lab' role users, enforced by the `@allowed_users` decorator.
- **Rendering**: Utilizes the 'students.html' template.

### 2. `search_students`
- **Purpose**: Handles dynamic searching of student profiles.
- **Access Control**: Intended for 'lab' role users.
- **Functionality**:
  - **Profile Retrieval**: Fetches all entries from the `StudentProfile` model.
  - **Search Filter**: Applies user-input criteria to filter student profiles.
  - **Dynamic Updating**: Employs HTMX for responsive updating of search results.

## Security and Permissions
- The search functionality is secured by role-based access control, limiting usage to authorized 'lab' users. This ensures that student data is accessed responsibly and confidentially.
