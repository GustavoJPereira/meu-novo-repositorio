class InMemoryTable():
        def __init__(self):
            self.lastId = -1;
            self.storage = {};

        def _nextId(self):
            self.lastId += 1;
            return self.lastId;

        def newRegistro(self, registro):
            id = _nextId()
            registro.id = id
            self.storage[id] == registro
        
        def getRegistro(self, id):
            if not self.storage[id]:
                raise Exception("id nao encontrado")
            return self.storage[id]
    
        def attRegistro(self, id, regitro):
            getRegistro(id)
            registro.id = id
            self.storage[id] = registro

        def getAll(self):
             return list(self.storage.values())