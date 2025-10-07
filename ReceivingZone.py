class ReceivingZone:
    def __init__(self, zone_id: int, type: str, capacity: int, current_load: int,
                 status: str, assigned_worker, location: str, queue_length: int,
                 created_date: str, last_update: str):
        self.zone_id = zone_id
        self.type = type
        self.capacity = capacity
        self.current_load = current_load
        self.status = status
        self.assigned_worker = assigned_worker
        self.location = location
        self.queue_length = queue_length
        self.created_date = created_date
        self.last_update = last_update

    def get_info(self):
        return (f"Receiving Zone ID: {self.zone_id}, Type: {self.type}, Status: {self.status}, "
                f"Load: {self.current_load}/{self.capacity}, Queue: {self.queue_length}, "
                f"Worker: {self.assigned_worker.name if self.assigned_worker else 'Немає'}, "
                f"Location: {self.location}, Created: {self.created_date}, "
                f"Last update: {self.last_update}") 
    
    def receive_package(self):
        if self.current_load < self.capacity:
            self.current_load += 1
        else:
            self.status = "перевантажена"

    def release_package(self):
        if self.current_load > 0:
            self.current_load -= 1

    def update_status(self, new_status: str):
        self.status = new_status


receiving_zones = {}
receiving_zones[1] = ReceivingZone(1, "митна", 80, 60, "активна", None, "Зона A", 5, "2022-05-01", "2024-06-12")
receiving_zones[2] = ReceivingZone(2, "внутрішня", 100, 95, "перевантажена", None, "Зона B", 12, "2021-12-10", "2024-04-30")
receiving_zones[3] = ReceivingZone(3, "експрес", 70, 40, "активна", None, "Зона C", 7, "2023-02-18", "2024-05-10")
receiving_zones[4] = ReceivingZone(4, "митна", 90, 85, "очікування", None, "Зона D", 9, "2022-08-25", "2024-03-22")
receiving_zones[5] = ReceivingZone(5, "внутрішня", 110, 100, "активна", None, "Зона E", 10, "2023-06-01", "2024-01-15")