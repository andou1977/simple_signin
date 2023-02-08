from django.contrib import messages
from django.shortcuts import render

from untitled1.models import andouuser


def index(request):
    return render(request, 'index.html')



def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


def save(request):
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')
    telephone = request.POST.get('telephone')
    account = request.POST.get('account')
    address = request.POST.get('address')
    image=request.FILES.get('image')

    helo = andouuser(username=username, email=email, password=password, telephone=telephone, account=account,
                     address=address,image=image)
    helo.save()
    return render(request, 'register.html')


def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    list = andouuser.objects.filter(username=username, password=password)
    if andouuser.objects.filter(username=username).exists() and andouuser.objects.filter(password=password).exists():
        return render(request, 'dashboard.html', {'list': list})
    else:
        return render(request, 'login.html')


#
#
#
# </form>
#
# {% for dre in messages %}
# <label style="color: red">{{ dre }}</label>
# {% endfor %}
#
# </div>
#
#
# <div class="row">
# {% for listouest in  list %}
# <div class="col-md-4 col-sm-6 col-xs-12">
#
# <div class="single-service-elements">
#
# <div class="single-serv-element">
# <img src="{{ listouest.Image.url }}" alt=""  style="width: 400px ; height: 200px"/>
# <i> <a href="{% url 'idouest' listouest.id %}">view</a></i>
# </div>




