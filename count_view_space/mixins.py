from rest_framework.response import Response

class CountMixin:
    def get(self, request):
        count=self.get_queryset().count()
        return Response(count)