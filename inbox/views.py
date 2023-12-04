from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from django.db.models import Q
from profilepage.models import User
from django.contrib.auth import get_user_model
from cryptography.fernet import Fernet
from django.conf import settings
from .forms import InboxNewMessageForm
from .models import *

# Encryption key for message encryption
f = Fernet(settings.ENCRYPT_KEY)

# View to retrieve and display all users
def get_all_users(request):
    users = User.objects.all() # Query all users from the database
    context = {'users':users}
    return render(users, 'users.html', context) # Render the users in the 'users.html' template

# View for displaying the user's inbox and conversations
@login_required
def inbox_view(request, conversation_id=None):
    # Get all conversations involving the logged-in user
    my_conversations = Conversation.objects.filter(participants=request.user)
    if conversation_id:
        # If a specific conversation is selected, retrieve it
        conversation = get_object_or_404(my_conversations, id=conversation_id)
        latest_message = conversation.messages.first()
        # Mark conversation as seen if the latest message is not sent by the user
        if conversation.is_seen == False and latest_message.sender != request.user:
            conversation.is_seen = True
            conversation.save()
    else:
        conversation = None
    context = {
        'conversation': conversation,
        'my_conversations': my_conversations
    }
    return render(request, 'inbox.html', context) # Render the inbox template


# View for searching users
def search_users(request):
    if request.htmx:
        letters = request.GET.get('search_user') # Get the search term
        if len(letters) > 0:
            # Filter users based on first name
            profiles = User.objects.filter(first_name__contains=letters).exclude(username=request.user)
            return render(request, 'list_searchuser.html', { 'users' : profiles })
        else:
            return HttpResponse('') # Return empty response for empty search term
    else:
        raise Http404()  # Raise 404 error if not an htmx request
    

# View to handle creation of new messages
@login_required     
def new_message(request, recipient_id):
    recipient = get_object_or_404( User, id=recipient_id) # Get the recipient user object
    new_message_form = InboxNewMessageForm() # Instantiate a new message form
    
    if request.method == 'POST':
        form = InboxNewMessageForm(request.POST)
        if form.is_valid(): # Validate the form
            message = form.save(commit=False)

            # encrypt message
            message_original = form.cleaned_data['body']
            message_bytes = message_original.encode('utf-8')
            message_encrypted = f.encrypt(message_bytes)
            message_decoded = message_encrypted.decode('utf-8')
            message.body = message_decoded
            
            message.sender = request.user # Set the sender of the message
            my_conversations = request.user.conversations.all()
            try:
                # Check if a conversation already exists with the recipient
                for c in my_conversations:
                    if recipient in c.participants.all():
                        message.conversation = c
                        message.save()
                        c.lastmessage_created = timezone.now()
                        c.is_seen = False
                        c.save()
                        return redirect('inbox', c.id) # Redirect to the conversation
            except:
                print("oops")
            # Create a new conversation if none exists
            new_conversation = Conversation.objects.create()
            new_conversation.participants.add(request.user, recipient)
            new_conversation.save()
            message.conversation = new_conversation
            message.save() 
            return redirect('inbox', new_conversation.id)
    
    context = {
        'recipient': recipient,
        'new_message_form': new_message_form
    }
    return render(request, 'form_newmessage.html', context)  # Render the new message form


# View to handle replies in a conversation
@login_required
def new_reply(request, conversation_id):
    new_message_form = InboxNewMessageForm()  # Instantiate a new message form
    my_conversations = request.user.conversations.all()
    conversation = get_object_or_404(my_conversations, id=conversation_id) # Get the specified conversation
    
    if request.method == 'POST':
        form = InboxNewMessageForm(request.POST)
        if form.is_valid(): # Validate the form
            message = form.save(commit=False)

            # encrypt message
            message_original = form.cleaned_data['body']
            message_bytes = message_original.encode('utf-8')
            message_encrypted = f.encrypt(message_bytes)
            message_decoded = message_encrypted.decode('utf-8')
            message.body = message_decoded
            
            message.sender = request.user # Set the sender of the message
            message.conversation = conversation
            message.save()
            conversation.lastmessage_created = timezone.now()
            conversation.is_seen = False
            conversation.save()
            return redirect('inbox', conversation.id) # Redirect to the conversation
    
    context = {
        'new_message_form': new_message_form,
        'conversation' : conversation
    }
    return render(request, 'form_newreply.html', context) # Render the reply form


# View to notify the user of a new message in a conversation
def notify_newmessage(request, conversation_id):
    conversation = get_object_or_404(Conversation, id=conversation_id)
    latest_message = conversation.messages.first()
    # Check if the latest message in the conversation is unseen and not sent by the user
    if conversation.is_seen == False and latest_message.sender != request.user:
        return render(request, 'notify_icon.html') # Render notification icon
    else:
        return HttpResponse('') # Return empty response if no new message
    

# View to notify the user of any new messages in their inbox   
def notify_inbox(request):
    my_conversations = Conversation.objects.filter(participants=request.user, is_seen=False)
    for c in my_conversations:
        latest_message = c.messages.first()
        # Check if the latest message in each conversation is not sent by the user
        if latest_message.sender != request.user:
            return render(request, 'notify_icon.html') # Render notification icon
    return HttpResponse('') # Return empty response if no new messages