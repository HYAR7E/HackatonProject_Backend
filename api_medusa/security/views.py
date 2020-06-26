from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from master.models import User
from .models import Token
from .serializers import TokenSz


class GenerateToken(APIView):
    """
    Descripcion:
        A POST request to this view will return user's token
    Params:
        user (pk)
    """

    def post(self, req):
        # Verify request's data
        if 'nickname' not in req.data: raise ValidationError("nickname not specified")
        if 'password' not in req.data: raise ValidationError("password not specified")

        nickname = req.data['nickname']
        password = req.data['password']
        try:
            user = User.objects.get(nickname=nickname, password=password)
        except User.DoesNotExist:
            # User register with received pk does not exists
            return Response(
                data={"error_detail": "User does not exists"},
                status=400
            )

        # Token get_or_create
        token, new = Token.objects.get_or_create(user=user)
        token = TokenSz(token)  # Serialize token object
        # Login user
        user.loggged = True
        user.save()
        # Return token
        return Response(data=token.data, status=200)


class DeleteToken(APIView):
    """
    Descripcion:
        A POST request to this view will return user's token
    Params:
        user (pk)
    """

    def delete(self, req):
        user_pk = req.data['user']
        try:
            user = User.objects.get(pk=user_pk)
        except User.DoesNotExist:
            # User register with received pk does not exists
            return Response(
                data={"error_detail": "User does not exists"},
                status=400
            )

        # Token delete
        token, new = Token.objects.filter(user=user).delete()
        # Logout user
        user.loggged = False
        user.save()
        # Return token
        return Response(status=200)
