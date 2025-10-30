from dataclasses import dataclass, field
from typing import Optional, List, Any, Dict, Set


@dataclass
class Truck:
    id: int
    license_plate: str
    capacity: int
    status: str
    driver_id: Optional[int] = None
    assigned_routes: List[int] = field(default_factory=list)

@dataclass
class Route:
    id: int
    start_point: str
    end_point: str
    distance_km: float
    status: str
    assigned_trucks: List[int] = field(default_factory=list)

@dataclass
class ReceivingZone:
    id: int
    name: str
    capacity: int
    current_load: int = 0
    worker_id: Optional[int] = None

@dataclass
class ShippingZone:
    id: int
    name: str
    capacity: int
    current_load: int = 0
    worker_id: Optional[int] = None

@dataclass
class StorageSystem:
    id: int
    name: str
    type: str
    capacity: int
    current_load: int = 0
    zone: Optional[str] = None


@dataclass
class Worker:
    id: int
    name: str
    email: str
    phone: str
    position: str


workers = [
    Worker(1, "Іван Іванов", "ivan@m.com", "0931111111", "оператор"),
    Worker(2, "Олег Коваль", "oleg@m.com", "0671111111", "охоронець"),
    Worker(3, "Андрій Сидоренко", "andriy@m.com", "0503333333", "менеджер зміни"),
    Worker(4, "Марія Левченко", "maria@m.com", "0634444444", "логіст"),
    Worker(5, "Віктор Петренко", "viktor@m.com", "0505555555", "комірник"),
    Worker(6, "Юлія Кравченко", "yuliya@m.com", "0976666666", "диспетчер"),
    Worker(7, "Петро Коваль", "petro@m.com", "0997777777", "водій"),
]

trucks = [
    Truck(101, "AA1111BB", 1000, "вільна"),
    Truck(102, "CC2222DD", 1200, "вільна"),
]

routes = [
    Route(201, "Склад 1", "Магазин A", 15.5, "активний"),
    Route(202, "Склад 2", "Магазин B", 25.0, "активний"),
]

receiving_zones = [
    ReceivingZone(301, "Зона A", 500),
    ReceivingZone(302, "Зона B", 300),
]

shipping_zones = [
    ShippingZone(401, "Зона C", 400),
    ShippingZone(402, "Зона D", 350),
]

storage_systems = [
    StorageSystem(501, "Склад 1", "холодильник", 1000, zone="Зона A"),
    StorageSystem(502, "Склад 2", "сухий", 800, zone="Зона B"),
]


ENTITY_LISTS: Dict[str, List[Any]] = {
    "Truck": trucks,
    "Route": routes,
    "ReceivingZone": receiving_zones,
    "ShippingZone": shipping_zones,
    "StorageSystem": storage_systems,
}

WORKER_ASSIGNMENT_TARGETS: Dict[str, List[Any]] = {
    "Truck": trucks,
    "ReceivingZone": receiving_zones,
    "ShippingZone": shipping_zones,
}

ALLOWED_ROLES: Dict[str, List[str]] = {
    "Truck": ["водій"],
    "ReceivingZone": ["комірник", "логіст"],
    "ShippingZone": ["комірник", "логіст"],
}


def get_assigned_worker_ids() -> Set[int]:
    assigned_ids = set()
    for entity_list in WORKER_ASSIGNMENT_TARGETS.values():
        for item in entity_list:
            if hasattr(item, 'worker_id') and item.worker_id is not None:
                assigned_ids.add(item.worker_id)
            elif hasattr(item, 'driver_id') and item.driver_id is not None:
                assigned_ids.add(item.driver_id)
    return assigned_ids

def get_unassigned_workers() -> List[Worker]:
    assigned_ids = get_assigned_worker_ids()
    return [w for w in workers if w.id not in assigned_ids]

def find_worker_by_id(worker_id: int) -> Optional[Worker]:
    return next((w for w in workers if w.id == worker_id), None)

def find_entity_by_id(entity_list: List[Any], entity_id: int) -> Optional[Any]:
    return next((e for e in entity_list if e.id == entity_id), None)

