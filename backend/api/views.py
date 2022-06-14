from django.http import JsonResponse
import json
from django.forms.models import model_to_dict
from products.models import Product

from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.


@api_view(["GET"])
def api_home(request, *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        # data['id'] = model_data.id
        # data['title'] = model_data.title
        # data['content'] = model_data.content
        # data['price'] = model_data.price
        data = model_to_dict(model_data)
    # return JsonResponse(data)
    return Response(data)


# def api_home(request, *args, **kwargs):
#     # request -> HttpRequest -> Django
#     # print(dir(request))
#     # request.body
#     print(request.GET)  # url query params
#     body = request.body  # bytw string of JSON data
#     data = {}
#     try:
#         data = json.loads(body)  # string of JSON data -> Python Dict
#     except:
#         pass
#     print(data)
#     data['params'] = dict(request.GET)  # request.META ->
#     data['headers'] = dict(request.headers)  # request.META ->

#     data['content_type'] = request.content_type  # request.
#     return JsonResponse(data)
