# myapp/views.py
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.mail import send_mail
from .serializers import ContactSerializer

@api_view(['POST'])
def contact_form(request):
    serializer = ContactSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

        subject = 'New Contact Form Submission'
        message = f'Name: {serializer.data["fullname"]} {serializer.data["phonenumber"]}\nEmail: {serializer.data["email"]}\nMessage: {serializer.data["message"]}'
        send_mail(subject, message, 'aravintharavinth6369@gmail.com', ['aravintharavinth6369@gmail.com'], fail_silently=False)

        return Response({'message': 'Form submitted successfully'})
    return Response(serializer.errors, status=400)


