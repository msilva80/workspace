from django.contrib.auth.models import User

#for the RESTful API
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
#from django.http import HttpResponse
#from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from webapp.serializers import MobileSerializer
from django.http import Http404
from rest_framework.views import APIView
#from rest_framework import status
#
"mixins and generics for simpler classes"
#from rest_framework import mixins
#from rest_framework import generics
#END OF RESTFUL API
class UserDetail(APIView):
          
    """
    Retrieve, update or delete a report.
    """
  

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except Report.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        report = self.get_object(pk)
        serializer = MobileSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        report = self.get_object(pk)
        serializer = MobileSerializer(snippet, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        report = self.get_object(pk)
        report.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
#we comment this class out, since we have simplified it below using generics
class UserList(APIView):
    """
    List all code reports, or create a new report.
    """
    
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = MobileSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MobileSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)