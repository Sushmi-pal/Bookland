from django.shortcuts import redirect


from main.views import SellCreateView, BuyListView

from main.views import searchbooks


class MyCustomMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self, request):
        response=self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.user:
            from accounts.views import ProfileView
            if not request.user.is_authenticated and view_func== ProfileView and view_func==BuyListView and view_func==SellCreateView   and view_func==searchbooks:
                return redirect('accounts:login')