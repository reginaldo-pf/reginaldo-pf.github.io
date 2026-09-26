import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_http_methods
from .models import Calculation
from .utils import safe_eval

@ensure_csrf_cookie
def index(request):
    """
    Renderiza a página principal da calculadora.
    Garante que o cookie de CSRF seja enviado ao cliente para as requisições AJAX.
    """
    return render(request, 'calculator/index.html')

@require_http_methods(["POST"])
def calculate(request):
    """
    Recebe uma expressão matemática via JSON, executa o cálculo de forma segura,
    persiste no banco de dados e retorna o resultado.
    """
    try:
        data = json.loads(request.body)
        expression = data.get('expression', '').strip()
    except json.JSONDecodeError:
        return JsonResponse({
            'success': False,
            'error': 'Payload JSON inválido.'
        }, status=400)
    
    if not expression:
        return JsonResponse({
            'success': False,
            'error': 'A expressão não pode estar vazia.'
        }, status=400)

    try:
        # Avaliar expressão de forma segura
        result_val = safe_eval(expression)
        result_str = str(result_val)
        
        # Persistir no histórico do banco de dados
        calc = Calculation.objects.create(
            expression=expression,
            result=result_str
        )
        
        return JsonResponse({
            'success': True,
            'id': calc.id,
            'expression': expression,
            'result': result_str
        })
        
    except ZeroDivisionError:
        return JsonResponse({
            'success': False,
            'error': 'Divisão por zero.'
        }, status=400)
    except (ValueError, TypeError, NameError, SyntaxError) as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=400)
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': 'Erro desconhecido ao processar o cálculo.'
        }, status=500)

@require_http_methods(["GET"])
def history(request):
    """
    Retorna a lista dos últimos 10 cálculos realizados ordenados por data decrescente.
    """
    calcs = Calculation.objects.all()[:10]
    data = []
    for c in calcs:
        data.append({
            'id': c.id,
            'expression': c.expression,
            'result': c.result,
            'timestamp': c.timestamp.strftime('%d/%m/%Y %H:%M:%S')
        })
    return JsonResponse(data, safe=False)

@require_http_methods(["DELETE"])
def clear_history(request):
    """
    Limpa todos os cálculos salvos no histórico.
    """
    Calculation.objects.all().delete()
    return JsonResponse({
        'success': True,
        'message': 'Histórico de cálculos limpo com sucesso.'
    })
