from django.shortcuts import render, redirect
from django.http import  HttpResponse
from .models import Place, Img, Review, Profile, City
from django.contrib.auth.decorators import login_required
from .forms import UserForm, ProfileForm, SearchForm, ReviewForm
from django.utils import timezone
from django.views import View

from django.contrib.auth import update_session_auth_hash


# Create your views here.

def index(request):
    return HttpResponse("Hello World")

def findStr(filter, str):
    if (filter == None or str == None):
        return None
    else:
        res = None
        i1 = filter.rfind(str)
        if (i1 >= 0):
            t = i1 + len(str)
            tmp = filter.find('&', t + 1)
            if (tmp == -1):
                res = filter[t:]
            else:
                res = filter[t:tmp]
        return res


class ShowAllProduct(View):
    def get(self, request):
        pass
def showAllProduct(request, type = None, order = None, filter = None):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data['search']
            place_list = Place.objects.all().filter(Name__contains=data)
            title = 'Search: {}'.format(str)
            context = {'place_list': place_list, 'title': title, 'searchForm': SearchForm()}
            return redirect('product:search', name = data)

    place_list = Place.objects.all()
    title = 'All'

    if (type == 'Sight'):
        place_list = place_list.filter(Type = 1)
        title = type
    elif (type == 'Restauran'):
        place_list = place_list.filter(Type = 2)
        title = type
    elif (type == 'Museum'):
        place_list = place_list.filter(Type = 3)
        title = type

    print(order)
    if (order == 'rating'):
        place_list = place_list.order_by('-Rating')
    elif (order == 'name'):
        place_list = place_list.order_by('Name')

    if (filter != None):
        try:
            c = City.objects.get(Name = filter)
            place_list = place_list.filter(City = c.id)
        except:
            print("Error")


    searchForm = SearchForm()
    allCity = City.objects.all()
    content = {'place_list': place_list, 'title': title, 'searchForm': searchForm, 'allCity': allCity}
    return render(request, 'product/cartegory.html', content)


def showProduct(request, id):
    p = Place.objects.get(id = id)
    p.updateRating()
    img5 = Img.objects.all().filter(place = id)[0:5]
    relatedProduct = Place.objects.exclude(id = id)[0:5]

    if request.user.is_authenticated:
        a = request.user.id
        try:
            userReview = Review.objects.get(id =  request.user.id)
        except:
            userReview = []
    try:
        reviews  = Review.objects.filter(place = id)
    except:
        reviews = []
    r = []
    for i in reviews:
        r.append([Profile.objects.get(user = i.auth), i])

    searchForm = SearchForm()
    reviewForm = ReviewForm()
    print('CHECK GET METHOD')

    if request.method == 'POST':
        print("Enter POST")

        reviewForm = ReviewForm(request.POST)
        if reviewForm.is_valid():
            comment = reviewForm.cleaned_data['comment']
            rating = reviewForm.cleaned_data['rating']
            print(rating)
            print(comment,  id, request.user.id)
            newReview = Review.objects.create(comment = comment, createTime = timezone.datetime.now(),
                                              place = Place.objects.get(id = id), auth = request.user, rating = rating)
            newReview.save()
            return redirect('product:product', id = id)



    content = {'place': p, 'img5': img5, 'related': relatedProduct, 'auth': r, 'searchForm' : SearchForm(), 'reviewForm': reviewForm}

    return render(request, 'product/product.html', content)

'''
User
'''

def login(request):
    return render(request, 'product/login.html')

@login_required(login_url='/products/login/')
def profile(request):
    if request.user.is_authenticated:
        cur_user = request.user
        try:
            p = Profile.objects.get(user = cur_user)
            context = {'profile': p}
            return render(request, 'product/profile.html', context)
        except:
            redirect('admin:admin')
    else:
        return redirect('product:login')

@login_required(login_url='/products/login/')
def editProfile(request):
    if (request.method == 'POST'):
        userform = UserForm(request.POST, instance=request.user)
        profileform = ProfileForm(request.POST, request.FILES, request.user.profile)

        if userform.is_valid() and profileform.is_valid():

            p = Profile.objects.get(user=request.user)
            ava = p.avatar
            p.delete()
            user_form = userform.save()
            Profile.objects.get(user = request.user).delete()
            profile_form = profileform.save(False)
            profile_form.user = request.user
            if (not request.FILES):
                profile_form.avatar = ava
            profile_form.save()
        return redirect('product:profile')
    else:
        userform = UserForm(instance=request.user)
        profileform = ProfileForm(instance=request.user.profile)
        args = {}
        args['userform'] = userform
        args['profileform'] = profileform
        args['profile'] = request.user.profile
        return render(request, 'product/profile.html', args)



def search(request, name):
    place_list = Place.objects.all().filter(Name__contains = name)
    title = 'Search: {}'.format(name)
    searchForm = SearchForm()
    context = {'place_list': place_list, 'title': title, 'searchForm': searchForm}
    return render(request, 'product/cartegory.html', context)


def show(request, str):
    type = findStr(str, 'Type=')
    order = findStr(str, 'Order=')
    city = findStr(str, 'City=')
    filter = findStr(str, 'Filter=')
    return redirect('product:type_order_filter', type = type, order = order, filter = filter)


def showContact(request):
    return render(request, 'product/contact.html')






