from django.views.generic import ListView, TemplateView, DetailView
from .models import Post
from hitcount.views import HitCountDetailView
from .services import get_cloudapi_data
from django.shortcuts import render

# Create your views here.


class BlogListView(ListView):
    model = Post
    template_name = "home.html"


class BlogDetailView(HitCountDetailView, DetailView):
    model = Post
    template_name = "post_detail.html"
    context_object_name = "postdetail"

    count_hit = True
    """
    data = {
        "hits": get_cloudapi_data(),
    }
    
    # for id in id_qs

    def get_hits(self):
        for value in self.data["hits"][0].items():
            if value == self.id_qs:
                hits = value

        return hits
    """
    id_qs = Post.objects.values_list("id")
    """
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["id_qs"] = Post.objects.values_list("id", flat=True)
        return context
    """

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["hits"] = get_cloudapi_data()
        return context


# print(BlogDetailView.id_qs)
# print(BlogDetailView.data["hits"][0].items())


class ResumePageView(TemplateView):
    template_name = "resume.html"


# test = BlogDetailView()
# print(test.get_context_data())
