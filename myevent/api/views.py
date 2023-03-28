from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from api.serializers import CategorySerializer, CountrySerializer, CitySerializer, EventSerializer, TicketSerializer, RegistrationSerializer, PaymentSerializer
from api.models import Category, Country, City, Event, Ticket, Registration, Payment


class CategoryViewSet(ViewSet):
    
    def list(LoginRequiredMixin,self, request):
        queryset = Category.objects.order_by('pk')
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)
 
    def create(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = Category.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = CategorySerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response(status=404)
        serializer = CategorySerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class CountryViewSet(ViewSet):

    def list(self, request):
        queryset = Country.objects.order_by('pk')
        serializer = CountrySerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = CountrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = Country.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = CountrySerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = Country.objects.get(pk=pk)
        except Country.DoesNotExist:
            return Response(status=404)
        serializer = CountrySerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = Country.objects.get(pk=pk)
        except Country.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class CityViewSet(ViewSet):

    def list(self, request):
        queryset = City.objects.order_by('pk')
        serializer = CitySerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = CitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = City.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = CitySerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = City.objects.get(pk=pk)
        except City.DoesNotExist:
            return Response(status=404)
        serializer = CitySerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = City.objects.get(pk=pk)
        except City.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class EventViewSet(ViewSet):

    def list(self, request):
        queryset = Event.objects.order_by('pk')
        serializer = EventSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = Event.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = EventSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            return Response(status=404)
        serializer = EventSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class TicketViewSet(ViewSet):

    def list(self, request):
        queryset = Ticket.objects.order_by('pk')
        serializer = TicketSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = TicketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = Ticket.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = TicketSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = Ticket.objects.get(pk=pk)
        except Ticket.DoesNotExist:
            return Response(status=404)
        serializer = TicketSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = Ticket.objects.get(pk=pk)
        except Ticket.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class RegistrationViewSet(ViewSet):

    def list(self, request):
        queryset = Registration.objects.order_by('pk')
        serializer = RegistrationSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = Registration.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = RegistrationSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = Registration.objects.get(pk=pk)
        except Registration.DoesNotExist:
            return Response(status=404)
        serializer = RegistrationSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = Registration.objects.get(pk=pk)
        except Registration.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class PaymentViewSet(ViewSet):

    def list(self, request):
        queryset = Payment.objects.order_by('pk')
        serializer = PaymentSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = Payment.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = PaymentSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = Payment.objects.get(pk=pk)
        except Payment.DoesNotExist:
            return Response(status=404)
        serializer = PaymentSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = Payment.objects.get(pk=pk)
        except Payment.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)
