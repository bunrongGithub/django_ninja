from cryptography.hazmat.backends.openssl import backend
from django.contrib.auth import get_user_model, authenticate
from ninja import Router
from ninja.orm import create_schema
from django.contrib.auth import login as django_login
router = Router()
_TGS = ["Django Ninja Auth"]
User = get_user_model()
UsernameSchemaMixin = create_schema(
    User, fields=[User.USERNAME_FIELD]
)


UserOut = create_schema(
    get_user_model(),exclude=["password"]
)


class LoginIn(UsernameSchemaMixin):
    password: str


_LOGIN_BACKEND = "django.contrib.auth.backends.ModelBackend"


@router.post("login", tags=_TGS, response={200: UserOut, 403: None}, auth=None)
def login(request, data: LoginIn):
    user = authenticate(backend=_LOGIN_BACKEND,**data.dict())
    if user is not None and user.is_active:
        django_login(request, user,backend=_LOGIN_BACKEND)
        return user
    return 403,None
