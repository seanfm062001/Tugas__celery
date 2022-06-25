from nameko.rpc import rpc
import time
from prima import getprima, prima
from palindrom import getpalindrom, palindrom
from celery.result import AsyncResult

from nameko.rpc import rpc
import pickle
import dependencies


class RoomService:

    name = 'user_service'

    database = dependencies.Database()

    @rpc
    def add_user(self,username,password):
        add = self.database.add_user(username,password)
        return add

    @rpc
    def check_user(self,user_data):
        add = self.database.check_user(user_data)
        return add

    @rpc
    def set_session(self,user_data):
        add = self.database.set_session(user_data)
        return add

    @rpc
    def generate_session_id(self,user_data):
        add = self.database.generate_session_id()
        return add

    @rpc
    def delete_session(self,session_id):
        add = self.database.delete_session(session_id)
        return add

    @rpc
    def prima(self, a):
        id = getprima.apply_async((a, 1))
        result = AsyncResult(id.id, app=prima)
        return result.get()
    
    @rpc
    def palindrom(self, a):
        id = getpalindrom.apply_async((a, 1))
        result = AsyncResult(id.id, app=palindrom)
        return result.get()
    
    

    