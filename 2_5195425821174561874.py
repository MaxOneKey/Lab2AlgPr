import sys
from dataclasses import dataclass, field
from typing import Optional, List, Any, Dict, Set


TRUCK_STATUSES = ["в дорозі", "доставлено", "на складі", "неактивний"]
ZONES = ["Зона A", "Зона B", "Зона C", "Склад 1"]
ROUTE_STATUSES = ["активний", "завершений"]
SHIPPING_TYPES = ["повітряний", "автомобільний", "дроновий"]
SHIFT_TYPES = ["денна", "нічна"]
WORKER_STATUSES = ["працює", "у відпустці", "на лікарняному"]
DEPARTMENTS = ["логістика", "комірник", "доставка"]
ROBOT_TASKS = ["сортування", "зарядка", "очікування", "калібрування"]


@dataclass
class Truck:
    id: int
    capacity: int 
    model: str
    current_status: str
    zone: Optional[str] = None
    route_id: Optional[int] = None
    assigned_routes: List[int] = field(default_factory=list)


@dataclass
class StorageSystem:
    id: int
    location: str
    capacity: int
    current_occupancy: int


@dataclass
class ShippingZone:
    id: int
    available_capacity: int
    zone_name: Optional[str] = None


@dataclass
class Route:
    id: int
    start_zone: str
    end_zone: str
    distance: float 
    status: str
    assigned_trucks: List[int] = field(default_factory=list)



@dataclass
class ReceivingZone:
    id: int
    zone_name: str
    capacity: int
    available_capacity: int


@dataclass
class Pallet:
    id: int
    type: str
    capacity: int 


@dataclass
class Packages:
    id: int
    weight: float
    destination_zone: str
    is_delivered: bool


@dataclass
class Drone:
    id: int
    model: str
    battery: int
    status: str
    max_capacity: int


@dataclass
class Client:
    id: int
    name: str
    email: str
    phone: str
    address: str


trucks = [
    Truck(1, 2000, "Volvo X1", "в дорозі", "Зона A"),
    Truck(2, 2500, "Scania Y3", "в дорозі", "Зона B"),
]

storage_systems = [
    StorageSystem(1, "Зона A", 5000, 3000),
    StorageSystem(2, "Зона B", 7000, 2000),
]

shipping_zones = [
    ShippingZone(1, "Зона A", 3000),
    ShippingZone(2, "Зона B", 5000),
]

routes = [
    Route(1, "Зона A", "Зона B", 120.5, "активний"),
    Route(2, "Зона C", "Зона B", 50.0, "завершений"),
]

receiving_zones = [
    ReceivingZone(1, "Зона A", 5000, 1500),
    ReceivingZone(2, "Зона C", 4000, 3000),
]

pallets = [
    Pallet(1, "Пластиковий", 100),
    Pallet(2, "Дерев'яний", 80),
]

packages = [
    Packages(1, 20.5, "Зона B", False),
    Packages(2, 15.0, "Зона C", True),
]

drones = [
    Drone(1, "DJI Phantom", 85, "активний", 5),
    Drone(2, "Parrot Anafi", 75, "неактивний", 3),
]

clients = [
    Client(1, "Іван Петров", "ivan@example.com", "0931234567", "Зона A"),
    Client(2, "Оля Коваль", "olya@example.com", "0679876543", "Зона B"),
]


ENTITY_LISTS: Dict[str, List[Any]] = {
    "Truck": trucks,
    "StorageSystem": storage_systems,
    "ShippingZone": shipping_zones,
    "Route": routes,
    "ReceivingZone": receiving_zones,
    "Pallet": pallets,
    "Packages": packages,
    "Drone": drones,
    "Client": clients,
    "Cart": carts,
    "Scanner": scanners,
    "Security": securities,
    "ShiftManager": shift_managers,
    "SortingRobot": sorting_robots,
}

WORKER_ASSIGNMENT_TARGETS: Dict[str, List[Any]] = {
    "Truck": trucks,
    "Drone": drones,
    "Cart": carts,
    "Scanner": scanners,
    "Security": securities,
}

PARAMETER_ASSIGNMENT_TARGETS: Dict[str, Dict[str, List[str]]] = {
    "Truck": {"current_status": TRUCK_STATUSES, "zone": ZONES},
    "Route": {"status": ROUTE_STATUSES},
    "Drone": {"status": WORKER_STATUSES},
    "Cart": {"status": WORKER_STATUSES, "zone": ZONES},
    "ShiftManager": {"status": WORKER_STATUSES, "shift_type": SHIFT_TYPES, "department": DEPARTMENTS, "zone": ZONES, "note": []},
    "SortingRobot": {"current_task": ROBOT_TASKS},
}

ALLOWED_ROLES: Dict[str, List[str]] = {
    "Truck": ["оператор", "логіст"],
    "Drone": ["оператор дронів"],
    "Cart": ["оператор", "комірник", "логіст"],
    "Scanner": ["оператор", "комірник", "диспетчер"],
    "Security": ["охоронець", "менеджер зміни"],
}



def display_entity_list(entity_list: List[Any], class_name: str):
    print(f"\n--- Список об'єктів класу {class_name} ---")
    for entity in entity_list:
        display_line = f"ID: {entity.id} - {entity}"
        print(display_line)
    print("-" * 30)

