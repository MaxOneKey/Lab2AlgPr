class Truck:
    def __init__(self,truck_id:int,capacity_weight:int,capacity_volume:float,driver_name:str,status:str,arrival_time:str,departure_time:str,route_id:int,license_plate:str,fuel_type:str):
        self.truck_id = truck_id
        self.capacity_weight = capacity_weight
        self.capacity_volume = capacity_volume
        self.driver_name = driver_name
        self.status = status
        self.arrival_time = arrival_time
        self.departure_time = departure_time
        self.route_id = route_id
        self.license_plate = license_plate
        self.fuel_type = fuel_type

    def get_info(self):
        return (f"Truck ID: {self.truck_id}, Driver: {self.driver_name}, Status: {self.status}, "
                f"Capacity: {self.capacity_weight}kg/{self.capacity_volume}m3, Route: {self.route_id}, "
                f"License Plate: {self.license_plate}, Fuel: {self.fuel_type}")
    def update_status(self, new_status: str):
        self.status = new_status

    def is_available(self):
        return self.status.lower() == 'очікує'

    def get_route(self):
        return self.route_id

    def update_driver(self, new_driver_name: str):
        self.driver_name = new_driver_name
trucks = {}


trucks[101] = Truck(101, 8000, 20.5, "Іван Петренко", "очікує", "18:00", "22:00", 12, "AB1234CD", "diesel")
trucks[102] = Truck(102, 6000, 15.0, "Петро Коваль", "в дорозі", "16:30", "20:00", 15, "BC5678EF", "gasoline")
trucks[103] = Truck(103, 10000, 25.0, "Олег Сидоренко", "очікує", "19:00", "23:00", 18, "CD9012GH", "diesel")
trucks[104] = Truck(104, 12000, 30.0, "Микола Іванов", "в дорозі", "15:00", "19:00", 20, "DE3456IJ", "electric")
trucks[105] = Truck(105, 7000, 18.0, "Василь Кравченко", "очікує", "17:30", "21:00", 22, "EF7890KL", "gasoline")
trucks[106] = Truck(106, 9000, 22.0, "Андрій Шевченко", "в дорозі", "14:00", "18:00", 25, "FG1234MN", "diesel")
trucks[107] = Truck(107, 11000, 28.0, "Сергій Бондаренко", "очікує", "20:00", "00:00", 30, "GH5678OP", "diesel")
trucks[108] = Truck(108, 5000, 12.0, "Юрій Ткаченко", "в дорозі", "13:30", "17:00", 35, "HI9012QR", "gasoline")
trucks[109] = Truck(109, 13000, 32.0, "Олександр Литвин", "очікує", "21:00", "01:00", 40, "IJ3456ST", "electric")
trucks[110] = Truck(110, 7500, 19.0, "Володимир Романенко", "в дорозі", "12:00", "16:00", 45, "JK7890UV", "diesel")
trucks[111] = Truck(111, 8500, 21.0, "Дмитро Савченко", "очікує", "22:00", "02:00", 50, "KL1234WX", "gasoline")
trucks[112] = Truck(112, 9500, 23.0, "Артем Козак", "в дорозі", "11:30", "15:00", 55, "LM5678YZ", "diesel")
trucks[113] = Truck(113, 11500, 27.0, "Михайло Гончаренко", "очікує", "23:00", "03:00", 60, "MN9012AB", "electric")
trucks[114] = Truck(114, 6500, 16.0, "Олег Рибак", "в дорозі", "10:00", "14:00", 65, "NO3456CD", "gasoline")
trucks[115] = Truck(115, 10500, 26.0, "Роман Левченко", "очікує", "00:00", "04:00", 70, "OP7890EF", "diesel")
trucks[116] = Truck(116, 7200, 17.0, "Микола Савчук", "в дорозі", "09:30", "13:00", 75, "PQ1234GH", "gasoline")
trucks[117] = Truck(117, 9800, 24.0, "Віталій Кравчук", "очікує", "01:00", "05:00", 80, "QR5678IJ", "diesel")
trucks[118] = Truck(118, 8800, 22.5, "Євгеній Тимошенко", "в дорозі", "08:00", "12:00", 85, "RS9012KL", "gasoline")
trucks[119] = Truck(119, 7600, 19.5, "Станіслав Мороз", "очікує", "02:00", "06:00", 90, "ST3456MN", "diesel")
trucks[120] = Truck(120, 6800, 16.5, "Іван Бойко", "в дорозі", "07:30", "11:00", 95, "TU7890OP", "gasoline")
while True:
    cmd = input("Введи ID вантажівки: ")
    if cmd.lower() == "close":
        break
    if cmd.isdigit():
        id_to_find = int(cmd)
        if id_to_find in trucks:
            print(trucks[id_to_find].get_info())
        else:
            print("Вантажівку з таким ID не знайдено.")
    else:
        print("Невірне введення. Введи ID.")

