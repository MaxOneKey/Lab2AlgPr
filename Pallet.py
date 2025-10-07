class Pallet:
    def __init__(self, pallet_id: int, type: str, capacity_weight: float, current_weight: float,
                 status: str, stack_level: int, created_date: str, last_service_date: str,
                 location: str, barcode: str):
        self.pallet_id = pallet_id
        self.type = type
        self.capacity_weight = capacity_weight
        self.current_weight = current_weight
        self.status = status
        self.stack_level = stack_level
        self.created_date = created_date
        self.last_service_date = last_service_date
        self.location = location
        self.barcode = barcode

    def get_info(self):
        return (f"Pallet ID: {self.pallet_id}, Type: {self.type}, Status: {self.status}, "
                f"Weight: {self.current_weight}/{self.capacity_weight}kg, Stack level: {self.stack_level}, "
                f"Location: {self.location}, Barcode: {self.barcode}, "
                f"Created: {self.created_date}, Last service: {self.last_service_date}")

    def load(self, weight: float):
        if self.current_weight + weight <= self.capacity_weight:
            self.current_weight += weight
            self.status = "завантажена"
        else:
            print("Перевищення вантажопідйомності!")

    def unload(self):
        self.current_weight = 0
        self.status = "вільна"

    def move_to(self, new_location: str):
        self.location = new_location


pallets = {}
pallets[1] = Pallet(1, "дерев’яна", 1000, 500, "завантажена", 1, "2022-01-10", "2024-03-15", "Зона A", "PL001")
pallets[2] = Pallet(2, "пластикова", 1200, 0, "вільна", 2, "2023-02-18", "2024-04-20", "Зона B", "PL002")
pallets[3] = Pallet(3, "металева", 1500, 700, "завантажена", 1, "2021-11-25", "2024-02-05", "Зона C", "PL003")
pallets[4] = Pallet(4, "дерев’яна", 900, 0, "вільна", 3, "2022-03-05", "2024-01-30", "Зона D", "PL004")
pallets[5] = Pallet(5, "пластикова", 1100, 600, "завантажена", 2, "2023-07-12", "2024-05-12", "Зона E", "PL005")