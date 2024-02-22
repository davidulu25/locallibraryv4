from django.shortcuts import render

from rest_framework import generics, authentication, permissions
from rest_framework.response import Response

from .models import Author
from .serializers import AuthorSerializer

class AuthorSingularView(generics.CreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        author_id = self.request.query_params.get("id")
        author = Author.objects.get(id=author_id)
        return author
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        if self.request.query_params.get("id"):
            return self.retrieve(request, *args, **kwargs)
        else:
            return self.create(request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
        if self.request.query_params.get("id"):
            return self.update(request, *args, **kwargs)
        else:
            return self.create(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        if self.request.query_params.get("id"):
            return self.destroy(request, *args, **kwargs)
        else:
            return self.create(request, *args, **kwargs)

class AuthorListView(generics.ListAPIView, generics.CreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    # function to override deleting single model instance
    def destroy(self, request, *args, **kwargs):
        queryset = Author.objects.all()
        respite, _ = queryset.delete()
        return Response({"message": f"all author profiles ({respite}) were deleted"})

    def get(self, request, *args, **kwargs):
        if self.get_queryset() is None:
            return self.create(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
        if self.get_queryset() is None:
            return self.create(request, *args, **kwargs)
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        if self.get_queryset() is None:
            return self.create(request, *args, **kwargs)
        return self.destroy(request, *args, **kwargs)