from django.contrib.auth.models import User
from rest_framework import serializers
from taxrisk.models import BzEntity


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('url', 'id', 'username')

    def __unicode__(self):
        return '%s' % self.username


class BzEntitySerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.StringRelatedField(many=False)

    class Meta:
        model = BzEntity
        fields = ('id','created_date', 'author')