from rest_framework import serializers
from .models import Subject

class SubjectModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Subject
        # fields = '__all__'
        exclude = ('slug',)