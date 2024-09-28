
# # # Create your views here.
# # from django.shortcuts import render, redirect
# # from .forms import BlogPostForm

# # def create_blog_post(request):
# #     if request.method == 'POST':
# #         form = BlogPostForm(request.POST, request.FILES)
# #         if form.is_valid():
# #             blog_post = form.save(commit=False)
# #             blog_post.author = request.user
# #             blog_post.save()
# #             return redirect('blog_post_detail', pk=blog_post.pk)
# #     else:
# #         form = BlogPostForm()
# #     return render(request, 'blog/create_blog.html', {'form': form})

# # from .models import BlogPost

# # def blog_list(request):
# #     blogs = BlogPost.objects.all()
# #     return render(request, 'blog/blog_list.html', {'blogs': blogs})

# # from django.shortcuts import get_object_or_404

# # def blog_post_detail(request, pk):
# #     blog_post = get_object_or_404(BlogPost, pk=pk)
# #     return render(request, 'blog/blog_detail.html', {'blog_post': blog_post})

# # def update_blog_post(request, pk):
# #     blog_post = get_object_or_404(BlogPost, pk=pk)
# #     if request.method == 'POST':
# #         form = BlogPostForm(request.POST, request.FILES, instance=blog_post)
# #         if form.is_valid():
# #             form.save()
# #             return redirect('blog_post_detail', pk=blog_post.pk)
# #     else:
# #         form = BlogPostForm(instance=blog_post)
# #     return render(request, 'blog/update_blog.html', {'form': form})

# # from django.shortcuts import redirect

# # def delete_blog_post(request, pk):
# #     blog_post = get_object_or_404(BlogPost, pk=pk)
# #     if request.method == 'POST':
# #         blog_post.delete()
# #         return redirect('blog_list')
# #     return render(request, 'blog/delete_blog.html', {'blog_post': blog_post})

# from django.http import JsonResponse
# from django.shortcuts import render, redirect, get_object_or_404
# from .forms import BlogPostForm
# from .models import BlogPost
# def create_blog_post(request):
#     if request.method == 'POST':
#         form = BlogPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             blog_post = form.save(commit=False)
#             blog_post.author = request.user
#             blog_post.save()
#             return redirect('blog_post_detail', pk=blog_post.pk)
#     else:
#         form = BlogPostForm()
#     return render(request, 'blog/create_blog.html', {'form': form})

# def blog_list(request):
#     blogs = BlogPost.objects.all()
#     return render(request, 'blog/blog_list.html', {'blogs': blogs})

# def blog_post_detail(request, pk):
#     blog_post = get_object_or_404(BlogPost, pk=pk)
#     return render(request, 'blog/blog_detail.html', {'blog_post': blog_post})

# def update_blog_post(request, pk):
#     blog_post = get_object_or_404(BlogPost, pk=pk)
#     if request.method == 'POST':
#         form = BlogPostForm(request.POST, request.FILES, instance=blog_post)
#         if form.is_valid():
#             form.save()
#             return redirect('blog_post_detail', pk=blog_post.pk)
#     else:
#         form = BlogPostForm(instance=blog_post)
#     return render(request, 'blog/update_blog.html', {'form': form})

# def delete_blog_post(request, pk):
#     blog_post = get_object_or_404(BlogPost, pk=pk)
#     if request.method == 'POST':
#         blog_post.delete()
#         return redirect('blog_list')
#     return render(request, 'blog/delete_blog.html', {'blog_post': blog_post})


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from .forms import BlogPostForm, SignUpForm
from .models import BlogPost

@login_required
def create_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user
            blog_post.save()
            return redirect('blog_post_detail', pk=blog_post.pk)
    else:
        form = BlogPostForm()
    return render(request, 'blog/create_blog.html', {'form': form})

def blog_list(request):
    blogs = BlogPost.objects.all()
    return render(request, 'blog/blog_list.html', {'blogs': blogs})

def blog_post_detail(request, pk):
    blog_post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'blog/blog_detail.html', {'blog_post': blog_post})

@login_required
def update_blog_post(request, pk):
    blog_post = get_object_or_404(BlogPost, pk=pk)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=blog_post)
        if form.is_valid():
            form.save()
            return redirect('blog_post_detail', pk=blog_post.pk)
    else:
        form = BlogPostForm(instance=blog_post)
    return render(request, 'blog/update_blog.html', {'form': form})

@login_required
def delete_blog_post(request, pk):
    blog_post = get_object_or_404(BlogPost, pk=pk)
    if request.method == 'POST':
        blog_post.delete()
        return redirect('blog_list')
    return render(request, 'blog/delete_blog.html', {'blog_post': blog_post})

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('blog_list')
    else:
        form = SignUpForm()
    return render(request, 'blog/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('blog_list')
    else:
        form = AuthenticationForm()
    return render(request, 'blog/login.html', {'form': form})
