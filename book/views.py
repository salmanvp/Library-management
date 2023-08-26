from django.shortcuts import render
from .models import book
from .models import student
from .forms import bookform
from .forms1 import studentform


def home(request):
    return render(request, 'home.html')


def add(request):
    if (request.method == 'POST'):
        a = request.POST['a']
        b = request.POST['b']
        c = request.POST['c']
        d = request.FILES['d']
        e = request.FILES['e']
        f = book.objects.create(title=a, author=b, price=c, pdf=d, cover=e)
        f.save()

        return view(request)
    return render(request, 'add book.html')


def view(request):
    k = book.objects.all()
    return render(request, 'view book.html', {'b': k})


def views(request):
    s = student.objects.all()
    return render(request, 'view student.html', {'a': s})


def addstudent(request):
    if (request.method == "POST"):
        x = (request.POST['x'])
        y = (request.POST['y'])
        z = (request.POST['z'])
        p = student.objects.create(name=x, age=y, place=z)
        p.save()

    return render(request, 'add student.html')


def fact(request):
    if (request.method == 'POST'):
        n = int(request.POST['n'])
        f = 1
        for i in range(1, n + 1):
            f = f * i
        return render(request, 'fact.html', {'fact': f})

    return render(request, 'fact.html')


def addbook1(request):
    f = bookform()
    if (request.method == "POST"):
        f = bookform(request.POST, request.FILES)
        if f.is_valid():
            f.save()
            return view(request)
    return render(request, 'addbook1.html', {'f': f})


def addstudent1(request):
    a = studentform()
    if request.method == 'POST':
        a = studentform(request.POST)
        if a.is_valid():
            a.save()
            return views(request)
    return render(request, 'add student1.html', {'a': a})


def nextview(request, p):
    b = book.objects.get(id=p)
    return render(request, 'nextview.html', {'b': b})


def delete(request, p):
    b = book.objects.get(id=p)
    b.delete()
    return view(request)


def edit(request, p):
    b = book.objects.get(id=p)
    f = bookform(instance=b)
    if (request.method == 'POST'):
        f = bookform(request.POST, request.FILES, instance=b)
        if f.is_valid():
            f.save()
            return view(request)
    return render(request, 'addbook1.html', {'f': f})
