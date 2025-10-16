class ReceivingZone:
    def __init__(self, zone_id, type, capacity, location, assigned_worker,
                 current_load, status, queue_length, created_by, last_updated_by):
        self.zone_id = zone_id
        self.type = type
        self.capacity = capacity
        self.location = location
        self.assigned_worker = assigned_worker
        self.current_load = current_load
        self.status = status
        self.queue_length = queue_length
        self.created_by = created_by
        self.last_updated_by = last_updated_by

    def add_package(self, count):
        if self.current_load + count <= self.capacity:
            self.current_load += count
            self.queue_length += count
        else:
            self.status = "перевантажена"
        self.update_status()

    def remove_package(self, count):
        self.current_load = max(0, self.current_load - count)
        self.queue_length = max(0, self.queue_length - count)
        self.update_status()

    def update_status(self):
        if self.current_load == 0:
            self.status = "очікування"
        elif self.current_load >= self.capacity:
            self.status = "перевантажена"
        else:
            self.status = "активна"

    def assign_worker(self, worker_name):
        self.assigned_worker = worker_name
        self.last_updated_by = worker_name

    def get_info(self):
        return f"Зона {self.zone_id} ({self.type}) — {self.status}, пакунків: {self.current_load}"


zones = {}
zones[1] = ReceivingZone(1, "митна", 100, "A", "Іван", 20, "активна", 5, "admin", "Іван")
zones[2] = ReceivingZone(2, "внутрішня", 80, "B", "Олена", 0, "очікування", 0, "admin", "Олена")
zones[3] = ReceivingZone(3, "експрес", 50, "C", "Петро", 50, "перевантажена", 10, "admin", "Петро")
zones[4] = ReceivingZone(4, "митна", 120, "D", "Марія", 60, "активна", 8, "admin", "Марія")
zones[5] = ReceivingZone(5, "внутрішня", 90, "E", "Андрій", 30, "активна", 3, "admin", "Андрій")
zones[6] = ReceivingZone(6, "експрес", 40, "F", "Юлія", 0, "очікування", 0, "admin", "Юлія")
zones[7] = ReceivingZone(7, "митна", 110, "G", "Богдан", 110, "перевантажена", 12, "admin", "Богдан")
zones[8] = ReceivingZone(8, "внутрішня", 70, "H", "Катерина", 20, "активна", 2, "admin", "Катерина")
zones[9] = ReceivingZone(9, "експрес", 60, "I", "Олег", 60, "перевантажена", 6, "admin", "Олег")
zones[10] = ReceivingZone(10, "митна", 95, "J", "Наталя", 45, "активна", 4, "admin", "Наталя")
zones[11] = ReceivingZone(11, "внутрішня", 85, "K", "Роман", 0, "очікування", 0, "admin", "Роман")
zones[12] = ReceivingZone(12, "експрес", 55, "L", "Ірина", 25, "активна", 3, "admin", "Ірина")
zones[13] = ReceivingZone(13, "митна", 100, "M", "Тарас", 100, "перевантажена", 9, "admin", "Тарас")
zones[14] = ReceivingZone(14, "внутрішня", 75, "N", "Світлана", 35, "активна", 5, "admin", "Світлана")
zones[15] = ReceivingZone(15, "експрес", 65, "O", "Дмитро", 10, "активна", 1, "admin", "Дмитро")