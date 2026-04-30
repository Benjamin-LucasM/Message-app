from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Message
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('inbox')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def inbox(request):
    query = request.GET.get('q', '').strip()
    results = []
    if query:
        results = User.objects.filter(username__icontains=query).exclude(pk=request.user.pk)

    sent_to = Message.objects.filter(sender=request.user).values_list('receiver', flat=True)
    received = Message.objects.filter(receiver=request.user).values_list('sender', flat=True)
    chat_user_ids = set(sent_to) | set(received)
    chat_users = User.objects.filter(pk__in=chat_user_ids).exclude(pk=request.user.pk)

    return render(request, 'messaging/inbox.html', {
        'results': results,
        'chat_users': chat_users,
        'query': query,
    })

@login_required
def chat(request, username):
    other = get_object_or_404(User, username=username)

    if request.method == 'POST':
        body = request.POST.get('body', '').strip()
        if body:
            Message.objects.create(sender=request.user, receiver=other, body=body)
        return redirect('chat', username=username)

    messages = Message.objects.filter(
        sender=request.user,   receiver=other
    ) | Message.objects.filter(
        sender=other, receiver=request.user
    )
    messages = messages.order_by('timestamp')

    return render(request, 'messaging/chat.html', {
        'other': other,
        'messages': messages,
    })

@login_required
def delete_message(request, message_id):
    message = get_object_or_404(Message, id=message_id, sender=request.user)
    other_username = message.receiver.username
    message.delete()
    return redirect('chat', username=other_username)