from django.http import HttpResponse


class CorsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Разрешить доступ с вашего фронтенда
        response['Access-Control-Allow-Origin'] = 'http://localhost:5173'  # Здесь укажите адрес вашего фронтенда
        response['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
        response['Access-Control-Allow-Headers'] = 'Content-Type'

        # Для поддержки OPTIONS запроса (предварительный запрос, проверяющий разрешения CORS)
        if request.method == 'OPTIONS':
            response['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
            response['Access-Control-Allow-Headers'] = 'Content-Type'
            response.status_code = 200  # Если это OPTIONS запрос, сразу возвращаем ответ без дальнейшей обработки

        return response