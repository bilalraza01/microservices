from django.shortcuts import render
from rest_framework import viewsets

# Create your views here.

class ProductViewSet(viewsets.ViewSet):
  def list(self, request): # GET api/products
    pass

  def create(self, request): # POST api/products
    pass

  def retrieve(self, request, pk=None): # GET api/products/:id
    pass

  def update(self, request, pk=None): # PUT api/products/:id
    pass

  def partial_update(self, request, pk=None): # PATCH api/products/:id
    pass

  def destroy(self, request, pk=None): # DELETE api/products/:id
    pass
