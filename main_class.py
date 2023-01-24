import re

class ExtractInfo:
    def __init__(self):
        self.email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b|\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[А-Я|а-я]{2,}\b'
        self.phone_regex = r'\b(?:\+?\d{1,3}[-.\s]?)?\(?(?:\d{3})?\)?[-.\s]?\d{3}[-.\s]?\d{4}\b|\b(?:\+?\d{1,3}[-.\s]?)?\(?(?:\d{3})?\)?[-.\s]?\d{3}[-.\s]?\d{2}[-.\s]?\d{2}\b'
        self.name_regex = r'[А-Я][а-я]+|[A-Z][a-z]+'

    def extract_info(self, text):
        email = re.findall(self.email_regex, text)
        phone = re.findall(self.phone_regex, text)
        name = re.findall(self.name_regex, text)

        data = {'name': name or None, 'email': email or None, 'phone': phone or None}
        return data

# создаем экземпляр класса
extractor = ExtractInfo()

text = "Меня зовут Марсель, мой адрес электронной почты marselle@example.com, и мой номер телефона +7 (999) 999-9999"
data = extractor.extract_info(text)
print(data)

# В этом коде функция extract_info() теперь является методом класса ExtractInfo, который использует регулярные выражения, 
# определенные в конструкторе класса. Это позволяет избежать дублирования кода и упрощает его поддержку
