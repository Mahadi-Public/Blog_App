from django.shortcuts import render,redirect,get_object_or_404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from blog.forms import PostCreateFroms,CategoryCreateFroms
from blog.models import Post,Category,Comments
from django.contrib import messages
from django.db.models import Q

# Create your views here.

@login_required
def CategoryCreateView(request):
    
    if request.method == 'POST':
        form = CategoryCreateFroms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('PostCreateView')
    else:
        form = CategoryCreateFroms()
        
            
    return render(request, 'blog/category_form.html', {'FORMS' : form})



@login_required
def PostCreateView(request):
    
    if request.method == 'POST':
        form = PostCreateFroms(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Post created successfully")
            return redirect('PostListView')
    else:
        form = PostCreateFroms()
            
    return render(request, 'blog/blog_form.html', {'FORMS' : form, 'messages': messages.get_messages(request)})



@login_required
def PostListView(request):
    
    query = request.GET.get('search')
    posts = Post.objects.all().order_by('-created_at')
    commonTags = Post.tags.most_common()[:4]
    
    if query:
        posts = posts.filter(Q(categories__name__icontains=query))

    categories = Category.objects.all()
    
    context = {
        'POSTS': posts,
        'CATEGORIES': categories,
        'QUERY': query,
        'COMMONTAGS' : commonTags
    }
    
    return render(request, 'blog/blog_list.html', context)



@login_required
def PostUpdateView(request,id):
    
    posts = get_object_or_404(Post, id=id)
    form = PostCreateFroms(request.POST or None, instance=posts)
    if form.is_valid():
        form.save()
        messages.warning(request, "Post Updated successfully")
        return redirect('PostDetailsView', id=id)
    
    return render(request, 'blog/blog_update.html', {'FORMS' : form })     



@login_required
def PostDetailsView(request, id):
    
    posts = get_object_or_404(Post, id=id)
    comment = Comments.objects.filter(post=posts, parent=None)
    replies = Comments.objects.filter(post=posts).exclude(parent=None)
    
    context= {
        'POSTSDETAILS': posts,
        'COMMENTS' : comment,
        'REPLIES' : replies
    }
    return render(request, 'blog/blog_detail.html', context)



@login_required
def PostDeleteView(request, id):
    
    posts = get_object_or_404(Post, id=id)
    posts.delete()
    messages.error(request, "Post delete successfully")
    return redirect('PostListView')



@login_required
def CommentsView(request):
    
    if request.method == "POST":
        comment = request.POST['comment']
        postid = request.POST['postid']
        parentid = request.POST['parentid']
        
        query = Post.objects.get(id=postid)
        
        if parentid:
            parent = Comments.objects.get(id=parentid)
            newComments = Comments(body=comment, author=request.user, post=query, parent=parent)
            newComments.save()
        else:
            comment = Comments(body=comment, author=request.user, post=query)     
            comment.save()
            
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))