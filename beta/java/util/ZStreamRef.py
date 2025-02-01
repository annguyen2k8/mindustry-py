import threading
class ZStreamRef:
    __address:int
    
    def __init__(self, address):
        self.__address = address
        self.lock = threading.Lock()

    def __enter__(self):
        self.lock.acquire()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.lock.release()
    
    @property
    def address(self):
        return self.__address
    
    def clear(self) -> None:
        self.__address = 0