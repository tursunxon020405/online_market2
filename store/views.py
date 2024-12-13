from django.shortcuts import render
from .models import *
from .forms import ChoiseForm
def home(request):
    ctg=Category.objects.all()
    product=Product.objects.all()
    ctx={'ctg':ctg,
         'product':product}
    return render(request,'index.html',ctx)

def product(request,slug):
    ctg=Category.objects.all()
    category=Category.objects.get(slug=slug)
    product=Product.objects.all().filter(type_id=category.id)
    ctx={'ctg':ctg,
         'category':category,
         'product':product}
    return render(request,'products.html',ctx)

def single(request, pk=None):
    ctg = Category.objects.all()
    product_pk = Product.objects.get(pk=pk)
    form = ChoiseForm()
    if request.POST:
        forms= ChoiseForm(request.POST or None, request.FILES or None)
        if forms.is_valid():
            root=forms.save()
            root=Buy.objects.get(pk=root.id)
            root.product=product_pk
            root.save()
            return redirect('home')
        else:
            print(forms.errors)