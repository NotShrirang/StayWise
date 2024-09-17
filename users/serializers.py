from users.models import StayWiseUser, ReservationUser
import requests
from django.contrib import auth
from django.contrib.auth.password_validation import validate_password
from rest_framework.serializers import ModelSerializer, CharField, SerializerMethodField, Serializer, ValidationError
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken, TokenError


class ReservationUserSerializer(ModelSerializer):
    userName = SerializerMethodField()
    reservationPlace = SerializerMethodField()
    reservationStartDate = SerializerMethodField()
    reservationEndDate = SerializerMethodField()

    class Meta:
        model = ReservationUser
        fields = ['id', 'user', 'reservation', 'userType', 'registerdAt', 'userName', 'reservationPlace', 'reservationStartDate', 'reservationEndDate']


    def get_userName(self, obj):
        return obj.user.firstName + " " + obj.user.lastName
    
    def get_reservationPlace(self, obj):
        return obj.reservation.place.name
    
    def get_reservationStartDate(self, obj):
        return obj.reservation.start_datetime
    
    def get_reservationEndDate(self, obj):
        return obj.reservation.end_datetime
    


class StayWiseUserSerializer(ModelSerializer):
    cityName = SerializerMethodField()

    class Meta:
        model = StayWiseUser
        fields = ['id', 'email', 'firstName', 'lastName', 'gender', 'dateOfBirth', 'city', 'phoneNumber', 'profilePicture', 'cityName']
        list_fields = fields
        get_fields = fields

    def get_cityName(self, obj):
        if obj.city:
            return f"{obj.city.name}, {obj.city.state.name}, {obj.city.state.country.name}"
        return None


class RegisterSerializer(ModelSerializer):
    password = CharField(min_length=8, write_only=True)

    class Meta:
        model = StayWiseUser
        fields = ['email', 'password', 'firstName',
                  'lastName', 'dateOfBirth', 'phoneNumber', 'city']

    def create(self, validated_data):
        return StayWiseUser.objects.create_user(**validated_data)


class RegisterGoogleSerializer(ModelSerializer):
    token = CharField(required=True)

    class Meta:
        model = StayWiseUser
        fields = (
            'token',
        )

    def validate(self, data):
        """
        Check if the user exists.
        """
        url = f"https://www.googleapis.com/oauth2/v1/tokeninfo?access_token={data['token']}"
        response = requests.get(url)
        if (response.status_code == 200):
            response_body = response.json()
            email = response_body["email"]
            user = StayWiseUser.objects.filter(email=email)
            if user.exists():
                raise ValidationError(
                    f"User with email {email} already exists")
            data['email'] = email
            return data
        raise ValidationError('invalid token')

    def create(self, validated_data):
        validated_data['is_active'] = True
        validated_data['signInMethod'] = "Google"
        validated_data['isVerified'] = False
        del validated_data['token']
        user = StayWiseUser.objects.create(**validated_data)
        user.save()
        return user


class LoginSerializer(ModelSerializer):
    password = CharField(min_length=6, write_only=True)
    email = CharField(max_length=255)
    tokens = SerializerMethodField()

    def get_tokens(self, obj):
        user = StayWiseUser.objects.get(email=obj['email'])
        return {
            'refresh': user.tokens()['refresh'],
            'access': user.tokens()['access']
        }

    class Meta:
        model = StayWiseUser
        fields = ['email', 'password', 'tokens']

    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')
        user = auth.authenticate(email=email, password=password)
        if not user:
            raise AuthenticationFailed('Invalid credentials, try again')
        if not user.is_active:
            raise AuthenticationFailed('Account disabled, contact admin')
        if not user.isVerified:
            raise AuthenticationFailed(
                'Account not verified, verify your email.')
        return {
            'email': user.email,
            'tokens': user.tokens
        }


class GoogleLoginSerializer(ModelSerializer):
    accessToken = CharField(write_only=True, required=True)

    class Meta:
        model = StayWiseUser
        fields = (
            'accessToken',
        )

    def validate(self, data):
        """
        Check if the user exists.
        """
        url = f"https://www.googleapis.com/oauth2/v1/tokeninfo?access_token={data['accessToken']}"
        response = requests.get(url)
        if (response.status_code == 200):
            response_body = response.json()
            email = response_body["email"]
            user = StayWiseUser.objects.filter(email=email)
            if not user.exists():
                raise ValidationError(
                    f"User with email {email} does not exist")
            if not user.first().is_active:
                raise ValidationError(f"User with email {email} is inactive")
            token = RefreshToken.for_user(user.first())
            data = dict()
            data['refresh'] = str(token)
            data['access'] = str(token.access_token)
            return data
        else:
            raise ValidationError('invalid token')


class LogoutSerializer(Serializer):
    refresh = CharField()

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail('bad_token')


class UpdatePasswordSerializer(ModelSerializer):
    password = CharField(write_only=True, required=True,
                         validators=[validate_password])
    confirmPassword = CharField(write_only=True, required=True)
    oldPassword = CharField(write_only=True, required=True)

    class Meta:
        model = StayWiseUser
        fields = ('oldPassword', 'password', 'confirmPassword')

    def validate(self, attrs):
        if attrs['password'] != attrs['confirmPassword']:
            raise ValidationError(
                {"password": "Password fields didn't match."})
        return attrs

    def validate_oldPassword(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise ValidationError(
                {"oldPassword": "Old password is not correct"})
        return value

    def update(self, instance, validated_data):
        user = self.context['request'].user
        if user.pk != instance.pk:
            raise ValidationError(
                {"authorize": "You dont have permission for this user."})

        instance.set_password(validated_data['password'])
        instance.save()
        return instance