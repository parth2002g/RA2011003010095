# train_schedule/views.py

import requests
from django.http import JsonResponse
from django.db.models import F
from datetime import datetime, timedelta
from .models import Train
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import CompanyRegistration
from .serializers import CompanyRegistrationSerializer

# train_schedule/views.py




def get_authorization_token(request):
    # Define the URL for the John Doe Railway Server authorization endpoint
    authorization_url = "http://20.244.56.144/train/auth"

    # Define the request data
    request_data = {
        "companyName": "Train Central",
        "clientID": "b46118f0-fbde-4b16-a4b1-6ae6ad718b27",
        "ownerName": "Rahul",
        "ownerEmail": "rahul@abc.edu",
        "rollNo": "1",
        "clientSecret": "XOyolORPasKWOdAN"
    }

    try:
        # Make a POST request to the authorization endpoint
        response = requests.post(authorization_url, json=request_data)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            data = response.json()
            return JsonResponse(data, status=status.HTTP_200_OK)
        else:
            # Handle other response codes if needed
            return Response("Authorization failed", status=response.status_code)
    except Exception as e:
        # Handle exceptions if the request fails
        return Response("Authorization request failed", status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def get_train_schedule(request):
    now = datetime.now()
    end_time = now + timedelta(hours=12)
    trains = Train.objects.filter(
        departure_time__gte=now,
        departure_time__lte=end_time,
        departure_time__gt=F('departure_time') + timedelta(minutes=30)
    ).order_by('sleeper_price', '-sleeper_seats_available', '-departure_time')

    data = []
    for train in trains:
        data.append({
            'name': train.name,
            'departure_time': train.departure_time.strftime('%Y-%m-%d %H:%M:%S'),
            'delay_minutes': train.delay_minutes,
            'sleeper_price': train.sleeper_price,
            'ac_price': train.ac_price,
            'sleeper_seats_available': train.sleeper_seats_available,
            'ac_seats_available': train.ac_seats_available,
        })

    return JsonResponse({'trains': data})



@api_view(['POST'])
def register_company(request):
    serializer = CompanyRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()  # Save the registration details
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

