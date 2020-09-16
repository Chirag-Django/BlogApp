from django.urls import path
from . import views

urlpatterns = [
    path('about/',views.AboutView.as_view(),name='about'),
    path('',views.PostListView.as_view(),name='post_list'),
    path('post/<int:pk>/',views.PostDetailView.as_view(),name='post_detail'),
    path('post/create/',views.post_create,name='post_create'),
    path('post/update/<int:pk>/',views.post_update,name='post_update'),
    path('post/delete/<int:pk>/',views.PostDeleteView.as_view(),name='post_delete'),
    path('drafts/',views.DraftListView.as_view(),name='draft_lists'),
    path('post/comment/<int:pk>/',views.add_comment_to_post,name='add_comment_to_post'),
    path('comment/<int:pk>/approve/',views.comment_approve,name='comment_approve'),
    path('comment/<int:pk>/remove/',views.comment_remove,name='comment_remove'),
    path('post/publish/<int:pk>/',views.post_publish,name='post_publish'),
]
