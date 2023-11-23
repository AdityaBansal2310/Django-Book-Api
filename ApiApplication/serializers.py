from rest_framework import serializers

class BookSerializer(serializers.Serializer):
     id = serializers.IntegerField(label = "Enter Book ID")
     title = serializers.CharField(label = "Enter Book Title")
     author = serializers.CharField(label = "Enter Book author")