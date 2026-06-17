from django.shortcuts import render, redirect
from .models import Equipment
from .forms import EquipmentForm
from django.shortcuts import get_object_or_404

def equipment_list(request):

    query = request.GET.get('q')

    if query:
        equipments = Equipment.objects.filter(
            name__icontains=query
        )

    else:
        equipments = Equipment.objects.all()

    return render(
        request,
        'equipment/equipment_list.html',
        {
            'equipments': equipments
        }
    )

def add_equipment(request):
    if request.method == 'POST':
        form = EquipmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/equipment/')
    else:
        form = EquipmentForm()

    return render(request, 'equipment/add_equipment.html', {'form': form})
# EDIT
def edit_equipment(request, id):
    equipment = get_object_or_404(Equipment, id=id)

    if request.method == 'POST':
        form = EquipmentForm(request.POST, instance=equipment)

        if form.is_valid():
            form.save()
            return redirect('/equipment/')

    else:
        form = EquipmentForm(instance=equipment)

    return render(
        request,
        'equipment/edit_equipment.html',
        {'form': form}
    )


# DELETE
def delete_equipment(request, id):
    equipment = get_object_or_404(Equipment, id=id)

    equipment.delete()

    return redirect('/equipment/')

def dashboard(request):

    total = Equipment.objects.count()

    available = Equipment.objects.filter(
        status='Available'
    ).count()

    maintenance = Equipment.objects.filter(
        status='Maintenance'
    ).count()

    return render(
        request,
        'equipment/dashboard.html',
        {
            'total': total,
            'available': available,
            'maintenance': maintenance
        }
    )
