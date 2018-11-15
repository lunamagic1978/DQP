from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import *


@csrf_exempt
def create_namespace(request):
    if request.method == "POST":
        data = request.POST
        namespace = data["namespace"]
        try:
            ApiNameSpace.objects.get(namespace=namespace)
            return JsonResponse({"msg": "namespace已经存在",
                                 "code": 300})
        except Exception:
            ApiNameSpace.objects.create(namespace=namespace)
            return JsonResponse({"msg": "namespace创建成功",
                                 "code": 200})
    else:
        return JsonResponse({"msg": "请求方法不正确",
                             "code": 400})