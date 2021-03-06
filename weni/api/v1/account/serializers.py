from django.conf import settings
from django.contrib.auth.password_validation import validate_password
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers

from weni.api.v1.fields import PasswordField
from weni.authentication.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "first_name", "last_name", "photo"]
        ref_name = None

    id = serializers.IntegerField(label=_("ID"), read_only=True)
    username = serializers.CharField(label=_("Username"), read_only=True)
    email = serializers.EmailField(label=_("Email"), read_only=True)
    photo = serializers.ImageField(label=_("User photo"), read_only=True)


class UserPhotoSerializer(serializers.Serializer):
    file = serializers.FileField(required=True)


class ChangePasswordSerializer(serializers.Serializer):
    password = PasswordField(
        write_only=True, validators=[validate_password], label=_("Password")
    )


class ChangeLanguageSerializer(serializers.Serializer):
    language = serializers.ChoiceField(settings.LANGUAGES, label=_("Language"))
