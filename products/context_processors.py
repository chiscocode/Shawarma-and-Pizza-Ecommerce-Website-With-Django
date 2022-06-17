from products.models import *

def main_categories(request):
    categories=Category.objects.all()

    return{'main_categories':categories}