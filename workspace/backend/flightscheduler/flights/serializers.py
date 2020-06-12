from django.contrib.auth.models import User
from flights.models import Schedule
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer) :
    class Meta:
        model = User
        fields = ('url', 'username', 'email')

class ScheduleSerializer(serializers.HyperlinkedModelSerializer) :
    class Meta:
        model = Schedule
        fields = (
            'airline',
            'flight_no',
            'trip_type',
            'departure_airport',
            'arrival_airport',
            'departure_date',
            'return_date'
            )
