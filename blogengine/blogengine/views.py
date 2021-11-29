from django.shortcuts import redirect

def redirect_blog(request):
    return redirect('blogpost_list_endpoint', parmanent=True)#301постійний,302тимчасовий по замовчуванню parmanent=False