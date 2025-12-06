from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .relation import (
    is_reflexive, is_irreflexive, is_symmetric,
    is_anti_symmetric, is_transitive,
    reflexive_closure, symmetric_closure, transitive_closure, warshall_steps
)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def calculate(request):
    m = request.data.get('matrix', [])
    n = len(m)
    # 基本校验
    if any(len(row)!=n for row in m):
        return Response({'detail':'矩阵必须为方阵'}, status=400)

    props = {
        'reflexive':      is_reflexive(m),
        'irreflexive':    is_irreflexive(m),
        'symmetric':      is_symmetric(m),
        'antiSymmetric':  is_anti_symmetric(m),
        'transitive':     is_transitive(m),
    }
    closures = {
        'reflexive':   reflexive_closure(m),
        'symmetric':   symmetric_closure(m),
        'transitive':  transitive_closure(m),
    }
    warshall = warshall_steps(m)

    return Response({
        'props': props,
        'closures': closures,
        'warshallSteps': warshall
    })
