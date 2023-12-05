# README: Inbox Function 

## Introduction
This document provides a comprehensive overview of the inbox function developed in Django, enabling students and principal investigators to communicate securely within our web platform.

## Dependencies
- **Django**: The primary Python web framework used.
- **cryptography**: For encrypting and decrypting message content.

## Architecture Overview
The inbox function is integrated within the Django application, following the Model-View-Template (MVT) pattern. It involves models for data representation, views for request handling, and templates for the user interface.

### Models
1. **InboxMessage**: Represents individual messages. Key fields include:
   - `sender`: A reference to the User who sent the message.
   - `conversation`: Links to the Conversation model, indicating which conversation the message belongs to.
   - `body`: The text content of the message.
   - `created`: Timestamp of message creation.
   - `body_decrypted`: A method to decrypt the message body for viewing.

2. **Conversation**: Manages conversation threads. Key fields include: 
   - `id`: A unique identifier for each conversation.
   - `participants`: A ManyToManyField linking to the User model. This field represents the users who are part of the conversation,
     allowing for group conversations.
   - `lastmessage_created`: A DateTimeField that records when the last message in the conversation was created.
   - `is_seen`: A BooleanField that indicates whether the conversation has been seen by the participants.

### Views
1. **get_all_users**: Retrieves all users to facilitate new conversations. Renders a user list in the 'users.html' template.
2. **inbox_view**: Manages the display of the user's inbox, showing conversation threads, and allowing reading and sending messages. Handles both retrieval of existing conversations and creation of new ones.
3. **search_users**: Provides functionality to search for users within the system. Useful for finding specific individuals to start a new conversation.
4. **new_message**: Manages the creation of new messages. Allows users to send messages to other users identified by recipient_id.
5. **new_reply**: Enables users to reply within an existing conversation. Takes conversation_id to append the reply to the correct conversation thread.
6. **notify_newmessage**: Sends notifications for new messages within a conversation. Takes conversation_id to identify the relevant conversation for the notification.
7. **notify_inbox**: Manages inbox notifications. Notifies users of any new messages or updates in their inbox.

## Functionality
- **User Authentication**: Ensures secure access to the inbox.
- **Conversation Management**: Facilitates private conversations.
- **Message Encryption**: Protects the privacy of communications.

## Security Features
### Authentication
- **Django Authentication**: Manages user sessions and access.
- **@login_required Decorator**: Restricts inbox actions to authenticated users.

### Message Encryption
- **Encryption Key**: Utilizes a Fernet key from Django settings.
- **Fernet Encryption**: Secures messages in the database and decrypts them when retrieved.
- **cryptography Library**: Provides robust encryption in line with modern standards.
