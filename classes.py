from collections import UserDict


class Record:   
    
    def __init__(self, name: str, phone = None) -> None:
        self.phones = set()
        self.name = Name(name)        
        if phone:
             self.phones.add(Phone(phone).value)
        self.user_record = {self.name.value: self.phones}

    def add_phone(self, phone):
        self.user_record.get(self.name.value).add(phone)
        return self.user_record
    
    def remove_phone(self, phone):
        self.user_record.get(self.name.value).discard(phone)
        return self.user_record
    
    def edit_phone(self, new_phone):
        # self.remove_phone(old_phone)
        self.add_phone(new_phone)
        return self.user_record


     
    def __str__(self) -> str:        
        return self.user_record
    
    # def __repr__(self) -> str:
    #     return str(self)


class Field:
    def __init__(self, value: str):
        self.value = value
    

class Name(Field):
    pass
        

class Phone(Field):
    pass


class AddressBook(UserDict):
    def add_record(self, record: Record):

        if record.name.value in self.data.keys():
            
            self.data[record.name.value].update(record.user_record[record.name.value])
        else:
            self.data[record.name.value] = record.user_record[record.name.value]
       
        # return self.data
        return f"User {record.name.value} has phone numbers: {self.data[record.name.value]}"

    def __str__(self) -> str:
        return self.data
    
 

# В этой домашней работе вы должны реализовать такие классы:

# Класс AddressBook, который наследуется от UserDict, и мы потом добавим логику поиска по записям в этот класс.
# Класс Record, который отвечает за логику добавления/удаления/редактирования необязательных полей и хранения обязательного поля Name.
# Класс Field, который будет родительским для всех полей, в нем потом реализуем логику общую для всех полей.
# Класс Name, обязательное поле с именем.
# Класс Phone, необязательное поле с телефоном и таких одна запись (Record) может содержать несколько.


# Критерии приёма

# Реализованы все классы из задания.
# Записи Record в AddressBook хранятся как значения в словаре. В качестве ключей используется значение Record.name.value.
# Record хранит объект Name в отдельном атрибуте.
# Record хранит список объектов Phone в отдельном атрибуте.
# Record реализует методы для добавления/удаления/редактирования объектов Phone.
# AddressBook реализует метод add_record, который добавляет Record в self.data.



    




