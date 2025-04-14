class Phone:
    line_type = 'проводной'
    def __init__(self, dial_type_value):
        self.dial_type = dial_type_value

    def ring(self):
        print('Дзззззыыыыыыыынь!')

    def call(self, phone_number):
        print(f'Звоню по номеру {phone_number}! Тип связи - {self.line_type}.')

class MobilePhone(Phone):
    pass

mobile_phone = MobilePhone('сенсорный')

mobile_phone.ring()
