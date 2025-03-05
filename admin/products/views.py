from django.shortcuts import render
from rest_framework import viewsets, status
from .models import Products, User
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from .producer import publish, publish_to_main
import random
# Create your views here.

class ProductViewSet(viewsets.ViewSet):
  def list(self, request): # GET api/products
    products = Products.objects.all()
    serializer = ProductSerializer(products, many=True)
    publish()
    publish_to_main()
    return Response(serializer.data)

  def create(self, request): # POST api/products
    serializer = ProductSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)

  def retrieve(self, request, pk=None): # GET api/products/:id
    try:
      product = Products.objects.get(id=pk)
      serializer = ProductSerializer(product)
      return Response(serializer.data)
    except Products.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)

  def update(self, request, pk=None): # PUT api/products/:id
    product = Products.objects.get(id=pk)
    serializer = ProductSerializer(instance=product, data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

  def destroy(self, request, pk=None): # DELETE api/products/:id
    product = Products.objects.get(id=pk)
    product.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

class UserAPIView(APIView):
  def get(self, request):
    users = User.objects.all()
    user = random.choice(users)
    return Response({"id": user.id})
