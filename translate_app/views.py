import dl_translate as dlt
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.shortcuts import render

# Carica il modello una sola volta all'avvio del server
translator = dlt.TranslationModel("facebook/m2m100_418M")

@csrf_exempt
def translate_text(request):
    if request.method == "POST":
        if 'HX-Request' in request.headers:
            text = request.POST.get('text', '')
            source_lang = request.POST.get('source_lang')
            target_lang = request.POST.get('target_lang')
        else:
            data = json.loads(request.body)
            text = data.get('text')
            source_lang = data.get('source_lang')
            target_lang = data.get('target_lang')
        
        if not text or not source_lang or not target_lang:
            return JsonResponse({'error': 'Missing parameters'}, status=400)

        try:
            translated_text = translator.translate(text, source=source_lang, target=target_lang, batch_size=32)
            if 'HX-Request' in request.headers:
                return HttpResponse(f'<span>{translated_text}</span>', content_type="text/html")
            else:
                return JsonResponse({'translated_text': translated_text}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=405)


def list_languages(request):
    if request.method == "GET":
        try:
            languages = translator.get_lang_code_map()
            if 'HX-Request' in request.headers:
                def_code = request.GET.get('def', '')
                options = ''.join([f'<option value="{code}" {"selected" if code == def_code else ""}>{name}</option>' for name, code in languages.items()])
                return HttpResponse(options, content_type="text/html")
            else:
                return JsonResponse({'languages': languages}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    return JsonResponse({'error': 'Invalid request method'}, status=405)

def home(request):
    return render(request, 'translate_app/index.html')
