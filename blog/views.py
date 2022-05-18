from django.shortcuts import render
from django.views import generic
from .models import Post, PostCategory
from .forms import CommentForm
from django.shortcuts import render, get_object_or_404


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    
    template_name = 'index.html'
    paginate_by = 9
    
    def get_context_data(self, *args, **kwargs):
        cat_menu = PostCategory.objects.all().order_by('name')
        context = super(PostList, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context
        
        
        

#class PostDetail(generic.DetailView):
 #   model = Post
  #  template_name = 'post_detail.html'

def fixed_posts():
    queryset_fixed=Post.objects.filter(fixing_status=1).order_by('-created_on')
    return render('partials/_sidebar.html', {'queryset_fixed': queryset_fixed})

def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats)
    category = get_object_or_404(PostCategory, pk=cats)
    return render(request, 'blog/categories.html', {'cats': cats, 'category_posts': category_posts, 'category': category})


def post_detail(request, slug):
    template_name = 'blog/post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments=post.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment=comment_form.save(commit=False)
            new_comment.post=post
            new_comment.save()

    else:
        comment_form=CommentForm()
    context={'post': post,
            'comments': comments,
            'new_comment': new_comment,
            'comment_form': comment_form
            }
    return render(request, template_name, context)


