from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Item
from .serializers import ItemSerialier


@api_view(['GET'])
def getData(request):
    items = Item.objects.all()
    serializer = ItemSerialier(items, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addData(request):
    serializer = ItemSerialier(data=request.data)
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)






