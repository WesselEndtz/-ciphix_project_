from rest_framework import serializers
from .models import Message

class MessageSerializer(serializers.Serializer):
    message = serializers.ListField(child=serializers.CharField(), allow_empty=True)

    def to_representation(self, instance):
        """
        Serialize the instance.
        """
        return {
            "message": instance.get("message", [])
        }

    def to_internal_value(self, data):
        """
        Deserialize the data and handle both string and list input.
        """
        message = data.get("message")
        if isinstance(message, list):
            # If 'message' is a list, return it as is
            return {"message": message}
        else:
            # If 'message' is a string, return it as a single string
            return {"message": message}
