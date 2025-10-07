class Drone:
    def __init__(self, drone_id: int, model: str, battery_capacity: int, payload_capacity: float,
                 range: float, status: str, current_location: str, software_version: str,
                 last_service_date: str, assigned_task: str = None):
        self.drone_id = drone_id
        self.model = model
        self.battery_capacity = battery_capacity
        self.payload_capacity = payload_capacity
        self.range = range
        self.status = status
        self.current_location = current_location
        self.software_version = software_version
        self.last_service_date = last_service_date
        self.assigned_task = assigned_task

    def get_info(self):
        return (f"Drone ID: {self.drone_id}, Model: {self.model}, Battery: {self.battery_capacity}%, "
                f"Payload: {self.payload_capacity}kg, Range: {self.range}km, Status: {self.status}, "
                f"Location: {self.current_location}, Task: {self.assigned_task}, "
                f"Software: {self.software_version}, Last service: {self.last_service_date}")

    def update_status(self, new_status: str):
        self.status = new_status

    def assign_task(self, task: str):
        self.assigned_task = task
        self.status = "в роботі"

    def update_location(self, new_location: str):
        self.current_location = new_location

    def charge_battery(self, amount: int):
        self.battery_capacity = min(100, self.battery_capacity + amount)


drones = {}
drones[1] = Drone(1, "kozak XXI", 241, 90, 10, 15, "очікує", "Склад A", "v1.5", "2024-05-15")
drones[2] = Drone(2, "kozak XX", 60, 8, 12, "в роботі", "Маршрут 3", "v1.3", "2024-03-20", "доставка пакунку 103")
drones[3] = Drone(3, "kozak XII", 30, 12, 18, "зарядка", "Станція 2", "v1.6", "2024-02-10")
drones[4] = Drone(4, "kozak IX", 75, 15, 25, "очікує", "Склад C", "v1.4", "2024-06-01")
drones[5] = Drone(5, "kozak X", 50, 20, 30, "в роботі", "Маршрут 5", "v1.7", "2024-04-10", "перевезення матеріалів")