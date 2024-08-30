from rest_framework import serializers
from .models import Country, State, City


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = (
            "id",
            "createdAt",
            "updatedAt",
            "name",
        )
        get_fields = fields
        list_fields = fields


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = (
            "id",
            "createdAt",
            "updatedAt",
            "name",
            "country",
        )
        list_fields = fields
        get_fields = fields


class CitySerializer(serializers.ModelSerializer):
    cityName = serializers.SerializerMethodField()
    state = serializers.SerializerMethodField()
    stateName = serializers.SerializerMethodField()
    country = serializers.SerializerMethodField()
    countryName = serializers.SerializerMethodField()

    class Meta:
        model = City
        fields = (
            "id",
            "createdAt",
            "updatedAt",
            "name",
            "cityName",
            "state",
            "stateName",
            "country",
            "countryName",
        )
        list_fields = fields
        get_fields = fields

    def get_cityName(self, instance):
        return instance.name + ", " + instance.state.name + ", " + instance.state.country.name

    def get_state(self, instance):
        return instance.state.id

    def get_stateName(self, instance):
        return instance.state.name + ", " + instance.state.country.name

    def get_country(self, instance):
        return instance.state.country.id

    def get_countryName(self, instance):
        return instance.state.country.name