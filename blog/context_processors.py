from .models import Post, PostCategory

def get_category_data(*args, **kwargs):
        categories_list={}
        cat_menu = PostCategory.objects.all().order_by('name')         
        categories_list={'cat_menu': cat_menu}        
        return categories_list

#In stand-by: volevo vedere se potevo cambiare dinamicamente il colore delle categorie
def get_category_color(*args, **kwargs):        
        cat_color = PostCategory.objects.all().order_by('name')         
        categories_color={'cat_color': cat_color}  
        #print(cat_color.category_color)      
        return categories_color


def get_post_left_fixed(*args, **kwargs):
        queryset=Post.objects.filter(fixing_status=1).order_by('-created_on')
        queryset_fixed={'queryset': queryset}        
        return queryset_fixed


        


        
