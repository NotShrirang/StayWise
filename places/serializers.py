from rest_framework import serializers
from places.models import Place, Views, PlaceImage


class ViewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Views
        fields = ['id', 'name']

class PlaceSerializer(serializers.ModelSerializer):
    views = ViewsSerializer(many=True, read_only=True)
    owner_name = serializers.SerializerMethodField()
    owner_email = serializers.SerializerMethodField()
    owner_profilePicture = serializers.SerializerMethodField()
    owner_phoneNumber = serializers.SerializerMethodField()
    class Meta:
        model = Place
        fields = ['id', 'name', 'description', 'owner', 'owner_name', 
                  'owner_email', 'owner_profilePicture', 'owner_phoneNumber',
                  'display_image', 'address', 'city', 'price',
                  'rating', 'guest_capacity', 'bedrooms', 'beds',
                  'bathrooms', 'views', 'has_wifi', 'has_tv',
                  'is_available', 'is_self_check_in', 'is_pet_friendly',
                  'createdAt', 'updatedAt']

    def get_owner_name(self, obj):
        return obj.owner.firstName + ' ' + obj.owner.lastName
    
    def get_owner_email(self, obj):
        return obj.owner.email
    
    def get_owner_profilePicture(self, obj):
        return obj.owner.profilePicture
    
    def get_owner_phoneNumber(self, obj):
        return obj.owner.phoneNumber


class PlaceImageSerializer(serializers.ModelSerializer):
    placeName = serializers.SerializerMethodField()
    uploaderName = serializers.SerializerMethodField()

    class Meta:
        model = PlaceImage
        fields = ['id', 'image', 'place', 'placeName', 'uploader', 'uploaderName', 'createdAt', 'updatedAt']

    def get_placeName(self, obj):
        return obj.place.name
    
    def get_uploaderName(self, obj):
        return obj.uploader.firstName + " " + obj.uploader.lastName
