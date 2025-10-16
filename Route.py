class Route:
    def __init__(self, route_id, start_point, end_point, distance, assigned_vehicle,
                 status, checkpoints, created_by, last_updated_by, route_type):
        self.route_id = route_id
        self.start_point = start_point
        self.end_point = end_point
        self.distance = distance
        self.assigned_vehicle = assigned_vehicle
        self.status = status
        self.checkpoints = checkpoints
        self.created_by = created_by
        self.last_updated_by = last_updated_by
        self.route_type = route_type

    def calculate_time(self):
        return round(self.distance / 60, 2)

    def add_checkpoint(self, point):
        self.checkpoints.append(point)
        self.last_updated_by = "system"

    def block_route(self):
        self.status = "заблокований"
        self.last_updated_by = "admin"

    def activate_route(self):
        self.status = "активний"
        self.last_updated_by = "admin"

    def get_summary(self):
        return f"{self.start_point} → {self.end_point}, {self.distance} км"


routes = {}
routes[1] = Route(1, "Склад A", "Клієнт 1", 120, "Фургон 1", "активний", [], "admin", "system", "міжміський")
routes[2] = Route(2, "Склад B", "Клієнт 2", 80, "Фургон 2", "активний", [], "admin", "system", "локальний")
routes[3] = Route(3, "Склад C", "Клієнт 3", 150, "Фургон 3", "заблокований", [], "admin", "system", "міжміський")
routes[4] = Route(4, "Склад D", "Клієнт 4", 60, "Фургон 4", "активний", [], "admin", "system", "локальний")
routes[5] = Route(5, "Склад E", "Клієнт 5", 200, "Фургон 5", "активний", [], "admin", "system", "міжміський")
routes[6] = Route(6, "Склад F", "Клієнт 6", 90, "Фургон 6", "активний", [], "admin", "system", "локальний")
routes[7] = Route(7, "Склад G", "Клієнт 7", 110, "Фургон 7", "активний", [], "admin", "system", "міжміський")
routes[8] = Route(8, "Склад H", "Клієнт 8", 70, "Фургон 8", "заблокований", [], "admin", "system", "локальний")
routes[9] = Route(9, "Склад I", "Клієнт 9", 130, "Фургон 9", "активний", [], "admin", "system", "міжміський")
routes[10] = Route(10, "Склад J", "Клієнт 10", 50, "Фургон 10", "активний", [], "admin", "system", "локальний")
routes[11] = Route(11, "Склад K", "Клієнт 11", 160, "Фургон 11", "активний", [], "admin", "system", "міжміський")
routes[12] = Route(12, "Склад L", "Клієнт 12", 85, "Фургон 12", "активний", [], "admin", "system", "локальний")
routes[13] = Route(13, "Склад M", "Клієнт 13", 140, "Фургон 13", "заблокований", [], "admin", "system", "міжміський")
routes[14] = Route(14, "Склад N", "Клієнт 14", 95, "Фургон 14", "активний", [], "admin", "system", "локальний")
routes[15] = Route(15, "Склад O", "Клієнт 15", 180, "Фургон 15", "активний", [], "admin", "system", "міжміський")