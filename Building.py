class Building:
    def __init__(self, buid, buname):
        self.__buid = buid                  
        self.__buname = buname               

    def __str__(self) -> str:
        return f"{self.buname} (อาคาร {self.buid})"
    
    @property
    def buid(self):
        return self.__buid
    
    @buid.setter
    def buid(self, value):
        self.__buid = value
        
    @property
    def buname(self):
        return self.__buname
    
    @buname.setter
    def buname(self, value):
        self.__buname = value