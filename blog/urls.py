from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('post/<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/create/', views.CreatePostView.as_view(), name='post_create'),
    path('post/<slug:slug>/edit/', views.UpdatePostView.as_view(), name='post_update'),
    path('post/<slug:slug>/delete/', views.DeletePostView.as_view(), name='post_delete'),
    path('drafts/', views.DraftListView.as_view(), name='post_draft_list'),
    path('post/<slug:slug>/publish/', views.publish_post(), name='post_publish'),
    path('post/<slug:slug>/comment/', views.add_comment_to_post(), name='add_post_comment'),
    path('comment/<slug:slug>/approve/', views.approve_comment, name='comment_approve'),
    path('comment/<slug:slug>/remove/', views.remove_comment, name='comment_remove'),
    path('summernote/', include('django_summernote.urls')),
]

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)