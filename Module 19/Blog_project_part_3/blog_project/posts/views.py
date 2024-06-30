from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .import forms
from .import models
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

# Create your views here.
@login_required
def add_post(request):
    if request.method == 'POST': #user post request korche
       post_form = forms.PostForm(request.POST)  #user er post request data eikhane capture korlam
       if post_form.is_valid(): # post kora data gula valid kina amra check kortechi
           # post_form.cleaned_data['author'] = request.user
           post_form.instance.author = request.user
           post_form.save() # jodi data gula valid hoy taile data databse e save hbe
           return redirect('add_post') # sob thik thakle user k redirect kore category page e redirect kortechi
    else: #user normally website e gele blanck page pabe
        post_form = forms.PostForm()
    return render(request, 'add_post.html', {'form': post_form})


# Add post using class based view 
@method_decorator(login_required, name = 'dispatch')
class addPostCreateView(CreateView):
    model = models.Post
    form_class = forms.PostForm
    template_name = 'add_post.html'
    success_url = reverse_lazy('add_post')
    def form_valid(self, form): 
        form.instance.author = self.request.user
        return super().form_valid(form)


@login_required
def edit_post(request, id):
    post = models.Post.objects.get(pk = id)
    post_form = forms.PostForm(instance = post)
    print(post.title)
    if request.method == 'POST': #user post request korche
       post_form = forms.PostForm(request.POST, instance=post)  #user er post request data eikhane capture korlam
       if post_form.is_valid(): # post kora data gula valid kina amra check kortechi
           post_form.instance.author = request.user
           post_form.save() # jodi data gula valid hoy taile data databse e save hbe
           return redirect('home') # sob thik thakle user k redirect kore category page e redirect kortechi
    
    return render(request, 'add_post.html', {'form': post_form})


# update post using classbased view.
@method_decorator(login_required, name = 'dispatch')
class editPostView(UpdateView):
    model = models.Post
    form_class = forms.PostForm
    template_name = 'add_post.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('profile')
    def form_valid(self, form): 
        form.instance.author = self.request.user
        return super().form_valid(form)
    


@login_required
def delete_post(request, id):
    
    post = models.Post.objects.get(pk=id)
    post.delete()
    return redirect('home')



# delete post using classbased view.
@method_decorator(login_required, name = 'dispatch')
class deletePostView(DeleteView):
    model = models.Post
    template_name = 'delete.html'
    success_url = reverse_lazy('profile')
    pk_url_kwarg = 'id'
    
    
class detailPostView(DetailView):
    model = models.Post
    pk_url_kwarg = 'pk'
    template_name = 'post_details.html'
    
    
    def post(self, request, *args, **kwargs):
        comment_form = forms.CommentForm(data = self.request.POST)
        post = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit = False)
            new_comment.post = post
            new_comment.save()
        return self.get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object # post model er object ekhane share korlam 
        comments = post.comments.all()
        comment_form = forms.CommentForm()
        context ['comments'] = comments
        context['comment_form'] = comment_form
        
        return context
    
    
