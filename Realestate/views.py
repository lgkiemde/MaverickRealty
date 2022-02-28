from django.shortcuts import render
from .models import *
from .forms import *
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

now = timezone.now()


def home(request):
    return render(request, 'Realestate/home.html',
                  {'Realestate': home})


#  @login_required
def customer_list(request):
    customer = Customer.objects.filter(created_date__lte=timezone.now())
    return render(request, 'Realestate/customer_list.html',
                  {'customers': customer})


#  @login_required
def customer_edit(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == "POST":
        # update
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.updated_date = timezone.now()
            customer.save()
            customer = Customer.objects.filter(created_date__lte=timezone.now())
            return render(request, 'Realestate/customer_list.html',
                          {'customers': customer})
    else:
        # edit
        form = CustomerForm(instance=customer)
    return render(request, 'Realestate/customer_edit.html', {'form': form})


#  @login_required
def customer_new(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.created_date = timezone.now()
            customer.save()
            customer = Customer.objects.filter(created_date__lte=timezone.now())
            return render(request, 'Realestate/customer_list.html',
                          {'customer': customer})
    else:
        form = CustomerForm()
        # print("Else")
    return render(request, 'Realestate/customer_new.html', {'form': form})



#  @login_required
def customer_delete(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    customer.delete()
    return redirect('Realestate:customer_list')


#  @login_required
def property_list(request):
    property = Property.objects.filter(created_date__lte=timezone.now())
    return render(request, 'Realestate/property_list.html',
                  {'property': property})


#  @login_required
def property_new(request):
    if request.method == "POST":
        form = PropertyForm(request.POST)
        if form.is_valid():
            property = form.save(commit=False)
            property.created_date = timezone.now()
            property.save()
            property = Property.objects.filter(created_date__lte=timezone.now())
            return render(request, 'Realestate/property_list.html',
                          {'property': property})
    else:
        form = PropertyForm()
        # print("Else")
    return render(request, 'Realestate/property_new.html', {'form': form})


#  @login_required
def property_edit(request, pk):
    property = get_object_or_404(Property, pk=pk)
    if request.method == "POST":
        form = PropertyForm(request.POST, instance=property)
        if form.is_valid():
            property = form.save()
            # service.customer = service.id
            property.updated_date = timezone.now()
            property.save()
            property = Property.objects.filter(created_date__lte=timezone.now())
            return render(request, 'Realestate/property_list.html', {'property': property})
    else:
        # print("else")
        form = PropertyForm(instance=property)
    return render(request, 'Realestate/property_edit.html', {'form': form})


#  @login_required
def property_delete(request,pk):
    property = get_object_or_404(Property, pk=pk)
    property.delete()
    return redirect('Realestate:property_list')


#  @login_required
def liens_list(request):
    liens = LienParcels.objects.filter(created_date__lte=timezone.now())
    return render(request, 'Realestate/liens_list.html',
                  {'liens': liens})


#  @login_required
def liens_edit(request, pk):
    liens = get_object_or_404(LienParcels, pk=pk)
    if request.method == "POST":
        form = LiensForm(request.POST, instance=liens)
        if form.is_valid():
            liens = form.save()
            # service.customer = service.id
            liens.updated_date = timezone.now()
            liens.save()
            liens = LienParcels.objects.filter(created_date__lte=timezone.now())
            return render(request, 'Realestate/liens_list.html', {'liens': liens})
    else:
        # print("else")
        form = LiensForm(instance=liens)
    return render(request, 'Realestate/liens_edit.html', {'form': form})


#  @login_required
def liens_delete(request, pk):
    liens = get_object_or_404(LienParcels, pk=pk)
    liens.delete()
    return redirect('Realestate:liens_list')


#  @login_required
def liens_new(request):
    if request.method == "POST":
        form = LiensForm(request.POST)
        if form.is_valid():
            liens = form.save(commit=False)
            liens.created_date = timezone.now()
            liens.save()
            liens = LienParcels.objects.filter(created_date__lte=timezone.now())
            return render(request, 'Realestate/liens_list.html',
                          {'liens': liens})
    else:
        form = LiensForm()
        # print("Else")
    return render(request, 'Realestate/liens_new.html', {'form': form})
