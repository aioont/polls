from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.template import RequestContext, loader
from .models import *
from django.urls import reverse
# Create your views here.

from .models import Question, Choice
from django.db.models import F
from django.utils import timezone
from .models import Question
from django.db.models import Sum
from django.contrib.auth.forms import UserCreationForm
from polls.forms import SignUpForm, LoginForm

from django.contrib.auth import authenticate, login as auth_login
# Rename the login function to avoid conflict with the import
def my_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('polls:index')
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()
    return render(request, 'polls/login.html', {'form': form})                                    



def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'polls/register.html', {'form': form})




def index(request):
    latest_questions = Question.objects.order_by('-pub_date')[:5]
    popular_poll = Question.objects.filter(pub_date__lte=timezone.now()) \
                .annotate(total_votes=Sum('choice__votes')) \
                .order_by('-total_votes') \
                .distinct()[:5]
    context = {'latest_questions': latest_questions, 'popular_poll': popular_poll}
    return render(request, 'polls/index.html', context)



def detail(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request, 'polls/detail.html',{'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    choices = question.choice_set.annotate(num_votes=F('votes')).order_by('-num_votes')
    return render(request, 'polls/results.html', {'question': question, 'choices': choices})

    
def vote(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    try:
        selection_choice = question.choice_set.get(pk = request.POST['choice'])
    except:
        return render(request, 'polls/detail.html', {'question': question, 'error_message': "Please select a chocice"})
    else:
        selection_choice.votes += 1
        selection_choice.save()
        return HttpResponseRedirect(reverse('polls:results',args={question_id,}))

def about(request):
    return render(request, 'polls/about.html')

def contact(request):
    return render(request, 'polls/contact.html')



def createpoll(request):
    if request.method == 'POST':
        question_text = request.POST.get('question_text')
        question = Question.objects.create(question_text=question_text)
        option_count = int(request.POST.get('option_count'))
        for i in range(1, option_count+1):
            choice_text = request.POST.get(f'choice_text_{i}')
            if choice_text:
                question.choice_set.create(choice_text=choice_text)
        return redirect('polls:index')
    else:
        return render(request, 'polls/createpoll.html')

def viewpolls(request):
    questions = Question.objects.all()
    choices = Choice.objects.all()
    return render(request, 'polls/view-polls.html', {
        'questions': questions,
        'choices': choices,
    })



