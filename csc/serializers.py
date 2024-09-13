from rest_framework import serializers
from .models import Country, State, City


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = (
            "name",
        )
        get_fields = fields
        list_fields = fields


class StateSerializer(serializers.ModelSerializer):
    countryName = serializers.SerializerMethodField()
    class Meta:
        model = State
        fields = (
            "name",
            "country",
            'countryName',
        )
        list_fields = fields
        get_fields = fields

    def get_countryName(self, instance):
        return instance.country.name


class CitySerializer(serializers.ModelSerializer):
    cityName = serializers.SerializerMethodField()
    state = serializers.SerializerMethodField()
    stateName = serializers.SerializerMethodField()
    country = serializers.SerializerMethodField()
    countryName = serializers.SerializerMethodField()

    class Meta:
        model = City
        fields = (
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
        return instance.state

    def get_stateName(self, instance):
        return instance.state.name + ", " + instance.state.country.name

    def get_country(self, instance):
        return instance.state.country

    def get_countryName(self, instance):
        return instance.state.country.name