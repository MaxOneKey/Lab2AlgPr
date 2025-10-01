class Package:
    def __init__(self, package_id: int, weight: float, volume: float, cargo_type: str,
                 priority: int, storage_temperature: float, destination_point: str,
                 status: str, arrival_time: str, dispatch_time: str):
        self.package_id = package_id
        self.weight = weight
        self.volume = volume
        self.cargo_type = cargo_type
        self.priority = priority
        self.storage_temperature = storage_temperature
        self.destination_point = destination_point
        self.status = status
        self.arrival_time = arrival_time
        self.dispatch_time = dispatch_time

    def get_info(self):
        return (f"Package ID: {self.package_id}, Type: {self.cargo_type}, Weight: {self.weight}kg, "
                f"Volume: {self.volume}m3, Priority: {self.priority}, "
                f"Storage Temp: {self.storage_temperature}°C, Destination: {self.destination_point}, "
                f"Status: {self.status}, Arrival: {self.arrival_time}, Dispatch: {self.dispatch_time}")

    def update_status(self, new_status: str):
        self.status = new_status

    def set_arrival_time(self, new_time: str):
        self.arrival_time = new_time

    def set_dispatch_time(self, new_time: str):
        self.dispatch_time = new_time

    def set_destination(self, new_destination: str):
        self.destination_point = new_destination

packages = {}

packages[101] = Package(101, 10, 0.5, "стандартний", 1, 20, "Склад A", "прийнятий", "08:00", "12:00")
packages[102] = Package(102, 5, 0.2, "крихкий", 2, 5, "Склад B", "обробляється", "09:30", "13:00")
packages[103] = Package(103, 15, 1.0, "небезпечний", 3, -5, "Склад C", "прийнятий", "10:00", "14:00")
packages[104] = Package(104, 8, 0.3, "стандартний", 1, 15, "Склад D", "відправлений", "07:45", "11:30")
packages[105] = Package(105, 12, 0.7, "крихкий", 2, 10, "Склад B", "обробляється", "11:15", "15:00")
packages[106] = Package(106, 20, 1.5, "небезпечний", 3, -10, "Склад A", "прийнятий", "12:00", "16:30")
packages[107] = Package(107, 7, 0.4, "стандартний", 1, 18, "Склад C", "відправлений", "08:30", "12:15")
packages[108] = Package(108, 9, 0.6, "крихкий", 2, 8, "Склад D", "обробляється", "10:45", "14:30")
packages[109] = Package(109, 14, 1.2, "небезпечний", 3, -3, "Склад B", "прийнятий", "09:00", "13:45")
packages[110] = Package(110, 6, 0.25, "стандартний", 1, 22, "Склад A", "відправлений", "07:30", "11:00")
packages[111] = Package(111, 11, 0.8, "крихкий", 2, 12, "Склад C", "обробляється", "11:00", "15:30")
packages[112] = Package(112, 18, 1.3, "небезпечний", 3, -7, "Склад D", "прийнятий", "12:30", "17:00")
packages[113] = Package(113, 4, 0.15, "стандартний", 1, 25, "Склад B", "відправлений", "08:15", "11:45")
packages[114] = Package(114, 13, 0.9, "крихкий", 2, 7, "Склад A", "обробляється", "10:00", "14:15")
packages[115] = Package(115, 16, 1.1, "небезпечний", 3, -2, "Склад C", "прийнятий", "09:45", "13:30")


