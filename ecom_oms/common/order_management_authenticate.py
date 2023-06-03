from rest_framework.authentication import get_authorization_header
from rest_framework import status
from django.http import JsonResponse


def order_management_authenticate(*args, **kwargs):
    ''' Authenticate Coupon Manager API '''
    def inner(request):
        try:
            token = verify_token_format(request)
        except Exception as e:
            # Convert the Exception response to JSON response
            return JsonResponse(e.__dict__['detail'], status=status.HTTP_401_UNAUTHORIZED)
        # Proceede with the url call
        return args[0](request)
    return inner


def verify_token_format(request):
    ''' Check Token from Header '''
    auth = get_authorization_header(request).split()

    if not auth or auth[0].lower() != b'token':
        msg = 'Invalid token header. No credentials provided.'
        # Status code for un-authorized token should be 401 (Un-Authorized)
        raise Exception(msg, status_code=status.HTTP_401_UNAUTHORIZED, name="Unauthorized")

    if len(auth) == 1:
        msg = 'Invalid token header. No token credentials provided.'
        raise Exception(msg, status_code=status.HTTP_401_UNAUTHORIZED, name="Unauthorized")
    elif len(auth) > 2:
        msg = 'Invalid token header'
        raise Exception(msg, status_code=status.HTTP_401_UNAUTHORIZED, name="Unauthorized")

    try:
        token = auth[1]
        if token=="null":
            msg = 'Null token not allowed'
            raise Exception(msg, status_code=status.HTTP_401_UNAUTHORIZED, name="Unauthorized")
    except UnicodeError:
        msg = 'Invalid token header. Token string should not contain invalid characters.'
        raise Exception(msg, status_code=status.HTTP_401_UNAUTHORIZED, name="Unauthorized")

    return authenticate_token_credentials(token)


def authenticate_token_credentials(token):
    ''' Authenticate Token credentials '''
    # For this instance making it hardcoded otherwise it should come from the environment variable
    pm_token = "pSaowjfdf2WPOkjr3o445ml098klmcpojfqPdoq3pweGF"

    if token.decode('ascii') == pm_token:
        return pm_token
    msg = "Invalid Token Signature"
    raise Exception(msg, status_code=status.HTTP_401_UNAUTHORIZED, name="Unauthorized")
