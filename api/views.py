
from rest_framework.response import Response

from .models import Article
from .serializers import ArticleSerializers

from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404

# Create your views here.

@api_view(["GET", "POST"])
def article_view(request, pk=None, *args, **kwargs):
    method = request.method

    if method == "GET":
        if pk is not None:
            obj = get_object_or_404(Article, pk=pk)
            data = ArticleSerializers(obj, many=False).data
            return Response(data)

        queryset = Article.objects.all()  
        data = ArticleSerializers(queryset, many=True).data
        return Response(data)  

    if method == "POST":

        serializer = ArticleSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({"invalid": "not good data"}, status=400)    


