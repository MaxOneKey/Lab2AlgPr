class Security:
    def __init__(self, guard_id, first_name, last_name, shift_type, assigned_zone,
                 contact_number, supervisor_id, status, rank, experience_years):
        self.guard_id = guard_id
        self.first_name = first_name
        self.last_name = last_name
        self.shift_type = shift_type
        self.assigned_zone = assigned_zone
        self.contact_number = contact_number
        self.supervisor_id = supervisor_id
        self.status = status
        self.rank = rank
        self.experience_years = experience_years
        self.equipment = []

    def patrol(self):
        self.status = "патруль"

    def return_to_post(self):
        self.status = "на посту"

    def add_equipment(self, item):
        self.equipment.append(item)

    def report(self):
        return f"{self.first_name} {self.last_name} — {self.status} у зоні {self.assigned_zone}"

    def get_contact(self):
        return self.contact_number


guards = {
    1: Security(1, "Олег", "Коваль", "денна", "Зона A", "0671111111", "M1", "на посту", "рядовий", 3),
    2: Security(2, "Ірина", "Мельник", "нічна", "Зона B", "0672222222", "M2", "патруль", "рядовий", 2),
    3: Security(3, "Андрій", "Сидоренко", "денна", "Зона C", "0673333333", "M3", "на посту", "старший", 5),
    4: Security(4, "Марія", "Іванова", "нічна", "Зона D", "0674444444", "M4", "на посту", "рядовий", 1),
    5: Security(5, "Тарас", "Лисенко", "денна", "Зона E", "0675555555", "M5", "патруль", "рядовий", 4),
    6: Security(6, "Олена", "Гончар", "нічна", "Зона F", "0676666666", "M6", "на посту", "рядовий", 2),
    7: Security(7, "Богдан", "Романюк", "денна", "Зона G", "0677777777", "M7", "на посту", "старший", 6),
    8: Security(8, "Катерина", "Шевченко", "нічна", "Зона H", "0678888888", "M8", "патруль", "рядовий", 3),
    9: Security(9, "Дмитро", "Захарченко", "денна", "Зона I", "0679999999", "M9", "на посту", "рядовий", 1),
    10: Security(10, "Світлана", "Кравець", "нічна", "Зона J", "0671010101", "M10", "на посту", "рядовий", 2),
    11: Security(11, "Роман", "Петренко", "денна", "Зона K", "0671212121", "M11", "патруль", "рядовий", 4),
    12: Security(12, "Юлія", "Степаненко", "нічна", "Зона L", "0671313131", "M12", "на посту", "старший", 5),
    13: Security(13, "Віталій", "Бондар", "денна", "Зона M", "0671414141", "M13", "на посту", "рядовий", 3),
    14: Security(14, "Наталя", "Данилюк", "нічна", "Зона N", "0671515151", "M14", "патруль", "рядовий", 2),
    15: Security(15, "Євген", "Мазур", "денна", "Зона O", "0671616161", "M15", "на посту", "рядовий", 1)
}