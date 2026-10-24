class Subject:
    def __init__(self, subid, subnameth, subnnameen, subunit, sublect, sublab):
        self.subid = subid
        self.subnameth = subnameth
        self.subnnameen = subnnameen
        self.subunit = subunit
        self.sublect = sublect
        self.sublab = sublab
    def __str__(self) -> str:
        return f"({self.subid} {self.subnameth} {self.subnnameen} {self.subunit} {self.sublect} {self.sublab})"
    
    @property
    def subid(self):
        return self.__subid
    @subid.setter
    def subid(self, value):
        self.__subid = value
        
    @property
    def subnameth(self):
        return self.__subnameth
    @subnameth.setter
    def subnameth(self, value):
        self.__subnameth = value
        
    @property
    def subnnameen(self):
        return self.__subnnameen
    @subnnameen.setter
    def subnnameen(self, value):
        self.__subnnameen = value
        
    @property
    def subunit(self):
        return self.__subunit
    @subunit.setter
    def subunit(self, value):
        self.__subunit = value
        
    @property
    def sublect(self):
        return self.__sublect
    @sublect.setter
    def sublect(self, value):
        self.__sublect = value
        
    @property
    def sublab(self):
        return self.__sublab
    @sublab.setter
    def sublab(self, value):
        self.__sublab = value