import json
from django.http import JsonResponse

from blog.models import Blog


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
