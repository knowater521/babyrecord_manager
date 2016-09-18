from rest_framework import serializers, viewsets, permissions

from babydata.models import *


class DrinkMilkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DrinkMilk
        fields = ('id', 'drink_at', 'amount', 'drink_type', 'record_at')


class DrinkMilkViewSet(viewsets.ModelViewSet):
    queryset = DrinkMilk.objects.all()

    serializer_class = DrinkMilkSerializer


class SleepSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sleep
        fields = ('id', 'sleep_start', 'sleep_end', 'record_at')


class SleepViewSet(viewsets.ModelViewSet):
    queryset = Sleep.objects.all()

    serializer_class = SleepSerializer


class PeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pee
        fields = ('id', 'record_date', 'pee_type', 'amount', 'record_at')


class PeeViewSet(viewsets.ModelViewSet):
    queryset = Pee.objects.all()

    serializer_class = PeeSerializer


class BreastBumpSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BreastBump
        fields = ('id', 'bump_at', 'amount', 'record_at')


class BreastBumpViewSet(viewsets.ModelViewSet):
    queryset = BreastBump.objects.all()

    serializer_class = BreastBumpSerializer
    permission_classes = (permissions.AllowAny,)
