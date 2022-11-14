# django imports
from .models import Category


# fucntion to process category menu context.
def category_menu(request):
    # subcategories will be shown
    categories = Category.objects.filter(parent=None)

    return {'category_menu': categories}
