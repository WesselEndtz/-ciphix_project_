from rest_framework.parsers import JSONParser
from rest_framework import views
from rest_framework.response import Response
from json import JSONDecodeError
from .serializers import MessageSerializer
from .utils.spacy_function import get_sentiment

class SentimentAPIView(views.APIView):
    def post(self, request):
        try:
            data = JSONParser().parse(request)
            serializer = MessageSerializer(data=data)
            
            if serializer.is_valid():
                message_details = serializer.validated_data
                message = str(message_details['message'])
                sentiment = get_sentiment('I am not very happy, but I am also not especially sad')
                # Add extra data to the response
                extra_data = {
                    message: str(sentiment),
                }
                response_data = {**message_details, **extra_data}
                return Response(response_data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except JSONDecodeError:
            return JsonResponse({"result": "error", "message": "JSON decoding error"}, status=400)
