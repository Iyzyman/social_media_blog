from django.contrib import messages
from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import Http404
from django.views import generic
from posts.forms import CommentForm
from django.contrib.auth.decorators import login_required

# pip install django-braces
from braces.views import SelectRelatedMixin

from . import forms
from . import models
from groups.models import Group, GroupMember

from django.contrib.auth import get_user_model
User = get_user_model()


class PostList(SelectRelatedMixin, generic.ListView):
    model = models.Post
    select_related = ("user", "group")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form']= CommentForm()
        context['get_other_groups']=Group.objects.all()
        if self.request.user.is_authenticated:
            context['get_user_groups'] = Group.objects.filter(memberships__user=self.request.user)
        return context
 


class UserPosts(generic.ListView):
    model = models.Post
    template_name = "posts/user_post_list.html"

    def get_queryset(self):
        try:
            self.post_user = User.objects.prefetch_related("posts").get(
                username__iexact=self.kwargs.get("username")
            )
        except User.DoesNotExist:
            raise Http404
        else:
            return self.post_user.posts.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_user"] = self.post_user
        context['comment_form']= CommentForm()
        return context


class PostDetail(SelectRelatedMixin, generic.DetailView):
    model = models.Post
    comment_form = CommentForm()
    select_related = ("user", "group")

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(
            user__username__iexact=self.kwargs.get("username")
        )
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form']= CommentForm()
        return context
   

class CreatePost(LoginRequiredMixin, SelectRelatedMixin, generic.CreateView):
    # form_class = forms.PostForm
    fields = ('image','message','group')
    model = models.Post

    # def get_form_kwargs(self):
    #     kwargs = super().get_form_kwargs()
    #     kwargs.update({"user": self.request.user})
    #     return kwargs

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)
    

class DeletePost(LoginRequiredMixin, SelectRelatedMixin, generic.DeleteView):
    model = models.Post
    select_related = ("user", "group")
    success_url = reverse_lazy("groups:all")

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id=self.request.user.id)

    def delete(self, *args, **kwargs):
        messages.success(self.request, "Post Deleted")
        return super().delete(*args, **kwargs)
    
@login_required
def add_comment_to_post(request, username, pk):
    post = get_object_or_404(models.Post, user__username=username, pk=pk)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
    return redirect('posts:single', username=post.user.username, pk=post.pk)
    
    