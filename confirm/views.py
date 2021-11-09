from  rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime

@api_view(['GET'])
def index(request):
    data = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    msg = 'server is live : '
    return Response ( data=msg+data , status=status.HTTP_200_OK)