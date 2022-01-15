from rest_framework import serializers
from watchlist_app.models import StreamPlatform, WatchList, Review


class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        # fields = '__all__'
        exclude = ['watchlist']


class WatchListSerializer(serializers.ModelSerializer):
    # reviews = ReviewSerializer(many=True, read_only=True)
    platform = serializers.CharField(source='platform.name')

    class Meta:
        model = WatchList
        fields = "__all__"


class StreamPlatformSerializer(serializers.ModelSerializer):
    """The name watchlist should be same as the name in the models file's watchlist class
    with the name as related field."""
    # watchlist = WatchListSerializer(many=True, read_only=True)
    # watchlist = serializers.StringRelatedField(many=True)
    watchlist = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # watchlist = TrackSerializer(many=True, read_only=True)

    class Meta:
        model = StreamPlatform
        fields = "__all__"
