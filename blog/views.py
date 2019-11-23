from django.shortcuts import render

posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018',
    },
    {
        'author': 'Jon Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'September 13, 2019',
    }
]


def home(request):
    """
    :param request: dict
    :return: home.html
    """
    context = {
        'posts': posts
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
