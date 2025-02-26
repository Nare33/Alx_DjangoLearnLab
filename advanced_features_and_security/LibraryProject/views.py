from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Article

# View all articles - only users with 'can_view' permission can access this view
@permission_required('myapp.can_view', raise_exception=True)
def article_list(request):
    articles = Article.objects.all()
    return render(request, 'article_list.html', {'articles': articles})

# Create a new article - only users with 'can_create' permission can access this view
@permission_required('myapp.can_create', raise_exception=True)
def create_article(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        Article.objects.create(title=title, content=content)
        return redirect('article_list')
    return render(request, 'create_article.html')

# Edit an existing article - only users with 'can_edit' permission can access this view
@permission_required('myapp.can_edit', raise_exception=True)
def edit_article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    if request.method == 'POST':
        article.title = request.POST['title']
        article.content = request.POST['content']
        article.save()
        return redirect('article_list')
    return render(request, 'edit_article.html', {'article': article})

# Delete an article - only users with 'can_delete' permission can access this view
@permission_required('myapp.can_delete', raise_exception=True)
def delete_article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    article.delete()
    return redirect('article_list')

