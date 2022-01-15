from django.urls import path, include
from  rest_framework.routers import DefaultRouter
from watchlist_app.api.views import (ReviewList, ReviewDetail, WatchListAV,
                                     StreamPlatformAV, WatchDetailsAV,
                                     StreamPlatformDetailsAV, ReviewCreate,
                                     StreamPlatformVS, UserReviewList, WatchList1)

router = DefaultRouter()
router.register('stream', StreamPlatformVS, basename='streamplatform')


urlpatterns = [
    path('', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>/', WatchDetailsAV.as_view(), name='movie-detail'),
    path('list-new/', WatchList1.as_view(), name='movie-detail'),

    path('', include(router.urls)),
    # path('stream/', StreamPlatformAV.as_view(), name='stream'),
    # path('stream/<int:pk>', StreamPlatformDetailsAV.as_view(), name='stream-detail'),

    # path('review/', ReviewList.as_view(), name='review-list'),
    # path('review/<int:pk>', ReviewDetail.as_view(), name='review-detail'),

    path('<int:pk>/review-create/', ReviewCreate.as_view(), name='stream-review'),
    path('<int:pk>/review/', ReviewList.as_view(), name='stream-review'),
    path('review/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),

    # path('review/<str:username>/', UserReviewList.as_view(), name='user-review-detail'),
    path('review/', UserReviewList.as_view(), name='user-review-detail'),
]
