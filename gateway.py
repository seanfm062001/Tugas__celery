
import json
from nameko.rpc import RpcProxy
from nameko.web.handlers import http

from werkzeug.wrappers import Response
import uuid

from dependencies import SessionProvider


class GatewayService:
    name = 'gateway'

    user_rpc = RpcProxy('user_service')
    session_provider = SessionProvider()

    @http('GET', '/prima/<int:num>')
    def prima(self, request, num):
        cookies = request.cookies
        if cookies:
            result = self.user_rpc.prima(num)
            response = Response(
                json.dumps(result),
                mimetype='application/json'
            )
            return response

        else:
            response = Response('You need to Login First')
            return response
        

    @http('GET', '/prima/palindrom/<int:num>')
    def palindrom(self, request, num):
        cookies = request.cookies
        if cookies:
            result = self.user_rpc.palindrom(num)
            response = Response(
                json.dumps(result),
                mimetype='application/json'
            )
            return response
        else:
            response = Response('You need to Login First')
            return response

    @http('POST', '/register')
    def add_user(self, request):
        result = request.json
        user = result ["username"]
        kunci = result ["password"]
        nambahroom = self.user_rpc.add_user(user,kunci)
        return nambahroom

    @http('GET', '/logout')
    def logout_user(self, request):
        cookies = request.cookies
        if cookies:
            response = Response('success')
            response.delete_cookie('SESSID')
            self.session_provider.delete_session(cookies['SESSID'])
            return response
        else:
            response = Response('You need to Login First')
            return response

    @http('POST', '/login')
    def check_user(self, request):
        result = request.json
        user_data = {
            'username': result['username'],
            'password': result['password']
        }
        cekuser = self.user_rpc.check_user(user_data)
        if cekuser== 1 :
            session_id = self.session_provider.set_session(user_data)
            response = Response(str(user_data))
            response.set_cookie('SESSID', session_id)
            return response
        
        else :
             return "username atau password salah"

    
        
    
   

   
    