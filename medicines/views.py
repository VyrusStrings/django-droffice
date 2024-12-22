from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MedicineForm
from .models import Medicine

@login_required
def create_medicine(request):
    if not request.user.is_doctor:
        messages.error(request, "Permission denied.")
        return redirect('home')
    if request.method == 'POST':
        form = MedicineForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Medicine created.")
            return redirect('medicines:list')
        else:
            messages.error(request, "Please correct the errors.")
    else:
        form = MedicineForm()
    return render(request, 'medicines/create_medicine.html', {'form': form})

@login_required
def list_medicines(request):
    if not request.user.is_doctor:
        messages.error(request, "Permission denied.")
        return redirect('home')
    meds = Medicine.objects.all()
    return render(request, 'medicines/list_medicines.html', {'medicines': meds})

@login_required
def update_medicine(request, pk):
    if not request.user.is_doctor:
        messages.error(request, "Permission denied.")
        return redirect('home')
    med = Medicine.objects.get(pk=pk)
    if request.method == 'POST':
        form = MedicineForm(request.POST, instance=med)
        if form.is_valid():
            form.save()
            messages.success(request, "Medicine updated.")
            return redirect('medicines:list')
        else:
            messages.error(request, "Please correct the errors.")
    else:
        form = MedicineForm(instance=med)
    return render(request, 'medicines/update_medicine.html', {'form': form})

@login_required
def delete_medicine(request, pk):
    if not request.user.is_doctor:
        messages.error(request, "Permission denied.")
        return redirect('home')
    med = Medicine.objects.get(pk=pk)
    if request.method == 'POST':
        med.delete()
        messages.success(request, "Medicine deleted.")
        return redirect('medicines:list')
    return render(request, 'medicines/delete_medicine.html', {'medicine': med})
