import pickle
from abc import ABC, abstractmethod
from excecoes.chave_invalida_error import ChaveInvalidaError

class DAO(ABC):
    @abstractmethod
    def __init__(self, datasource=''):
        self.__datasource = datasource
        self.__cache = {} 
        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()

    def __dump(self):
        pickle.dump(self.__cache, open(self.__datasource, 'wb'))

    def __load(self):
        self.__cache = pickle.load(open(self.__datasource,'rb'))

    
    def add(self, key, obj):
        self.__cache[key] = obj
        self.__dump()  

    
    def update(self, key, obj):
        try:
            if key in self.__cache:
                self.__cache[key] = obj 
                self.__dump()  
            else:
                raise ChaveInvalidaError()
        except KeyError:
            raise ChaveInvalidaError()

    def get(self, key):
        try:
            return self.__cache[key]
        except KeyError:
            raise ChaveInvalidaError()

    
    def remove(self, key):
        try:
            self.__cache.pop(key)
            self.__dump() 
        except KeyError:
            raise ChaveInvalidaError()

    def get_all(self):
        return list(self.__cache.values())