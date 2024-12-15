from django.shortcuts import redirect, render

# Create your views here.
from rest_framework.views import APIView

from django.http import HttpResponse, JsonResponse

from rest_framework import generics, status
from rest_framework.response import Response
import random, string

from list.models import Url

class UrlShortCreateView(APIView):
    
    def generate_random_string(self,length=6):
        characters = string.ascii_letters + string.digits
        random_string = ''.join(random.choice(characters) for _ in range(length))
        return random_string
    
    def post(self, request, *args, **kwargs):
        try:
            url = self.request.data.get("url")
            
            if not url:
                return Response({"Url is empty",status.HTTP_400_BAD_REQUEST})
            # random_url = self.generate_random_string()
            random_url = self.generate_random_string(length=8)
            Url.objects.create(original_url = url,short_url=random_url)
            random_url = f"http://localhost:8000/api/redirect/{random_url}"
            print(random_url)
            return Response({"shortUrl": random_url})
        except Exception as e:
            print(e)
            import traceback
            traceback.print_exc()
            return Response("Short URL not found", status=404)
            
class UrlRedirectView(APIView):
    
     def get(self, request, short_url, *args, **kwargs):
        try:
            url_mapping = Url.objects.get(short_url=short_url)
            original_url = url_mapping.original_url
            return redirect(original_url) 
        except Url.DoesNotExist:
            return HttpResponse("Short URL not found", status=404)