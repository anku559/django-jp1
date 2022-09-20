from django.core.exceptions import ObjectDoesNotExist
from django.utils.decorators import method_decorator
from django.db.models import Q, F
from django.forms.models import model_to_dict
from django.http import request, JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from store.models import Product
import json
from django.views.generic import View


@method_decorator(csrf_exempt, name="dispatch")
class ProductRouteManager(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("This is GET request")

    def post(self, request, *args, **kwargs):
        return HttpResponse("This is POST request")

    def put(self, request, *args, **kwargs):
        return HttpResponse("This is PUT request")

    def patch(self, request, *args, **kwargs):
        return HttpResponse("This is PATCH request")

    def delete(self, request, *args, **kwargs):
        return HttpResponse("This is DELETE request")


def create_product(req: request):
    new_product = Product.save()

    return HttpResponse("Product created successfully.")


def fetch_products(req: request):
    try:
        product_list = Product.objects.values("title", "id", "collection__title")

        return JsonResponse({"status": 200, "data": list(product_list)})

        # return render(
        #     req, "filtered-products.html", {"products": products_greater_than}
        # )

    except ObjectDoesNotExist:
        return HttpResponse("Product with id not exists.")


# exists = Product.objects.filter(id=1).exists()
# single_product = Product.objects.get(id=1)
# print(json.dumps(single_product))
# print(type(single_product))
# products = Product.objects.all()
# product_count = Product.objects.count()
# return JsonResponse(
#     {
#         "code": 200,
#         "info": "OK",
#         "status": True,
#         "message": "Products fetched successfully.",
#         "data_count": product_count,
#         # "data": products,
#     }
# )
