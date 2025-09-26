from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from apps.rest_api.models import ApiKey

BYPASS_PATHS = (
    "/api/schema",
    "/api/docs",
    "/swagger",
    "/swagger.json",
    "/redoc",
)

class ApiKeyAuthentication(BaseAuthentication):
    def authenticate(self, request):

        path = (request.path or "").rstrip("/") 
        if any(path.startswith(p.rstrip("/")) for p in BYPASS_PATHS):
            return None

        api_key = request.headers.get("X-API-Key")
        if not api_key:
            raise AuthenticationFailed("API key is required")

        try:
            key = ApiKey.objects.get(key=api_key, is_active=True)
        except ApiKey.DoesNotExist:
            raise AuthenticationFailed("Invalid or inactive API key")
        
        return (None, key)
