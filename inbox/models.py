from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.timesince import timesince
from cryptography.fernet import Fernet
from django.conf import settings
import uuid

# Model for individual messages in the inbox system
class InboxMessage(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_messages") # Reference to the user who sent the message
    conversation = models.ForeignKey('Conversation', on_delete=models.CASCADE, related_name="messages")  # Reference to the conversation the message belongs to
    body = models.TextField() # The body of the message
    created = models.DateTimeField(auto_now_add=True) # Timestamp when the message was created

    # Method to decrypt the message body
    @property
    def body_decrypted(self):
        f = Fernet(settings.ENCRYPT_KEY) # Encryption key from settings
        message_decrypted = f.decrypt(self.body) # Decrypt the message body
        message_decoded = message_decrypted.decode('utf-8') # Decode the decrypted message
        return message_decoded
    
    # Metadata options for the InboxMessage model
    class Meta:
        ordering = ['-created'] # Orders messages by their creation time, newest first

    # String representation of the InboxMessage model  
    def __str__(self):
        time_since = timesince(self.created, timezone.now()) # Time since the message was sent
        return f'[{self.sender.username} : {time_since} ago]' # Format: [sender: time since sent ago]
    
# Model representing a conversation between users
class Conversation(models.Model):
    id = models.CharField(max_length=100, default=uuid.uuid4, unique=True, primary_key=True, editable=False) # Unique ID for the conversation
    participants = models.ManyToManyField(User, related_name='conversations') # Users participating in the conversation
    lastmessage_created = models.DateTimeField(default=timezone.now)  # Timestamp of the last message sent in the conversation
    is_seen = models.BooleanField(default=False) # Flag to indicate if the last message has been seen
    
    # Metadata options for the Conversation model
    class Meta:
        ordering = ['-lastmessage_created'] # Orders conversations based on the latest message sent
        
    # String representation of the Conversation model
    def __str__(self):
        user_names = ", ".join(user.username for user in self.participants.all()) # Join usernames of participants
        return f'[{user_names}]' # Format: [username1, username2, ...]