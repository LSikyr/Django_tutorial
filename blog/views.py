from django.shortcuts import render
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


def about(request):
    """
    :param request: dict
    :return: about.html
    """
    return render(request, 'blog/about.html', {
        'title': 'about',
    })
