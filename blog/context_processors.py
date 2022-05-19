from .models import Post, PostCategory

def get_category_data(*args, **kwargs):
        categories_list={}
        cat_menu = PostCategory.objects.all().order_by('name')         
        categories_list={'cat_menu': cat_menu}        
        return categories_list


def get_post_left_fixed(*args, **kwargs):
        queryset=Post.objects.filter(fixing_status=1).order_by('-created_on')
        queryset_fixed={'queryset': queryset}        
        return queryset_fixed
        


        
