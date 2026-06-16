from django.shortcuts import render, redirect
from .models import Equipment
from .forms import EquipmentForm

def equipment_list(request):
    equipments = Equipment.objects.all()
    return render(request, 'equipment/equipment_list.html', {'equipments': equipments})


def add_equipment(request):
    if request.method == 'POST':
        form = EquipmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/equipment/')
    else:
        form = EquipmentForm()

    return render(request, 'equipment/add_equipment.html', {'form': form})