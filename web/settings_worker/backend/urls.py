from django.urls import path
from .views import SettingsLoaderViewSet, save_to_file,index
settings_get_and_post = SettingsLoaderViewSet.as_view({
    'get':'index',
})
settings_put=SettingsLoaderViewSet.as_view({
    'put':'update'
})
urlpatterns = [
    path('', index),
    path('<int:pk>', settings_put),
    path('save', save_to_file)
]