from rest_framework import serializers

class WordsCountSerializer(serializers.Serializer):
    word = serializers.CharField(max_length=20)
    cont = serializers.IntegerField()
