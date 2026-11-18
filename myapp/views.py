# app - views.py file

from django.shortcuts import get_object_or_404, redirect, render
from .models import User
from .forms import UserForm

# Create your views here.


def user_list(request):
    records = User.objects.all().order_by("name")
    mydict = {
        "records": records,
        "user_count": records.count(),
        "photo_count": records.exclude(photo="").exclude(photo="a.png").count(),
    }
    return render(request, "Listingpage.html", context=mydict)


def AddUser(request):
    mydict = {}
    form = UserForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect("user_list")

    mydict["form"] = form
    return render(request, "Add.html", mydict)


def EditUser(request, id=None):
    one_rec = get_object_or_404(User, pk=id)
    form = UserForm(request.POST or None, request.FILES or None, instance=one_rec)
    if form.is_valid():
        form.save()
        return redirect("user_list")
    mydict = {"form": form}
    return render(request, "edit.html", context=mydict)


def DeleteUser(request, eid=None):
    one_rec = get_object_or_404(User, pk=eid)
    if request.method == "POST":
        one_rec.delete()
        return redirect("user_list")
    return render(request, "Delete.html", {"user": one_rec})


def ViewUser(request, eid=None):
    mydict = {}
    one_rec = get_object_or_404(User, pk=eid)
    mydict["user"] = one_rec
    return render(request, "View.html", mydict)
