class Client:
    def __init__(self, client_id, first_name, last_name, email, phone, address,
                 registration_date, company, loyalty_level, notes):
        self.client_id = client_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.address = address
        self.registration_date = registration_date
        self.company = company
        self.loyalty_level = loyalty_level
        self.notes = notes

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_contact_info(self):
        return f"{self.email}, {self.phone}"

    def upgrade_loyalty(self, new_level):
        self.loyalty_level = new_level

    def add_note(self, note):
        self.notes += f"\n{note}"

    def get_summary(self):
        return f"{self.get_full_name()} — {self.loyalty_level} клієнт, компанія: {self.company or 'фіз. особа'}"


clients = {}

clients[1] = Client(1, "Олег", "Коваль", "oleg@mail.com", "0931111111", "вул. А, 1", "2023-01-10", "ТОВ А", "золотий", "")
clients[2] = Client(2, "Ірина", "Мельник", "iryna@mail.com", "0932222222", "вул. Б, 2", "2023-02-15", "", "срібний", "")
clients[3] = Client(3, "Андрій", "Сидоренко", "andriy@mail.com", "0933333333", "вул. В, 3", "2023-03-20", "ТОВ В", "бронзовий", "")
clients[4] = Client(4, "Марія", "Іванова", "maria@mail.com", "0934444444", "вул. Г, 4", "2023-04-05", "", "золотий", "")
clients[5] = Client(5, "Тарас", "Лисенко", "taras@mail.com", "0935555555", "вул. Д, 5", "2023-05-12", "ТОВ Д", "срібний", "")
clients[6] = Client(6, "Олена", "Гончар", "olena@mail.com", "0936666666", "вул. Е, 6", "2023-06-18", "", "бронзовий", "")
clients[7] = Client(7, "Богдан", "Романюк", "bogdan@mail.com", "0937777777", "вул. Ж, 7", "2023-07-22", "ТОВ Ж", "золотий", "")
clients[8] = Client(8, "Катерина", "Шевченко", "katya@mail.com", "0938888888", "вул. З, 8", "2023-08-30", "", "срібний", "")
clients[9] = Client(9, "Дмитро", "Захарченко", "dima@mail.com", "0939999999", "вул. І, 9", "2023-09-05", "ТОВ І", "бронзовий", "")
clients[10] = Client(10, "Світлана", "Кравець", "sveta@mail.com", "0931010101", "вул. Й, 10", "2023-10-10", "", "золотий", "")
clients[11] = Client(11, "Роман", "Петренко", "roman@mail.com", "0931212121", "вул. К, 11", "2023-11-15", "ТОВ К", "срібний", "")
clients[12] = Client(12, "Юлія", "Степаненко", "yulia@mail.com", "0931313131", "вул. Л, 12", "2023-12-20", "", "бронзовий", "")
clients[13] = Client(13, "Віталій", "Бондар", "vitaliy@mail.com", "0931414141", "вул. М, 13", "2024-01-25", "ТОВ М", "золотий", "")
clients[14] = Client(14, "Наталя", "Данилюк", "natasha@mail.com", "0931515151", "вул. Н, 14", "2024-02-28", "", "срібний", "")
clients[15] = Client(15, "Євген", "Мазур", "yevhen@mail.com", "0931616161", "вул. О, 15", "2024-03-30", "ТОВ О", "бронзовий", "")