from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from .models import Merchant, Stores, Items
from .seralizers import MerchantSerializer, StoresSerializer, ItemsSerializer


@csrf_exempt
def merchant_list(request):
    if request.method == 'GET':
        queryset = Merchant.objects.all()
        serializer = MerchantSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MerchantSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def merchant_detail(request, pk):
    try:
        merchant = Merchant.objects.get(pk=pk)
    except Merchant.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = MerchantSerializer(merchant)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = MerchantSerializer(merchant, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        merchant.delete()
        return HttpResponse(status=204)


@csrf_exempt
def stores_list(request):
    if request.method == 'GET':
        queryset = Stores.objects.all()
        serializer = StoresSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = StoresSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def stores_detail(request, pk):
    try:
        stores = Stores.objects.get(pk=pk)
    except Stores.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = StoresSerializer(stores)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = StoresSerializer(stores, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        stores.delete()
        return HttpResponse(status=204)


@csrf_exempt
def items_list(request):
    if request.method == 'GET':
        queryset = Items.objects.all()
        serializer = ItemsSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ItemsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def items_detail(request, pk):
    try:
        item = Items.objects.get(pk=pk)
    except Items.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ItemsSerializer(item)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ItemsSerializer(item, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return HttpResponse(status=204)
