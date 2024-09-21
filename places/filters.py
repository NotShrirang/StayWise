from  utils.filters import DateFilter

from .models import Place, PlaceImage, Views


class PlaceFilter(DateFilter):
    class Meta:
        model = Place
        fields = (
            'createdAt',
            'updatedAt',
            'city',
            'rating',
            'guest_capacity',
            'bedrooms',
            'beds',
            'bathrooms',
            'has_wifi',
            'has_tv',
            'is_available',
            'is_self_check_in',
            'is_pet_friendly',
        )


class PlaceImageFilter(DateFilter):
    class Meta:
        model = PlaceImage
        fields = (
            'createdAt',
            'updatedAt',
            'place',
        )