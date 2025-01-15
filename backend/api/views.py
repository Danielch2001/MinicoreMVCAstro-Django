from rest_framework.viewsets import ModelViewSet
from .serializers import GastoSerializer
from django.db.models import Sum, Value, FloatField, OuterRef, Subquery
from django.http import JsonResponse
from .models import Gasto, Departamento
from django.db.models.functions import Coalesce, Cast
from django.db.models import FloatField

class GastoViewSet(ModelViewSet):
    queryset = Gasto.objects.all()
    serializer_class = GastoSerializer


def totales_por_departamento(request):
    fecha_inicio = request.GET.get('fecha_inicio')
    fecha_fin = request.GET.get('fecha_fin')

    if not fecha_inicio or not fecha_fin:
        return JsonResponse({'error': 'Debe proporcionar fecha_inicio y fecha_fin'}, status=400)

    # Subquery para calcular el total de gastos por departamento
    subquery = Gasto.objects.filter(
        fecha__range=[fecha_inicio, fecha_fin],
        departamento_id=OuterRef('pk')
    ).annotate(
        total_gasto=Coalesce(Sum('monto', output_field=FloatField()), Value(0, output_field=FloatField()))
    ).values('total_gasto')[:1]

    # Anotar todos los departamentos con el total correspondiente
    totales = Departamento.objects.annotate(
        total=Coalesce(Subquery(subquery, output_field=FloatField()), Value(0, output_field=FloatField()))
    ).values('nombre', 'total')

    # Retornar los datos como JSON
    return JsonResponse(list(totales), safe=False)
    