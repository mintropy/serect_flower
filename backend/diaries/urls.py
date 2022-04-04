from django.urls import path

from .views.diary import DiaryViewSet
from .views.flower import FlowerViewSet


diary_list = DiaryViewSet.as_view(
    {
        "post": "create",
    }
)
diary_montly = DiaryViewSet.as_view({"get": "montly"})
diary_daily = DiaryViewSet.as_view(
    {
        "get": "daily",
        "put": "update",
        "delete": "destroy",
    }
)
nltk_download = DiaryViewSet.as_view({'get': 'nltk_download'})
flower_list = FlowerViewSet.as_view({"get": "list"})
flower_detail = FlowerViewSet.as_view({"get": "retrieve"})
flower_user = FlowerViewSet.as_view({"get": "user"})

urlpatterns = [
    path("nltk-download/", nltk_download),
    path("", diary_list, name="diary_list"),
    path("<int:year>/<int:month>/", diary_montly),
    path("<int:year>/<int:month>/<int:day>/", diary_daily),
    path("flowers/", flower_list),
    path("flowers/user/", flower_user),
    path("flowers/<int:flower_id>/", flower_detail),
]
