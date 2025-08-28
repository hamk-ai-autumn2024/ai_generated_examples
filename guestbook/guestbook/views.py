from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views.generic import ListView

from .forms import MessageForm, SignupForm
from .models import Message


class MessageListView(ListView):
    model = Message
    template_name = 'guestbook/message_list.html'
    context_object_name = 'guestbook_messages'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = MessageForm()
        return context


@login_required
def add_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            msg = form.save(commit=False)
            msg.user = request.user
            msg.save()
            messages.success(request, 'Message posted!')
    return redirect('guestbook:list')


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Welcome! Your account is ready.')
            return redirect('guestbook:list')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', { 'form': form })
