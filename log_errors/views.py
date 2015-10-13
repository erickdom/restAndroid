from django.http.response import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from log_errors.models import Log_Errors
from log_errors.serializers import Log_ErrorsSerialize


class Log_ErrosREST(APIView):

    def get_object(self, pk):
        try:
            return Log_Errors.objects.get(pk=pk)
        except Log_Errors.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        transactions = Log_Errors.objects.all()
        serializer = Log_ErrorsSerialize(transactions, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = Log_ErrorsSerialize(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





