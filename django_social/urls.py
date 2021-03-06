from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from app.views import UserCreateView, MainView, SuggestionCreateView, AlcoholCreateView, UserDetailView, AddFollower, \
    FollowerListView, UserListView, AlcoholListView, AlcoholDetailView, LikeView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^signup/$', UserCreateView.as_view(), name="user_create_view"),
    url(r'^$', MainView.as_view(), name="main_view"),
    url(r'^login/$', auth_views.login, name="login_view"),
    url(r'^logout/$', auth_views.logout_then_login, name="logout_view"),
    url(r'^addalcohol/$', AlcoholCreateView.as_view(), name="alcohol_create_view"),
    url(r'^alcohollist/$', AlcoholListView.as_view(), name="alcohol_list_view"),
    url(r'^alcoholdetails/(?P<pk>\d+)$', AlcoholDetailView.as_view(), name="alcohol_detail_view"),
    url(r'^makesuggestion/$', SuggestionCreateView.as_view(), name="suggestion_create_view"),
    url(r'^userdetails/(?P<pk>\d+)/$', UserDetailView.as_view(), name="user_detail_view"),
    url(r'^addfollower/(?P<pk>\d+)/$', AddFollower.as_view(), name='add_follower_view'),
    url(r'^followerlist/(?P<pk>\d+)$', FollowerListView.as_view(), name="follower_list_view"),
    url(r'^userlist/', UserListView.as_view(), name="user_list_view"),
    url(r'^likes/(?P<pk>\d+)/$', LikeView.as_view(), name="like_view"),
]
