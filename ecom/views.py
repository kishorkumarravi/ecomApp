from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
import json
import logging
import random
from random import randint

from ecom.models import Registration2, Items, OrderHistory
from ecom.serializers import RegistrationSerializer, ItemsSerializer, OrderHistorySerializer
from ecom.db_utils import create_user, create_items, create_history

@api_view(['GET'])
def about(request):
    return Response({"message": "About page"})

@api_view(['POST'])
def signup(request):
    try:
        json_req = request.data
        emailId = json_req['emailId']
        reg = Registration2.objects.all()
        if reg is not None:
            reg = reg.filter(emailId=emailId)
        reg_serializer = RegistrationSerializer(reg, many=True)
        db_data = reg_serializer.data
        print(db_data)
        if len(db_data) > 0:
            data = {"message":"User already registered"}
            return JsonResponse(data)    

        tran_serializer = create_user(json_req)
        data = {"message":"User added succesfully"}
        return JsonResponse(data)
    except Exception as err:
        logging.error(f'err : {err}')
        return JsonResponse("Failed to add record")

@api_view(['GET'])
def users_list(request):
    try:
        reg = Registration2.objects.all()
        reg_serializer = RegistrationSerializer(reg, many=True)
        data = {"data" : reg_serializer.data, "size": len(reg_serializer.data) }
        return JsonResponse(data=data, safe=False)

    except Exception as err:
        logging.error(f'err : {err}')
        return JsonResponse("Failed to get users")

@api_view(['POST'])
def add_items(request):
    try:
        json_req = request.data
        tran_serializer = create_items(json_req)
        data = {"message":"Item added succesfully"}
        return JsonResponse(data)
    except Exception as err:
        logging.error(f'err : {err}')
        return JsonResponse("Failed to add Item")

@api_view(['GET'])
def item_list(request):
    try:
        items = Items.objects.all()
        item_serializer = ItemsSerializer(items, many=True)
        data = {"data" : item_serializer.data, "size": len(item_serializer.data) }
        return JsonResponse(data=data, safe=False)

    except Exception as err:
        logging.error(f'err : {err}')
        return JsonResponse("Failed to get items")

@api_view(['POST'])
def order_items(request):
    try:
        json_req = request.data
        tran_serializer = create_history(json_req)
        data = {"message":"Ordered succesfully"}
        return JsonResponse(data)
    except Exception as err:
        logging.error(f'err : {err}')
        return JsonResponse("Failed to Order Item")

@api_view(['GET'])
def order_history(request):
    try:
        emailId = request.GET.get('emailId', None)
        orders = OrderHistory.objects.all()
        if orders is not None:
            orders = orders.filter(emailId=emailId)

        order_serializer = OrderHistorySerializer(orders, many=True)
        data = {"data" : order_serializer.data, "size": len(order_serializer.data) }
        return JsonResponse(data=data, safe=False)

    except Exception as err:
        logging.error(f'err : {err}')
        return JsonResponse("Failed to get orders")

@api_view(['POST'])
def applogin(request):
    try:
        json_req = request.data
        emailId = json_req['emailId']
        password = json_req['password']
        
        reg = Registration2.objects.all()
        if reg is not None:
            reg = reg.filter(emailId=emailId)
        reg_serializer = RegistrationSerializer(reg, many=True)
        db_data = reg_serializer.data
        if len(db_data) > 0:
            actPass = db_data[0]['password']
            print(actPass)
            if actPass == password:
                data = 'Login succesful'
            else:
                data = 'Login failed'
        else:
            data = 'User not found'

        return JsonResponse({"message":data})

    except Exception as err:
        logging.error(f'err : {err}')
        return JsonResponse("Failed to get orders")