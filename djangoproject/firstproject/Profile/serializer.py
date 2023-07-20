from .models import Userprofile,Address_details

from rest_framework import serializers

class Userprofileserializer(serializers.ModelSerializer):
    class Meta:
        model = Userprofile
        fields = "__all__"
# Serializers define the API representation.

class Address_detailsserializer(serializers.ModelSerializer):
    user=Userprofileserializer()
    class Meta:
        model = Address_details
        fields = "__all__"

