from django.shortcuts import render
from .forms import SellForm
from django.contrib.auth.models import User
from .models import Description
from django.shortcuts import get_object_or_404
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
# Create your views here.
class SellCreateView(LoginRequiredMixin,CreateView):
    model = Description
    fields = ['book_name', 'edition', 'location', 'price', 'phone', 'book_image']

    def form_valid(self, form):
        form.instance.seller=self.request.user
        return super().form_valid(form)

class SellUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Description
    fields = ['book_name', 'edition', 'location', 'price', 'phone', 'book_image']

    def form_valid(self, form):
        form.instance.seller=self.request.user
        return super().form_valid(form)

    def test_func(self):
        desc=self.get_object()
        if self.request.user==desc.seller:
            return True
        return False



def SellBooks(request):
    u=User.objects.get(id=request.user.id)
    u.save()
    if request.method=='POST':
        form=SellForm(request.POST,request.FILES)
        if form.is_valid():
            print('form is valid')
            form.save()




    elif request.method=='GET':
        form=SellForm()
    context={
        'form':form


    }
    return render(request,'main/sell.html',context)

def BuyBooks(request):
    u=User.objects.all()
    desc=Description.objects.all()
    return render(request,'main/buy.html',{'desc':desc,'u':u})




class BuyListView(ListView):
    model = Description
    template_name = 'main/buy.html'
    context_object_name = 'desc'



class BuyDetailView(DetailView):
    model = Description

class SellDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Description
    success_url = '/begin/'

    def test_func(self):
        desc = self.get_object()
        if self.request.user == desc.seller:
            return True
        return False






def DetailofBooks(request,user_id):
    obj=get_object_or_404(User,id=user_id)
    desc = get_object_or_404(Description,id=user_id)
    return render(request,'main/description_detail.html',{'desc':desc,'obj':obj})


def searchbooks(request):
    query=request.GET['query']
    books=Description.objects.filter(book_name__icontains=query)
    return render(request,'main/searchbooks.html',{'desc':books})

