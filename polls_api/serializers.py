from rest_framework import serializers
from .models import PollDetail

class PollDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PollDetail
        fields = ["poll", "timestamp", "completed",  "updated", "user"]