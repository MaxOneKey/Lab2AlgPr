class SortingRobot:
    def __init__(self, robot_id: int, model: str, status: str, battery_level: int,
                 max_load: float, location: str, assigned_task: str, software_version: str,
                 last_service_date: str, speed: float):
        self.robot_id = robot_id
        self.model = model
        self.status = status
        self.battery_level = battery_level
        self.max_load = max_load
        self.location = location
        self.assigned_task = assigned_task
        self.software_version = software_version
        self.last_service_date = last_service_date
        self.speed = speed

    def get_info(self):
        return (f"Robot ID: {self.robot_id}, Model: {self.model}, Status: {self.status}, "
                f"Battery: {self.battery_level}%, Max load: {self.max_load}kg, "
                f"Location: {self.location}, Task: {self.assigned_task}, "
                f"Software: {self.software_version}, Last service: {self.last_service_date}, "
                f"Speed: {self.speed} m/s")

    def update_status(self, new_status: str):
        self.status = new_status

    def charge_battery(self, amount: int):
        self.battery_level = min(100, self.battery_level + amount)

    def move_to(self, new_location: str):
        self.location = new_location

    def assign_task(self, task: str):
        self.assigned_task = task
        self.status = "в роботі"

robots = {}
robots[201] = SortingRobot(201, "SR-100", "очікування", 80, 50, "Зона A", None, "v1.2", "2024-05-10", 1.5)
robots[202] = SortingRobot(202, "SR-200", "в роботі", 50, 60, "Зона B", "сортування пакунків", "v1.3", "2024-04-20", 2.0)
robots[203] = SortingRobot(203, "SR-150", "зарядка", 20, 55, "Станція зарядки", None, "v1.1", "2024-03-15", 1.8)
robots[204] = SortingRobot(204, "SR-300", "очікування", 90, 70, "Зона C", None, "v1.4", "2024-06-01", 2.5)
robots[205] = SortingRobot(205, "SR-250", "в роботі", 60, 65, "Зона D", "переміщення вантажів", "v1.2", "2024-05-25", 2.2)