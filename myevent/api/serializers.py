from rest_framework.serializers import ModelSerializer
from api.models import Category, Country, City, Event, Ticket, Registration, Payment


class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class CountrySerializer(ModelSerializer):

    class Meta:
        model = Country
        fields = '__all__'


class CitySerializer(ModelSerializer):

    class Meta:
        model = City
        fields = '__all__'


class EventSerializer(ModelSerializer):

    class Meta:
        model = Event
        fields = '__all__'


class TicketSerializer(ModelSerializer):

    class Meta:
        model = Ticket
        fields = '__all__'


class RegistrationSerializer(ModelSerializer):

    class Meta:
        model = Registration
        fields = '__all__'


class PaymentSerializer(ModelSerializer):

    class Meta:
        model = Payment
        fields = '__all__'
