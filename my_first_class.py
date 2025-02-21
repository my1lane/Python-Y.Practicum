class Phone():
    
    line_type = 'проводной'
    
    def __init__(self, dial_type_value):
        self.dial_type = dial_type_value
        
    def ring(self):
        print('Дззззыыыыыынь!')
        
    def call(self, phone_number):
        print(f'Звоню по номеру {phone_number}! Тип связи - {self.line_type}.')
        
    def get_missed_calls(self):
        print('Запрос количества пропущенных вызовов.')
        
rotary_phone = Phone(dial_type_value='дисковый')

rotary_phone.get_missed_calls()