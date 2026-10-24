from Program import Program

class Student:
    def __init__(self, std_id, firstname, lastname, program: Program):
        self.std_id = std_id              
        self.firstname = firstname        
        self.lastname = lastname         
        self.program = program              
        
    def __str__(self) -> str:
        return f"รหัส {self.std_id}: {self.firstname} {self.lastname} - สาขา {self.program.name_th}"
    @property
    def std_id(self):
        return self.__std_id
    @std_id.setter
    def std_id(self, value):
        self.__std_id = value

    @property
    def firstname(self):
        return self.__firstname
    @firstname.setter
    def firstname(self, value):
        self.__firstname = value

    @property
    def lastname(self):
        return self.__lastname
    @lastname.setter
    def lastname(self, value):
        self.__lastname = value

    @property
    def program(self):
        return self.__program
    @program.setter
    def program(self, value):
        self.__program = value