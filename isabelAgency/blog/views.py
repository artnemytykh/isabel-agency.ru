from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 3)

    paginator.object_list = list(reversed(paginator.object_list))

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    page = page_obj

    post_count = len(page)
    while page.has_previous():
        page = paginator.get_page(page.previous_page_number())
        post_count += len(page)

    return render(request, 'blog/index.html', {
        "posts": page_obj,
        "all_posts": posts,
        "post_count": post_count
    })

def post(request, id):
    post = Post.objects.get(pk=id)
    return render(request, 'blog/post.html', {
        "post": post
    })