def handle_worker_assignment(assign: bool):
    action_verb = "Призначення" if assign else "Видалення"
    print(f"\n===== {action_verb} працівника =====")
    class_name, entity_list = select_target_class(WORKER_ASSIGNMENT_TARGETS)
    if not class_name:
        return

    worker_obj = None
    if assign:
        unassigned_workers = get_unassigned_workers()
        if not unassigned_workers:
            print("✅ Наразі немає вільних працівників для призначення.")
            return

        print("\nКого Ви хочете призначити? (Вільні працівники)")

        try:
            worker_id = int(input("Введіть ID працівника: "))
            worker_obj = find_worker_by_id(worker_id)
            if not worker_obj:
                print("❌ Працівника з таким ID не знайдено.")
                return
        except ValueError:
            print("❌ Невірний формат ID.")
            return

    display_entity_list(entity_list, class_name)
    
    try:
        entity_id = int(input(f"Введіть ID об'єкта {class_name} для {'призначення' if assign else 'видалення'}: "))
        entity_obj = find_entity_by_id(entity_list, entity_id)

        if not entity_obj:
            print(f"❌ Об'єкт {class_name} з ID {entity_id} не знайдено.")
            return

    except ValueError:
        print("❌ Невірний формат ID.")
        return

    if assign:
        if hasattr(entity_obj, 'worker_id') and entity_obj.worker_id is not None:
            print(f"⚠️ Об'єкт {class_name} (ID {entity_id}) вже має працівника.")
            return

        entity_obj.worker_id = worker_obj.id
        print(f"✅ Працівника ID {worker_obj.id} ({worker_obj.name}) успішно ПРИЗНАЧЕНО до {class_name} ID {entity_id}.")
    
    else: 
        if hasattr(entity_obj, 'worker_id') and entity_obj.worker_id is None:
            print(f"⚠️ Об'єкт {class_name} (ID {entity_id}) не має призначеного працівника.")
            return

        assigned_worker_id = entity_obj.worker_id
        entity_obj.worker_id = None
        print(f"✅ Працівника ID {assigned_worker_id} успішно звільнено від об'єкта {class_name} (ID {entity_id}).")

def get_assigned_worker_ids() -> Set[int]:
    assigned_ids = set()
    for entity_list in WORKER_ASSIGNMENT_TARGETS.values():
        for item in entity_list:
            if hasattr(item, 'worker_id') and item.worker_id is not None:
                assigned_ids.add(item.worker_id)
    return assigned_ids

def get_unassigned_workers() -> List[Client]:
    assigned_ids = get_assigned_worker_ids()
    return [w for w in clients if w.id not in assigned_ids]

def find_worker_by_id(worker_id: int) -> Optional[Client]:
    return next((w for w in clients if w.id == worker_id), None)

def find_entity_by_id(entity_list: List[Any], entity_id: int) -> Optional[Any]:
    return next((e for e in entity_list if e.id == entity_id), None)

def select_target_class(target_map: Dict[str, Any]) -> tuple[Optional[str], Optional[List[Any]]]:
    print("\nДе Ви хочете це зробити? (Виберіть клас)")
    class_names = list(target_map.keys())
    for i, name in enumerate(class_names):
        print(f"{i + 1}. {name}")

    try:
        choice = int(input("Ваш вибір (номер): "))
        if not 1 <= choice <= len(class_names):
            print("❌ Невірний вибір.")
            return None, None
        
        class_name = class_names[choice - 1]
        entity_list = target_map[class_name]
        return class_name, entity_list
        
    except ValueError:
        print("❌ Невірний формат введення.")

        return None, None
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
        print("1. Призначити працівника (Cart/Security/Scaner)")
        print("2. Видалити працівника (Unassign Worker)")
        print("3. Призначити/Змінити параметр (Set Parameter)")
        print("4. Видалити параметр (Unset Parameter)")
        print("5. Призначити працівника(Truck/Drone)")
        print("6. Призначити маршрут вантажівці")
        print("7. Показати всі об'єкти")
        print("8. Вихід")
        
        
        
        choice = input("Ваш вибір: ")

        if choice == '1':
            handle_worker_assignment(assign=True)
        elif choice == '2':
            handle_worker_assignment(assign=False)
        elif choice == '3':
            handle_parameter_assignment(assign=True)
        elif choice == '4':
            handle_parameter_assignment(assign=False)
        elif choice == "5":
            print("Куди призначити працівника?")
            for i, c in enumerate(WORKER_ASSIGNMENT_TARGETS.keys()):
                print(f"{i+1}. {c}")
            try:
                cls_choice = int(input("Вибір: "))
                class_name = list(WORKER_ASSIGNMENT_TARGETS.keys())[cls_choice-1]
                assign_worker_to_entity(class_name)
            except:
                print("❌ Невірний ввід")
        elif choice == "6":
            assign_route_to_truck()
        elif choice == "7":
            for cls, lst in ENTITY_LISTS.items():
                display_entity_list(lst, cls)
        elif choice == "8":
            print("Вихід")
            break
        else:
            print("❌ Невірний вибір")

if __name__ == "__main__":
    menu_main()


