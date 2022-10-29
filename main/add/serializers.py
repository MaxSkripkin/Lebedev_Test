from rest_framework import serializers

from add.models import Putin_order


class PutinOrderSerializer(serializers.ModelSerializer):
    """
    Сериализуем данные
    """
    class Meta:
        model = Putin_order
        fields = '__all__'
