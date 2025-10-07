class StorageSystem:
    def __init__(self, storage_id: int, type: str, capacity_weight: float, capacity_volume: float,
                 temperature: float, status: str, location: str, created_date: str,
                 last_service_date: str, operator_id: int):
        self.storage_id = storage_id
        self.type = type
        self.capacity_weight = capacity_weight
        self.capacity_volume = capacity_volume
        self.temperature = temperature
        self.status = status
        self.location = location
        self.created_date = created_date
        self.last_service_date = last_service_date
        self.operator_id = operator_id

    def get_info(self):
        return (f"Storage ID: {self.storage_id}, Type: {self.type}, Status: {self.status}, "
                f"Capacity: {self.capacity_weight}kg / {self.capacity_volume}m³, "
                f"Temp: {self.temperature}°C, Location: {self.location}, "
                f"Operator ID: {self.operator_id}, Created: {self.created_date}, "
                f"Last service: {self.last_service_date}")

    def update_status(self, new_status: str):
        self.status = new_status

    def update_temperature(self, new_temp: float):
        self.temperature = new_temp

    def service(self, date: str):
        self.last_service_date = date
        self.status = "в обслуговуванні"

    def is_available(self):
        return self.status == "доступна"


storages = {}
storages[1] = StorageSystem(1, "холодильна", 20000, 500, -5, "доступна", "Зона A", "2022-01-15", "2024-05-10", 1)
storages[2] = StorageSystem(2, "суха", 15000, 600, 20, "заповнена", "Зона B", "2021-09-20", "2024-04-15", 2)
storages[3] = StorageSystem(3, "автоматизована", 25000, 800, 18, "доступна", "Зона C", "2023-02-10", "2024-03-22", 3)
storages[4] = StorageSystem(4, "суха", 12000, 400, 22, "в ремонті", "Зона D", "2020-12-05", "2024-02-01", 4)
storages[5] = StorageSystem(5, "холодильна", 18000, 450, -10, "доступна", "Зона E", "2022-07-25", "2024-01-10", 5)