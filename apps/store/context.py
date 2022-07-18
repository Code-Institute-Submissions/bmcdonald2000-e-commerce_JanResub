# django imports
from .models import Category


# fucntion to process category menu context.
def category_menu(request):
    categories = Category.objects.all()

    return {'category_menu': categories}
