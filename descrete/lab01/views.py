from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
import itertools

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def truth_table(request):
    """
    入参：
    {
      "vars": ["P","Q"],
      "expr": "(P and Q) or (not P)"
    }
    返回：
    {
      "table": [
         {"P":true,"Q":true,"value":true},
         ...
      ],
      "pcnf": "...",
      "pdnf": "..."
    }
    """
    data = request.data
    vars = data['vars']
    expr = data['expr']

    def eval_expr(assign):
        env = {k: assign[k] for k in vars}
        return eval(expr, {"__builtins__":{}, "true":True, "false":False, "not":lambda x:not x, "and":lambda a,b:a and b, "or":lambda a,b:a or b}, env)

    table = []
    for values in itertools.product([False,True], repeat=len(vars)):
        assign = dict(zip(vars, values))
        assign['value'] = eval_expr(assign)
        table.append(assign)

    pdnf = " ∨ ".join([f"({'∧'.join([ (k if v else '¬'+k) for k,v in row.items() if k!='value' ])})" for row in table if row['value']])
    pcnf = " ∧ ".join([f"({'∨'.join([ ('¬'+k if v else k) for k,v in row.items() if k!='value' ])})" for row in table if not row['value']])

    return Response({"table": table, "pcnf": pcnf, "pdnf": pdnf})