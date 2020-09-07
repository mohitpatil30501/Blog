import json

from django.contrib.auth.models import User
from django.http import JsonResponse

from blog.models import *


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
        total_like = LikePost.objects.filter(post=post, is_like=True).count()
        response.append({
            "id": post.id,
            "author_id": post.author.id,
            "author_username": post.author.username,
            "blog_id": post.blog.id,
            "blog_name": post.blog.name,
            "headline": post.headline,
            "body_text": post.body_text,
            "total_like": total_like,
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
        total_like = LikeComment.objects.filter(comment=comment, is_like=True).count()
        response.append({
            "post_id": comment.post.id,
            "blog_name": comment.post.blog.name,
            "post_headline": comment.post.headline,
            "username": comment.user.username,
            "comment": comment.comment,
            "total_like": total_like,
            "created_at": comment.created_at,
            "modifies_at": comment.modifies_at
        })

    return JsonResponse({"message": "api success", "data": response})


def sub_comment(request):
    params = json.loads(request.body)
    comment_id = params.get('comment_id')
    created_by_id = params.get('created_by_id')
    sub_comment = params.get('sub_comment')
    response = []
    SubComment.objects.create(
        comment=PostComment.objects.get(id=comment_id),
        created_by=User.objects.get(id=created_by_id),
        sub_comment=sub_comment
    )
    return JsonResponse({"message": "api success", "data": response})


def like_post(request):
    params = json.loads(request.body)
    post_id = params.get('post_id')
    user_id = params.get('user_id')
    is_like = params.get('is_like')

    if LikePost.objects.filter(post__id=post_id, user__id=user_id).exists():
        like = LikePost.objects.get(post__id=post_id, user__id=user_id)
        like.is_like = is_like
        like.save()
    else:
        LikePost.objects.create(
            post=Post.objects.get(id=post_id),
            user=User.objects.get(id=user_id),
            is_like=is_like
        )
    return JsonResponse({"message": "api success"})


def like_comment(request):
    params = json.loads(request.body)
    comment_id = params.get('comment_id')
    user_id = params.get('user_id')
    is_like = params.get('is_like')

    if LikeComment.objects.filter(comment__id=comment_id, user__id=user_id).exists():
        like = LikeComment.objects.get(comment__id=comment_id, user__id=user_id)
        like.is_like = is_like
        like.save()
    else:
        LikeComment.objects.create(
            comment=PostComment.objects.get(id=comment_id),
            user=User.objects.get(id=user_id),
            is_like=is_like
        )
    return JsonResponse({"message": "api success"})
