from rest_framework import serializers

from notes.models import Note, Book, Tag
from accounts.models import User


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)

    def create(self, validated_data):
        user = User.objects._create_user(validated_data['email'], validated_data['password'])
        return user

    class Meta:
        model = User
        fields = ('id', 'email', 'password')
        read_only_fields = ('id',)
        extra_kwargs = {
            'password': {'write_only': True}
        }


class NoteSerializer(serializers.ModelSerializer):

    owner = UserSerializer(many=False, read_only=True)
    last_editor = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Note
        fields = ('id', 'title', 'body', 'pub_date', 'tags', 'book', 'owner', 'editors', 'viewers','last_editor')
        read_only_fields = ('id', 'pub_date', 'owner', 'last_editor')



class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'body')
        read_only_fields = ('id',)



class BookSerializer(serializers.ModelSerializer):
    owner = UserSerializer(many=False, read_only=True)
    notes = NoteSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = ('id', 'owner', 'title', 'description', 'notes')
        read_only_fields = ('id', 'owner',)