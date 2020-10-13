# serializers.py

from rest_framework import serializers

from ecom.models import Registration2, Items, OrderHistory

class RegistrationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Registration2
        fields = ('userName', 'emailId', 'password', 'regType')

class ItemsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Items
        fields = ('itemName', 'itemNo', 'description', 'cost')

class OrderHistorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderHistory
        fields = ('userName', 'emailId', 'itemName', 'itemNo', 'description', 'cost')
