from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, PostLoginView
from . import views

urlpatterns = [
    path('', PostLoginView.as_view(), name='login_page'),
    path('home', PostListView.as_view(), name='core_backend'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_confirm_delete'),
    path('about/', views.about, name='core_backend-about'),
    path('post/new/', PostCreateView.as_view(), name='post_new'),

]



