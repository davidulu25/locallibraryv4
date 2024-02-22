from django.shortcuts import render

from django.contrib.auth.models import User

from rest_framework import generics
from rest_framework.response import Response

from count_view_space.mixins import CountMixin
from bookinstance_model_space.models import BookInstance
from bookinstance_model_space.serializers import BookInstanceSerializer

class BookCountView(generics.GenericAPIView, CountMixin):
    serializer_class = BookInstanceSerializer
    queryset = BookInstance.objects.all()

    def get_queryset(self):
        book_data = self.request.query_params.get("id")
        queryset = BookInstance.objects.filter(book=book_data)
        return queryset
    
    def list(self, request, *args, **kwargs):
        return Response("")

class UserVisitsCountView(generics.GenericAPIView, CountMixin):
    model = User
    
    def get(self, request, *args, **kwargs):
        num_visits = request.session.get("num_visits", 0)
        request.session["num_visits"] = num_visits + 1
        return Response(num_visits)