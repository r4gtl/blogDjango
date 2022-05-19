from .models import PostCategory

def get_category_data(*args, **kwargs):
        categories_list={}
        cat_menu = PostCategory.objects.all().order_by('name') 
        print(cat_menu) 
        for cat in cat_menu:      
            categories_list.update((cat))
        print(categories_list)    
        return categories_list

        


        
