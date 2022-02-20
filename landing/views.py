from django.contrib.auth.views import PasswordChangeView
from django.db.models import Prefetch
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, DetailView
from django.contrib.auth.forms import UserCreationForm
from lessons.forms import *
from lessons.models import Lessons
from .forms import *
from django.contrib import messages


def landing(request):
    if request.user.is_authenticated:
        return redirect('news')
    else:
        return render(request, 'landing/../static/landing.html', locals())


@method_decorator(login_required, name='dispatch')
class News(ListView):
    model = Lessons
    template_name = 'static/news.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Lessons.objects.all().prefetch_related(
            Prefetch('releases', queryset=DoneLessonsModel.objects.filter(user=self.request.user))).all()



@login_required
def aboutus(request):
    return render(request, 'landing/../static/aboutus.html', locals())


@login_required
def diagram(request):
    return render(request, 'landing/../static/diagram.html', locals())


# @method_decorator(login_required, name='dispatch')
# class Theory(DetailView):
#     model = Lessons
#     template_name = 'static/theory.html'
#     context_object_name = 'posts'
#     pk_url_kwarg = 'lesson_id'
#
#     def get_queryset(self):
#         return Lessons.objects.filter(user=self.request.user)

@login_required
def theory(request, lesson_id):
    posts = get_object_or_404(Lessons, pk=lesson_id)
    context = {'posts': posts}
    return render(request, 'landing/../static/theory.html', context)


# @method_decorator(login_required, name='dispatch')
# class Practice(DetailView, CreateView):
#     model = Lessons
#     template_name = 'static/practice.html'
#     context_object_name = 'posts'
#     pk_url_kwarg = 'lesson_id'
#     form_class = LessonDone
#
#     def get_success_url(self):
#         return reverse_lazy('practice', kwargs={'lesson_id': self.pk})
#
#     def get_queryset(self):
#         return Lessons.objects.filter(user=self.request.user)

@login_required
def practice(request, lesson_id):
    form = LessonDone()
    posts = get_object_or_404(Lessons, pk=lesson_id)
    lessonid = Lessons.objects.get(pk=lesson_id)
    relposts = Lessons.objects.prefetch_related('relatedtest').all()
    if request.method == 'POST':
        marks = request.POST["getscore"]
        p, created = DoneLessonsModel.objects.get_or_create(
            user=request.user,
            lessons=lessonid,
        )
        p.mark = int(marks)
        if p.mark >= 4:
            p.done = True
        else:
            p.done = False
        p.save()
        form = LessonDone(request.POST, instance=p)
        if form.is_valid():
            try:
                form.save()
                return redirect('practice')
            except:
                form.add_error(None, 'Ошибка')
    context = {'posts': posts, 'form': form, 'relposts':relposts}
    return render(request, 'landing/../static/practice.html', context)


# @method_decorator(login_required, name='dispatch')
# class Newwords(DetailView):
#     model = Lessons
#     template_name = 'static/newwords.html'
#     context_object_name = 'posts'
#     pk_url_kwarg = 'lesson_id'
#
#     def get_queryset(self):
#         return Lessons.objects.filter(user=self.request.user)

@login_required
def newwords(request, lesson_id):
    posts = get_object_or_404(Lessons, pk=lesson_id)
    context = {'posts': posts}
    return render(request, 'landing/../static/newwords.html', context)


def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Аккаунт с именем ' + user + ' был создан, теперь можете войти')
            return redirect('login')
    context = {'form': form}
    return render(request, 'registration/register.html', context)


def profilePage(request):
    user = request.user
    form = ProfileForm(instance=user)
    context = {'form': form}
    return render(request, 'registration/profile/profile.html', context)


def editprofilePage(request):
    user = request.user
    form = EditProfileForm(instance=user)

    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    context = {'form': form}
    return render(request, 'registration/profile/editprofile.html', context)


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('password_success')
    template_name = 'registration/profile/edit_password.html'


def password_success(request):
    return render(request,'registration/profile/password_success.html')


def intro(request):
    return render(request,'landing/../static/intro.html')


def intro2(request):
    return render(request,'landing/../static/intro2.html')


def intro3(request):
    return render(request,'landing/../static/intro3.html')