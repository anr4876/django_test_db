from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Post
from .serializers import TestDataSerializer


@api_view(['GET'])
def getTestDatas(request):
    datas = Post.objects.all()
    serializer = TestDataSerializer(datas, many=True)
    return Response(serializer.data)