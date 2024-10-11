import datetime
import jwt

Secret_key = "clave_token"
def generar_token():
    payload = {
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1),
        'iat': datetime.datetime.utcnow(),
        'sub': 'microservicio_2'
    }
    return jwt.encode(payload, SECRET_KEY, algorithm='HS256')