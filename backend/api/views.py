from django.http import JsonResponse
import json
from django.forms.models import model_to_dict
from products.models import Product

from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.serializers import ProductSerializer
# Create your views here.


@api_view(["GET"])
def api_home(request, *args, **kwargs):
    """
    DRF API View
    """
    instance = Product.objects.all().order_by("?").first()
    data = {}
    if instance:

        data = ProductSerializer(instance).data
    # return JsonResponse(data)
    return Response(data)


@api_view(["POST"])
def api_home(request, *args, **kwargs):
    """
    DRF API View
    """
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        instance = serializer.save()
        print(instance)
        return Response(serializer.data)
    return Response({"Invalid": "no good data"}, status=400)


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

    # data['id'] = model_data.id
    # data['title'] = model_data.title
    # data['content'] = model_data.content
    # data['price'] = model_data.price
    # data = model_to_dict(instance, fields=[
    #    'id', 'title', 'price', 'sale_price'])
