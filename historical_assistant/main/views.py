# Create your views here.
from django.shortcuts import render
from .models import War
from django.http import JsonResponse
from .search import search_faiss

def search(request):
    if request.method == 'GET':
        query = request.GET.get('q')
        if query:
            try:
                results = search_faiss(query)
                formatted_results = [str(r) for r in results]
                return render(request, 'main/base.html', {'results': formatted_results})
            except Exception as e:
                return JsonResponse({'error': str(e)}, status=500)
        else:
            return JsonResponse({'error': 'Empty query'}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

def base(request):
    return render(request, 'main/base.html')