from django.contrib.auth.models import User
from django.conf import settings

from rest_framework.authentication import BasicAuthentication
from rest_framework.exceptions import AuthenticationFailed


import jwt

class JWTAuthentication(BasicAuthentication):

    def authenicate(self, request):

        header = request.headers.get('Authorization')

        if not header:
            return None # This request is not authenticated.

        if not header.startswith('Bearer'):
            # Send a 401 response
            raise AuthenticationFailed({'message': 'Invalid Authorization header'})

        token = header.replace('Bearer ', '') # Get the token from the header.

        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            user = User.objects.get(pk=payload.get('sub'))
        except jwt.exceptions.InvalidTokenError:
            raise AuthenticationFailed({'message': 'Invalid token'})
        except User.DoesNotExist:
            raise AuthenticationFailed({'message': 'Invalid subject'})

        # 'authenticate' should return a tuple is auth is successful
        # The first element is the user, the second is the token (if used).
        # request.user will be the user.
        # request.token will be the token.
        return (user, token)
