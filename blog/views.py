from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from blog.models import Post


def home(request):
    """
    :param request: dict
    :return: home.html
    """
    context = {
        'posts': Post.objects.all()  # pylint: disable=E1101
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    """ List of posts """
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    """ Details about post """
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    """ Post creation """
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """ Update post """
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """ Delete post """
    model = Post
    success_url = '/'

    def test_func(self):
        """
        Test if user is author of post
        """
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    """
    :param request: dict
    :return: about.html
    """
    return render(request, 'blog/about.html', {
        'title': 'about',
    })
