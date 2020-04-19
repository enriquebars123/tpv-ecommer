"""Usuario serializers."""


# Django Rest Framework
from rest_framework import serializers
import django_filters

from apps_tpvCommerce.user.models import user
from apps_tpvCommerce.user.models import people

class userSerializers(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True,required=False)

    class Meta:
        model = user
        fields = (
            'id',
            'username',
            'email',
            'name',
            'password',
        )

    def create(self, validated_data):
        user = super(UserSerializers, self).create(
            validated_data
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


    def update(self, instance, validated_data):
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        return super(UserSerializers, self).update(
            instance,
            validated_data,
        )


class peopleSerializers(serializers.ModelSerializer):

    class Meta:
        model = people
        fields = '__all__'