from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def add(request):
    try:
        data = json.loads(request.body)
        a = data.get('A')
        b = data.get('B')
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError("Invalid input: A and B must be numbers.")
        return JsonResponse({"answer": a + b})
    except (ValueError, KeyError, json.JSONDecodeError) as e:
        return JsonResponse({"error": str(e)}, status=400)

@csrf_exempt
def subtract(request):
    try:
        data = json.loads(request.body)
        a = data.get('A')
        b = data.get('B')
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError("Invalid input: A and B must be numbers.")
        return JsonResponse({"answer": a - b})
    except (ValueError, KeyError, json.JSONDecodeError) as e:
        return JsonResponse({"error": str(e)}, status=400)

@csrf_exempt
def multiply(request):
    try:
        data = json.loads(request.body)
        a = data.get('A')
        b = data.get('B')
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError("Invalid input: A and B must be numbers.")
        return JsonResponse({"answer": a * b})
    except (ValueError, KeyError, json.JSONDecodeError) as e:
        return JsonResponse({"error": str(e)}, status=400)

@csrf_exempt
def divide(request):
    try:
        data = json.loads(request.body)
        a = data.get('A')
        b = data.get('B')
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError("Invalid input: A and B must be numbers.")
        if b == 0:
            raise ZeroDivisionError("Division by zero!")
        return JsonResponse({"answer": a / b})
    except (ValueError, KeyError, json.JSONDecodeError, ZeroDivisionError) as e:
        return JsonResponse({"error": str(e)}, status=400)
