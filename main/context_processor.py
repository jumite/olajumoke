from .models import *

def dropdown(request):
    info = AppInfo.objects.get(pk=1)
    fdog = Category.objects.all()
    # userprof = Customer.objects.get(user__username = request.user.username)
    
    
    context = {
         'info':info,
         'fdog':fdog,
          # 'userprof':userprof
    }
    
    return context


def cartcount(request):
     count = Cart.objects.filter(user__username =request.user.username, paid=False)
     
     itemcount = 0
     
     for item in count:
          itemcount += item.quantity
          
     context ={
          'itemcount':itemcount
     }  
     
     return context   
          