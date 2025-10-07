class ShippingZone:
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
        return (f"Shipping Zone ID: {self.zone_id}, Type: {self.type}, Status: {self.status}, "
                f"Load: {self.current_load}/{self.capacity}, Queue: {self.queue_length}, "
                f"Worker: {self.assigned_worker.name if self.assigned_worker else 'Немає'}, "
                f"Location: {self.location}, Created: {self.created_date}, "
                f"Last update: {self.last_update}")

    def add_package(self):
        if self.current_load < self.capacity:
            self.current_load += 1
            self.queue_length = max(0, self.queue_length - 1)
        else:
            self.status = "перевантажена"

    def remove_package(self):
        if self.current_load > 0:
            self.current_load -= 1

    def update_status(self, new_status: str):
        self.status = new_status


shipping_zones = {}
shipping_zones[1] = ShippingZone(1, "експрес", 100, 80, "активна", None, "Зона A", 10, "2022-03-01", "2024-06-10")
shipping_zones[2] = ShippingZone(2, "стандарт", 150, 150, "перевантажена", None, "Зона B", 20, "2023-01-15", "2024-05-12")
shipping_zones[3] = ShippingZone(3, "міжнародна", 200, 120, "активна", None, "Зона C", 15, "2021-10-20", "2024-04-01")
shipping_zones[4] = ShippingZone(4, "експрес", 80, 60, "активна", None, "Зона D", 8, "2022-11-05", "2024-02-25")
shipping_zones[5] = ShippingZone(5, "стандарт", 120, 100, "активна", None, "Зона E", 5, "2023-05-10", "2024-03-18")