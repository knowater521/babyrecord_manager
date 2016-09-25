from rest_framework import serializers, viewsets, permissions
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response


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

    @list_route(methods=['post'])
    def setpeedata(self, request):
        record_date = request.data['record_date'];
        pee_type = request.data['pee_type'];
        amount = request.data['amount'];

        # 先检查该日是否已经有了
        li = Pee.objects.filter(record_date=record_date, pee_type=pee_type)

        if len(li) == 0:
            obj = Pee.objects.create(
                record_date=record_date,
                pee_type=pee_type,
                amount=amount
            );
        else:
            obj = li[0]
            obj.amount = amount;
            obj.save();

        return Response({'amount': str(amount)})


    @list_route(methods=['get'])
    def getpeedata(self, request):
        record_date = request.query_params['record_date'];
        pee_type = request.query_params['pee_type'];
        # 先检查该日是否已经有了
        li = Pee.objects.filter(record_date=record_date, pee_type=pee_type)

        amount = 0;
        if len(li) > 0:
            obj = li[0]
            amount = obj.amount

        return Response({'amount': str(amount)})


class BreastBumpSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BreastBump
        fields = ('id', 'bump_at', 'amount', 'record_at')


class BreastBumpViewSet(viewsets.ModelViewSet):
    queryset = BreastBump.objects.all()

    serializer_class = BreastBumpSerializer
    permission_classes = (permissions.AllowAny,)
