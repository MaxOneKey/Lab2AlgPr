import time
class Worker:
    def __init__(self, worker_id: int, name: str, role: str, shift: str):
        self.worker_id = worker_id
        self.name = name
        self.role = role
        self.shift = shift

    def get_info(self):
        return f"Worker ID: {self.worker_id}, Name: {self.name}, Role: {self.role}, Shift: {self.shift}"
class Cart:
    def __init__(self, cart_id, capacity_weight, capacity_volume, cart_type,status, current_location, assigned_worker,created_date, last_service_date, wheel_type):
        
        self.cart_id = cart_id
        self.capacity_weight = capacity_weight
        self.capacity_volume = capacity_volume
        self.cart_type = cart_type
        self.status = status
        self.current_location = current_location
        self.assigned_worker = assigned_worker
        self.created_date = created_date
        self.last_service_date = last_service_date
        self.wheel_type = wheel_type
    
    def get_info(self):
        return (f"Cart ID: {self.cart_id}, Type: {self.cart_type}, Status: {self.status}, "
                f"Location: {self.current_location}, Wheel type: {self.wheel_type}, "
                f"Worker: {self.assigned_worker.name if self.assigned_worker else 'Немає'}, "
                f"Created: {self.created_date}, Last service: {self.last_service_date}")

    def assign_worker(self, worker):
        self.assigned_worker = worker
        self.status = "зайнятий"
    
    def release(self):
        self.assigned_worker = None
        self.status = "вільний"

    def mark_as_broken(self):
        self.status = "зламаний"

    def move_to(self, new_location: str):
        self.current_location = new_location

    def is_available(self):
        return self.status == "вільний"

workers = {}
carts = {}

workers[1] = Worker(1, "Іван Іванов", "оператор", "денна")
workers[2] = Worker(2, "Петро Петров", "вантажник", "нічна")
workers[3] = Worker(3, "Сидір Сидоров", "оператор", "денна")
workers[4] = Worker(4, "Микола Миколенко", "вантажник", "нічна")
workers[5] = Worker(5, "Василь Васильов", "оператор", "денна")
workers[6] = Worker(6, "Олександр Олександров", "вантажник", "нічна")
workers[7] = Worker(7, "Дмитро Дмитренко", "оператор", "денна")
workers[8] = Worker(8, "Андрій Андрієнко", "вантажник", "нічна")
workers[9] = Worker(9, "Юрій Юрченко", "оператор", "денна")
workers[10] = Worker(10, "Сергій Сергієнко", "вантажник", "нічна")

carts[1]= Cart(1, 1000, 2.5, "електричний", "вільний", "Зона А", None, "2023-01-15", "2024-05-10", "пневматичні")
carts[2]= Cart(2, 1500, 3.0, "ручний", "вільний", "Зона B", None, "2023-02-20", "2024-04-15", "суцільнолиті")
carts[3]= Cart(3, 1200, 2.8, "електричний", "вільний", "Зона C", None, "2023-03-10", "2024-03-20", "пневматичні")
carts[4]= Cart(4, 2000, 4.0, "ручний", "вільний", "Зона D", None, "2023-01-25", "2024-02-28", "суцільнолиті")

def assign_worker_to_cart(cart, worker_list):
    if cart.assigned_worker:
        print(f"Візок {cart.cart_id} вже закріплено за {cart.assigned_worker.name}")
        choice = input("Хочеш замінити працівника? (так/ні): ")
        if choice.lower() != "так":
            return

    for worker in worker_list:
        if all(c.assigned_worker != worker for c in carts.values()):
            cart.assign_worker(worker)
            print(f"Візок {cart.cart_id} тепер використовує {worker.name}")
            return

    print("Вільного працівника немає")

while True:
    print("\nСловник візків:")
    for c in carts.values():
        print(f"ID {c.cart_id}: {c.cart_type}, Статус: {c.status}, Працівник: {c.assigned_worker.name if c.assigned_worker else 'Немає'}")

    id_input = input("\nВведи ID візка (або 'exit' для виходу): ")
    if id_input.lower() == "exit":
        break

    if not id_input.isdigit():
        print("Введи число")
        time.sleep(2)
        continue

    id_cart = int(id_input)
    if id_cart not in carts:
        print("Такого візка немає")
        time.sleep(2)
        continue

    cart = carts[id_cart]

    command = input("Введи команду (get_info / assign_worker): ")

    if command.lower() == "get_info":
        print(cart.get_info())
    elif command.lower() == "assign_worker":
        assign_worker_to_cart(cart, list(workers.values()))
    else:
        print("Невідома команда")
    time.sleep(2)
