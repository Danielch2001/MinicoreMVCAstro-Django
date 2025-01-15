import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from api.models import Departamento, Empleado, Gasto

# Crear Departamentos
it = Departamento.objects.create(nombre='IT')
desarrollo = Departamento.objects.create(nombre='Desarrollo')
diseno = Departamento.objects.create(nombre='Diseño')
marketing = Departamento.objects.create(nombre='Marketing')

# Crear Empleados
zoila = Empleado.objects.create(nombre='Zoila Baca', departamento=it)
aquiles = Empleado.objects.create(nombre='Aquiles C', departamento=it)
johnny = Empleado.objects.create(nombre='Johnny Melas', departamento=desarrollo)

# Crear Gastos
Gasto.objects.create(fecha='2024-11-16', descripcion='UPS', monto=60, empleado=zoila, departamento=it)
Gasto.objects.create(fecha='2024-11-22', descripcion='Monitor secundario', monto=250, empleado=johnny, departamento=desarrollo)
Gasto.objects.create(fecha='2024-11-23', descripcion='Rollup', monto=60, empleado=johnny, departamento=diseno)
Gasto.objects.create(fecha='2024-11-25', descripcion='UPS', monto=60, empleado=zoila, departamento=it)
