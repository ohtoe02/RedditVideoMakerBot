from django.urls import path
from .views import SettingsLoaderViewSet
settings_get_and_post = SettingsLoaderViewSet.as_view({
    'get':'list',
    'post':'create'
})
settings_put=SettingsLoaderViewSet.as_view({
    'put':'update'
})
urlpatterns = [
    path('', settings_get_and_post),
    path('<int:pk>', settings_put),
]