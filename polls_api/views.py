from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import PollDetail
from .serializers import PollDetailSerializer

class PollDetailListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the poll items for given requested user
        '''
        poll_details = PollDetail.objects.filter(user = request.user.id)
        serializer = PollDetailSerializer(poll_details, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given poll data
        '''
        data = {
            'poll': request.data.get('poll'), 
            'completed': request.data.get('completed'), 
            'user': request.user.id
        }
        serializer = PollDetailSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class PollDetailApiViewId(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, poll_id, user_id):
        '''
        Helper method to get the object with given poll_id, and user_id
        '''
        try:
            return PollDetail.objects.get(id=poll_id, user = user_id)
        except PollDetail.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, poll_id, *args, **kwargs):
        '''
        Retrieves the Todo with given poll_id
        '''
        poll_instance = self.get_object(poll_id, request.user.id)
        if not poll_instance:
            return Response(
                {"res": "Object with poll id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = PollDetailSerializer(poll_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, poll_id, *args, **kwargs):
        '''
        Updates the poll item with given poll_id if exists
        '''
        poll_instance = self.get_object(poll_id, request.user.id)
        if not poll_instance:
            return Response(
                {"res": "Object with poll id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'task': request.data.get('task'), 
            'completed': request.data.get('completed'), 
            'user': request.user.id
        }
        serializer = PollDetailSerializer(instance = poll_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, poll_id, *args, **kwargs):
        '''
        Deletes the poll item with given poll_id if exists
        '''
        poll_instance = self.get_object(poll_id, request.user.id)
        if not poll_instance:
            return Response(
                {"res": "Object with poll id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        poll_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )