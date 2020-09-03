import json

from django.contrib.auth.models import User
from django.http import JsonResponse

from blog.models import Blog, Post, PostComment


def blog(request):
    """

    :param request:
            name: str
            tag: str
    :return:
        JsonResponse:
        success/ fail
    """
    response = []
    if request.method == "POST":
        params = json.loads(request.body)
        name = params.get('name')
        tag = params.get('tag')

        Blog.objects.create(name=name, tag=tag)

    if request.method == "GET":
        queryset = Blog.objects.all()
        for _blog in queryset:
            response.append({
                "id": _blog.id,
                "name": _blog.name,
                "tag": _blog.tag,
            })

    return JsonResponse({"message": "api success", "data": response})


def post(request):
    """

    :param request:
            author : user_id
            blog : blog_id
            headline : str
            body_text : str

    :return:
        success / fail
    """

    response = []

    params = json.loads(request.body)
    author_id = params.get('author_id')
    blog_id = params.get('blog_id')
    headline = params.get('headline')
    body_text = params.get('body_text')

    author = User.objects.get(id=author_id)
    blog = Blog.objects.get(id=blog_id)

    Post.objects.create(author=author, blog=blog,
                        headline=headline, body_text=body_text)

    return JsonResponse({"message": "api success", "data": response})


def get_all_post(request):
    queryset = Post.objects.all()
    response = []
    for post in queryset:
        response.append({
            "id": post.id,
            "author_id": post.author.id,
            "author_username": post.author.username,
            "blog_id": post.blog.id,
            "blog_name": post.blog.name,
            "headline": post.headline,
            "body_text": post.body_text,
            "created_at": post.created_at,
            "modifies_at": post.modifies_at
        })

    return JsonResponse({"message": "api success", "data": response})


def post_comment(request):
    params = json.loads(request.body)
    post_id = params.get('post_id')
    user_id = params.get('user_id')
    comment = params.get('comment')
    response = []
    PostComment.objects.create(
        post=Post.objects.get(id=post_id),
        user=User.objects.get(id=user_id),
        comment=comment
    )
    return JsonResponse({"message": "api success", "data": response})


def get_post_comment(request):
    params = json.loads(request.body)
    post_id = params.get('post_id')

    response = []
    queryset = PostComment.objects.filter(post__id=post_id)
    for comment in queryset:
        response.append({
            "post_id": comment.post.id,
            "blog_name": comment.post.blog.name,
            "post_headline": comment.post.headline,
            "username": comment.user.username,
            "comment": comment.comment,
            "created_at": comment.created_at,
            "modifies_at": comment.modifies_at
        })

    return JsonResponse({"message": "api success", "data": response})