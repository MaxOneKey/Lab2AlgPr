class ShiftManager:
    def __init__(self, manager_id, first_name, last_name, shift_type, contact_number,
                 email, status, department, notes, zone):
        self.manager_id = manager_id
        self.first_name = first_name
        self.last_name = last_name
        self.shift_type = shift_type
        self.contact_number = contact_number
        self.email = email
        self.status = status
        self.department = department
        self.notes = notes
        self.zone = zone
        self.assigned_workers = []
        self.responsibilities = []

    def assign_worker(self, worker_name):
        self.assigned_workers.append(worker_name)

    def add_responsibility(self, task):
        self.responsibilities.append(task)

    def go_on_leave(self):
        self.status = "у відпустці"

    def return_from_leave(self):
        self.status = "активний"

    def get_profile(self):
        return f"{self.first_name} {self.last_name} — {self.shift_type}, {self.status}"


managers = {}
managers[1] = ShiftManager(1, "Олег", "Коваль", "денна", "0501111111", "oleg@mail.com", "активний", "логістика", "", "Зона A")
managers[2] = ShiftManager(2, "Ірина", "Мельник", "нічна", "0502222222", "iryna@mail.com", "активний", "логістика", "", "Зона B")
managers[3] = ShiftManager(3, "Андрій", "Сидоренко", "денна", "0503333333", "andriy@mail.com", "у відпустці", "логістика", "", "Зона C")
managers[4] = ShiftManager(4, "Марія", "Іванова", "нічна", "0504444444", "maria@mail.com", "активний", "логістика", "", "Зона D")
managers[5] = ShiftManager(5, "Тарас", "Лисенко", "денна", "0505555555", "taras@mail.com", "активний", "логістика", "", "Зона E")
managers[6] = ShiftManager(6, "Олена", "Гончар", "нічна", "0506666666", "olena@mail.com", "активний", "логістика", "", "Зона F")
managers[7] = ShiftManager(7, "Богдан", "Романюк", "денна", "0507777777", "bogdan@mail.com", "активний", "логістика", "", "Зона G")
managers[8] = ShiftManager(8, "Катерина", "Шевченко", "нічна", "0508888888", "katya@mail.com", "активний", "логістика", "", "Зона H")
managers[9] = ShiftManager(9, "Дмитро", "Захарченко", "денна", "0509999999", "dima@mail.com", "активний", "логістика", "", "Зона I")
managers[10] = ShiftManager(10, "Світлана", "Кравець", "нічна", "0501010101", "sveta@mail.com", "активний", "логістика", "", "Зона J")
managers[11] = ShiftManager(11, "Роман", "Петренко", "денна", "0501212121", "roman@mail.com", "активний", "логістика", "", "Зона K")
managers[12] = ShiftManager(12, "Юлія", "Степаненко", "нічна", "0501313131", "yulia@mail.com", "активний", "логістика", "", "Зона L")
managers[13] = ShiftManager(13, "Віталій", "Бондар", "денна", "0501414141", "vitaliy@mail.com", "активний", "логістика", "", "Зона M")
managers[14] = ShiftManager(14, "Наталя", "Данилюк", "нічна", "0501515151", "natasha@mail.com", "активний", "логістика", "", "Зона N")
managers[15] = ShiftManager(15, "Євген", "Маз