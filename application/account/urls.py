from django.conf.urls import patterns, include, url
import views


urlpatterns = patterns('',
    url(r'^login/$', 
        views.LoginView.as_view(), 
        name='login'
    ),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^create_user/', 
        views.CreateUserView.as_view(), 
        name='create-user'
    )
)
