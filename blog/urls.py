from django.urls import path
from .views import BlogListView, ResumePageView, BlogDetailView

urlpatterns = [
    path("post/<int:pk>/", BlogDetailView.as_view(), name="post_detail"),
    path("", BlogListView.as_view(), name="home"),
    path("resume/", ResumePageView.as_view(), name="resume"),
]
