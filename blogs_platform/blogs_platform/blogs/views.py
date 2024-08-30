from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Value, F
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import UserPassesTestMixin

from .models import Profile, Blog, Comment, Messages, Subscibers, User
from .forms import BlogForm, MessagesForm, CommentForm, UserRegistrationForm, LoginForm
from django.views.generic.base import TemplateView
# Create your views here.


def blog_list(request):
    blogs = Blog.objects.all()
    paginator = Paginator(blogs, 1, orphans=1)
    if 'page' in request.GET:
        page_num = request.GET['page']
    else:
        page_num = 1
    page = paginator.get_page(page_num)
    context = {"object_list": page.object_list, "page_obj": page}
    return render(request, "/blog_list.html", context)

class BlogCreate(CreateView):
    model = Blog
    success_url = reverse_lazy('blog_list')
    form_class = BlogForm


class BlogDelete(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog_list')
    template_name = 'blog/blog_form.html'


class BlogUpdate(UpdateView):
    model = Blog
    fields = '__all__'
    success_url = reverse_lazy('blog_list')


class BlogList(ListView):
    model = Blog
    paginate_by = 2
    paginate_orphans = 1

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, 'Bce блоги')
        return super().dispatch(request, *args, **kwargs)


class BlogDetail(DetailView):
    model = Blog
    context_object_name = 'blog'

##############################################
def message_list(request):
    messages = Messages.objects.all()
    paginator = Paginator(messages, 1, orphans=1)
    if 'page' in request.GET:
        page_num = request.GET['page']
    else:
        page_num = 1
    page = paginator.get_page(page_num)
    context = {"object_list": page.object_list, "page_obj": page}
    return render(request, "blog/message_list.html", context)

class MessagesCreate(CreateView):
    model = Blog
    success_url = reverse_lazy('massage_list')
    form_class = MessagesForm


class MessagesDelete(DeleteView):
    model = Messages
    success_url = reverse_lazy('massage_list')
    template_name = '/message_form.html'


class MessagesUpdate(UpdateView):
    model = Messages
    fields = '__all__'
    success_url = reverse_lazy('massage_list')


class MessagesList(ListView):
    model = Messages
    paginate_by = 2
    paginate_orphans = 1

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, 'Bce сообщения')
        return super().dispatch(request, *args, **kwargs)


class MessagesDetail(DetailView):
    model = Messages
    context_object_name = 'massage'
#########################################

def comment_list(request):
    comments = Comment.objects.all()
    paginator = Paginator(comments, 1, orphans=1)
    if 'page' in request.GET:
        page_num = request.GET['page']
    else:
        page_num = 1
    page = paginator.get_page(page_num)
    context = {"object_list": page.object_list, "page_obj": page}
    return render(request, "/comment_list.html", context)

class CommentCreate(CreateView):
    model = Comment
    success_url = reverse_lazy('comment_list')
    form_class = CommentForm


class CommentDelete(DeleteView):
    model = Comment
    success_url = reverse_lazy('comment_list')
    template_name = '/comment_form.html'


class CommentUpdate(UpdateView):
    model = Comment
    fields = '__all__'
    success_url = reverse_lazy('comment_list')


class CommentList(ListView):
    model = Comment
    paginate_by = 2
    paginate_orphans = 1

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, 'Bce комментарии')
        return super().dispatch(request, *args, **kwargs)


class CommentDetail(DetailView):
    model = Comment
    context_object_name = 'comment'

class MainPage(TemplateView):
    template_name = 'store/about.html'


class UserRegisterView(FormView, UserPassesTestMixin):
    template_name = 'store/product_form.html'
    form_class = UserRegistrationForm
    success_url = 'store/about.html'

    def post(self, request, *args, **kwargs):
        data = dict(request.POST)
        pass1 = data.pop('password1') # None
        pass2 = data.pop('password2') # None
        form = UserRegistrationForm(request.POST)
        if pass1 != pass2:
            return self.form_invalid(form)
        else:
            if form.is_valid():
                return self.form_valid(form)
            else:
                return self.form_invalid(form)

    def form_valid(self, form):
        return HttpResponse('New user has been added')