def display_entity_list(entity_list: List[Any], class_name: str, assignable: bool = False):
    print(f"\n--- Список об'єктів класу {class_name} ---")
    for entity in entity_list:
        worker_status = ""
        if hasattr(entity, 'worker_id'):
            worker_status = f"(Призначено: {entity.worker_id})" if entity.worker_id else "(ВІЛЬНО)"
        elif hasattr(entity, 'driver_id'):
            worker_status = f"(Водій: {entity.driver_id})" if entity.driver_id else "(ВІЛЬНО)"

        display_line = f"ID: {entity.id}"

     
        if class_name == "Truck":
            display_line += f" (Ліцензія: {entity.license_plate}, Ємність: {entity.capacity}, Статус: {entity.status})"
        elif class_name == "Route":
            display_line += f" (Маршрут: {entity.start_point} → {entity.end_point}, Дистанція: {entity.distance_km} км, Статус: {entity.status})"
        elif class_name in ["ReceivingZone", "ShippingZone"]:
            display_line += f" (Назва: {entity.name}, Ємність: {entity.capacity}, Поточне навантаження: {entity.current_load})"
        elif class_name == "StorageSystem":
            display_line += f" (Назва: {entity.name}, Тип: {entity.type}, Ємність: {entity.capacity}, Поточне навантаження: {entity.current_load}, Зона: {entity.zone})"

        if assignable:
            display_line += f" {worker_status}"

        print(display_line)
    print("-" * 30)

def assign_worker_to_entity(class_name: str):
    entity_list = ENTITY_LISTS[class_name]
    unassigned = get_unassigned_workers()
    print(f"\nВільні працівники для {class_name}:")
    for w in unassigned:
        print(f"{w.id}: {w.name} ({w.position})")
    try:
        worker_id = int(input("Введіть ID працівника: "))
        worker = find_worker_by_id(worker_id)
        if not worker or worker.id not in [w.id for w in unassigned]:
            print("❌ Невірний працівник")
            return
        entity_id = int(input(f"Введіть ID об'єкта {class_name}: "))
        entity = find_entity_by_id(entity_list, entity_id)
        if not entity:
            print("❌ Об'єкт не знайдено")
            return
   
        if worker.position not in ALLOWED_ROLES[class_name]:
            print(f"❌ Працівник має роль '{worker.position}', потрібна: {ALLOWED_ROLES[class_name]}")
            return
        if hasattr(entity, 'worker_id'):
            entity.worker_id = worker.id
        elif hasattr(entity, 'driver_id'):
            entity.driver_id = worker.id
        print(f"✅ Працівник {worker.name} призначений на {class_name} ID {entity.id}")
    except ValueError:
        print("❌ Невірний ввід")

def assign_route_to_truck():
    display_entity_list(trucks, "Truck")
    display_entity_list(routes, "Route")
    try:
        truck_id = int(input("Введіть ID вантажівки: "))
        truck = find_entity_by_id(trucks, truck_id)
        if not truck:
            print("❌ Вантажівка не знайдена")
            return
        route_id = int(input("Введіть ID маршруту: "))
        route = find_entity_by_id(routes, route_id)
        if not route:
            print("❌ Маршрут не знайдено")
            return
        if route_id not in truck.assigned_routes:
            truck.assigned_routes.append(route_id)
        if truck_id not in route.assigned_trucks:
            route.assigned_trucks.append(truck_id)
        print(f"✅ Маршрут ID {route.id} призначено вантажівці ID {truck.id}")
    except ValueError:
        print("❌ Невірний ввід")


def menu_main():
    while True:
        print("\n" + "="*40)
        print("          СИСТЕМА УПРАВЛІННЯ СКЛАДОМ")
        print("="*40)
        print("1. Призначити працівника")
        print("2. Призначити маршрут вантажівці")
        print("3. Показати всі об'єкти")
        print("4. Вихід")
        choice = input("Ваш вибір: ")
        if choice == "1":
            print("Куди призначити працівника?")
            for i, c in enumerate(WORKER_ASSIGNMENT_TARGETS.keys()):
                print(f"{i+1}. {c}")
            try:
                cls_choice = int(input("Вибір: "))
                class_name = list(WORKER_ASSIGNMENT_TARGETS.keys())[cls_choice-1]
                assign_worker_to_entity(class_name)
            except:
                print("❌ Невірний ввід")
        elif choice == "2":
            assign_route_to_truck()
        elif choice == "3":
            for cls, lst in ENTITY_LISTS.items():
                display_entity_list(lst, cls)
        elif choice == "4":
            print("Вихід")
            break
        else:
            print("❌ Невірний вибір")

if __name__ == "__main__":
    menu_main()