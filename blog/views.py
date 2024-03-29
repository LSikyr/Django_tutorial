from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
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
        'posts': Post.objects.all()  # pylint: disable=no-member
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    """ List of posts """
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


class UserPostListView(ListView):
    """ List of user posts """
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')  # pylint: disable=no-member


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
