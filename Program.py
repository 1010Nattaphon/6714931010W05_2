class Program:
    def __init__(self, short_name, name_th, name_en):
        self.short_name = short_name     
        self.name_th = name_th           
        self.name_en = name_en            
        
    def __str__(self) -> str:
        return f"{self.name_th} ({self.short_name})"
    @property
    def id(self): return self.__id
    @id.setter
    def id(self, value): self.__id = value

    @property
    def name_th(self): return self.__name_th
    @name_th.setter
    def name_th(self, value): self.__name_th = value

    @property
    def name_en(self): return self.__name_en
    @name_en.setter
    def name_en(self, value): self.__name_en = value

    @property
    def short_name(self): return self.__short_name
    @short_name.setter
    def short_name(self, value): self.__short_name = value