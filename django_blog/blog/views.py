from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post, Comment
from .forms import CommentForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render
from .models import Post, Tag

class PostByTagListView(ListView):
    model = Post
    template_name = 'blog/post_list_by_tag.html'  # Use your desired template
    context_object_name = 'posts'

    def get_queryset(self):
        tag_slug = self.kwargs['tag_slug']
        tag = get_object_or_404(Tag, slug=tag_slug)
        return Post.objects.filter(tags=tag)

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'  

    def get_queryset(self):
        queryset = Post.objects.all()

        search_query = self.request.GET.get('search', '')
        if search_query:
            queryset = queryset.filter(Q(title__icontains=search_query) | Q(content__icontains=search_query))

        return queryset

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

class PostCreateView(CreateView):
    model = Post
    template_name = 'blog/post_form.html'  
    fields = ['title', 'content', 'tags']
    success_url = reverse_lazy('post-list')

class PostUpdateView(UpdateView):
    model = Post
    template_name = 'blog/post_form.html'  
    fields = ['title', 'content', 'tags']  
    success_url = reverse_lazy('post-list')

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'  
    success_url = reverse_lazy('post-list')

def post_search(request):
    search_query = request.GET.get('q', '')  # Get the search query from the GET request
    tag_query = request.GET.get('tag', '')  # Get the tag filter from the GET request
    
    if search_query and tag_query:
        posts = Post.objects.filter(
            Q(title__icontains=search_query) |
            Q(content__icontains=search_query),
            tags__name__icontains=tag_query  # Filter by tag name
        ).distinct()  # Use distinct to ensure no duplicate posts

    elif search_query:
        posts = Post.objects.filter(
            Q(title__icontains=search_query) | Q(content__icontains=search_query)
        )
    elif tag_query:
        posts = Post.objects.filter(tags__name__icontains=tag_query).distinct()
    else:
        posts = Post.objects.all()

    return render(request, 'blog/post_list.html', {'posts': posts, 'search_query': search_query, 'tag_query': tag_query})

def tag_posts(request, tag_name):
    tag = Tag.objects.get(name=tag_name)
    posts = tag.posts.all()  
    return render(request, 'blog/tag_posts.html', {'posts': posts, 'tag_name': tag_name})

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/post_detail.html'

    def form_valid(self, form):
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        form.instance.author = self.request.user
        form.instance.post = post
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'post_id': self.kwargs['pk']})

class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/edit_comment.html'

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'post_id': self.object.post.id})

    def test_func(self):
        comment = self.get_object()
        return comment.author == self.request.user

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'blog/confirm_delete.html'
    context_object_name = 'comment'

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'post_id': self.object.post.id})

    def test_func(self):
        comment = self.get_object()
        return comment.author == self.request.user

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all()
    comment_form = CommentForm()

    if request.method == "POST" and request.user.is_authenticated:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', post_id=post.id)

    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments, 'comment_form': comment_form})

@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user != comment.author:
        return redirect('post_detail', post_id=comment.post.id)

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('post_detail', post_id=comment.post.id)
    else:
        form = CommentForm(instance=comment)

    return render(request, 'blog/edit_comment.html', {'form': form, 'comment': comment})

@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user == comment.author:
        post_id = comment.post.id
        comment.delete()
        return redirect('post_detail', post_id=post_id)
    return redirect('post_detail', post_id=comment.post.id)

