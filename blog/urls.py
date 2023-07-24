from django.urls import path
from . import views
app_name = "blog"

urlpatterns = [
    path("",views.PostList.as_view(), name= "post_list" ),
    path("<slug:slug>", views.PostDetail.as_view(),name= "post_detail" ),
    path("category/<str:slug>", views.PostByCategory.as_view(),name= "post_by_category" ),
    path("tag/<slug:slug>", views.PostByTag.as_view(),name= "post_by_tag" ),
]
