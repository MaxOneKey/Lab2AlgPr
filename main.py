import sys
from dataclasses import dataclass, field
from typing import Optional, List, Any, Dict, Set


SHIFT_TYPES = ["денна", "нічна"]
STATUSES = ["працює", "у відпустці", "на лікарняному", "вільний"]
DEPARTMENTS = ["логістика", "комірник", "доставка"]
ZONES = ["Зона A", "Зона B", "Зона C", "Склад 1"]
ROBOT_TASKS = ["сортування", "зарядка", "очікування", "калібрування"]

@dataclass
class Worker:
    id: int
    name: str
    email: str
    phone: str
    position: str

@dataclass
class Cart:
    id: int
    capacity: int
    speed: float
    type: str
    worker_id: Optional[int] = None
    status: Optional[str] = None
    zone: Optional[str] = None
    start_date: Optional[str] = None
    last_service: Optional[str] = None
    wheels: Optional[str] = None

@dataclass
class Scanner:
    id: int
    type: str
    status: str
    zone: str
    worker_id: Optional[int] = None
    time: Optional[str] = None
    formats: List[str] = field(default_factory=list)
    connection: Optional[str] = None
    created: Optional[str] = None
    updated: Optional[str] = None

@dataclass
class Security:
    id: int
    worker_id: Optional[int] = None
    shift_type: Optional[str] = None
    zone: Optional[str] = None
    phone: Optional[str] = None
    post_id: Optional[str] = None
    status: Optional[str] = None
    rank: Optional[str] = None
    experience: Optional[int] = None

@dataclass
class ShiftManager:
    id: int
    name: str
    phone: str
    email: str
    shift_type: Optional[str] = None
    status: Optional[str] = None
    department: Optional[str] = None
    note: Optional[str] = None
    zone: Optional[str] = None

@dataclass
class SortingRobot:
    id: int
    model: str
    status: str
    battery: int
    speed: int
    zone: str
    current_task: Optional[str] = None
    version: Optional[str] = None
    updated: Optional[str] = None
    power_usage: Optional[float] = None



workers = [
    Worker(1, "Іван Іванов", "ivan@m.com", "0931111111", "оператор"),
    Worker(2, "Олег Коваль", "oleg@m.com", "0671111111", "охоронець"),
    Worker(3, "Андрій Сидоренко", "andriy@m.com", "0503333333", "менеджер зміни"),
    Worker(4, "Марія Левченко", "maria@m.com", "0634444444", "логіст"),
    Worker(5, "Віктор Петренко", "viktor@m.com", "0505555555", "комірник"),
    Worker(6, "Юлія Кравченко", "yuliya@m.com", "0976666666", "диспетчер"),
]

carts = [
    Cart(101, 50, 5.5, "ручний", zone="Зона A", worker_id=1),  
    Cart(102, 100, 4.0, "електричний"),                      
    Cart(103, 75, 5.0, "ручний"),                            
]

scanners = [
    Scanner(201, "QR", "робочий", "Зона B", worker_id=3),  
    Scanner(202, "ШК", "неактивний", "Склад 1"),             
]

securities = [
    Security(301),                                          
    Security(302, shift_type="нічна"),                    
]

shift_managers = [
    ShiftManager(401, "Світлана Гриб", "0991112233", "svitlana@m.com"),
    ShiftManager(402, "Дмитро Сагайдак", "0993334455", "dmytro@m.com"),
]

sorting_robots = [
    SortingRobot(501, "Model A", "робочий", 80, 10, "Зона C"),
    SortingRobot(502, "Model B", "очікування", 95, 12, "Зона C"),
]



ENTITY_LISTS: Dict[str, List[Any]] = {
    "Cart": carts,
    "Scanner": scanners,
    "Security": securities,
    "ShiftManager": shift_managers,
    "SortingRobot": sorting_robots,
}

WORKER_ASSIGNMENT_TARGETS: Dict[str, List[Any]] = {
    "Cart": carts,
    "Scanner": scanners,
    "Security": securities,
}

PARAMETER_ASSIGNMENT_TARGETS: Dict[str, Dict[str, List[str]]] = {
    "Cart": {"status": STATUSES, "zone": ZONES},
    "ShiftManager": {"status": STATUSES, "shift_type": SHIFT_TYPES, "department": DEPARTMENTS, "zone": ZONES, "note": []},
    "SortingRobot": {"current_task": ROBOT_TASKS},
}

ALLOWED_ROLES: Dict[str, List[str]] = {
    "Cart": ["оператор", "комірник", "логіст"],
    "Scanner": ["оператор", "комірник", "диспетчер"],
    "Security": ["охоронець", "менеджер зміни"],
}



def get_assigned_worker_ids() -> Set[int]:
    """Повертає множину ID усіх працівників, які наразі десь призначені."""
    assigned_ids = set()
    for entity_list in WORKER_ASSIGNMENT_TARGETS.values():
        for item in entity_list:
    
            if hasattr(item, 'worker_id') and item.worker_id is not None:
                assigned_ids.add(item.worker_id)
    return assigned_ids

def get_unassigned_workers() -> List[Worker]:
    """Повертає список об'єктів Worker, які ніде не призначені."""
    assigned_ids = get_assigned_worker_ids()
    return [w for w in workers if w.id not in assigned_ids]

def find_worker_by_id(worker_id: int) -> Optional[Worker]:
    """Знаходить об'єкт Worker за ID."""
    return next((w for w in workers if w.id == worker_id), None)

def find_entity_by_id(entity_list: List[Any], entity_id: int) -> Optional[Any]:
    """Знаходить об'єкт у списку за ID."""
    return next((e for e in entity_list if e.id == entity_id), None)

def display_entity_list(entity_list: List[Any], class_name: str, assignable: bool = False):
    """Відображає список об'єктів для вибору."""
    print(f"\n--- Список об'єктів класу {class_name} ---")
    for entity in entity_list:
        worker_status = ""
        if hasattr(entity, 'worker_id'):
            worker_status = f"(Призначено: {entity.worker_id})" if entity.worker_id is not None else "(ВІЛЬНО)"
        
        display_line = f"ID: {entity.id}"
        
        if assignable:
            display_line += f" {worker_status}"
        elif class_name in PARAMETER_ASSIGNMENT_TARGETS:
   
            fields_to_show = ', '.join([f"{k}={getattr(entity, k)}" for k in list(entity.__dataclass_fields__.keys())[1:4]])
            display_line += f" ({fields_to_show}...)"

        print(display_line)
    print("-" * 30)



def select_target_class(target_map: Dict[str, Any]) -> tuple[Optional[str], Optional[List[Any]]]:
    """Функція для вибору класу (Cart, Scanner, Security і т.д.)"""
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


def handle_worker_assignment(assign: bool):
    """Обробляє призначення/видалення працівника з урахуванням ролей."""
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
        for w in unassigned_workers:
            print(f"ID: {w.id} - {w.name} (Роль: {w.position})")
        
        try:
            worker_id = int(input("Введіть ID працівника: "))
            worker_obj = find_worker_by_id(worker_id)
            if not worker_obj or worker_id not in [w.id for w in unassigned_workers]:
                print("❌ Працівника з таким ID не знайдено або він вже призначений.")
                return
        except ValueError:
            print("❌ Невірний формат ID.")
            return

     
        required_roles = ALLOWED_ROLES.get(class_name, [])
        worker_role = worker_obj.position
        
        if required_roles and worker_role not in required_roles:
            print(f"❌ ПРИЗНАЧЕННЯ СКАСОВАНО: Працівник '{worker_obj.name}' має роль '{worker_role}'.")
            print(f"   Для об'єкта {class_name} дозволені лише ролі: {', '.join(required_roles)}")
            return
 
    display_entity_list(entity_list, class_name, assignable=True)
    
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
        if entity_obj.worker_id is not None:
            print(f"⚠️ Об'єкт {class_name} (ID {entity_id}) вже має працівника (ID: {entity_obj.worker_id}).")
            confirm = input("Продовжити та перевизначити? (так/ні): ").lower()
            if confirm != 'так':
                print("Дію скасовано.")
                return
        
        entity_obj.worker_id = worker_obj.id
        print(f"✅ Працівника ID {worker_obj.id} ({worker_obj.name}) успішно ПРИЗНАЧЕНО до {class_name} ID {entity_id}.")
    
    else: 
        if entity_obj.worker_id is None:
            print(f"⚠️ Об'єкт {class_name} (ID {entity_id}) вже не має призначеного працівника.")
            return

        assigned_worker_id = entity_obj.worker_id
        entity_obj.worker_id = None
        print(f"✅ Працівника ID {assigned_worker_id} успішно ВИДАЛЕНО з {class_name} ID {entity_id}.")


def handle_parameter_assignment(assign: bool):
    """Обробляє призначення/видалення параметрів."""
    action_verb = "Призначення" if assign else "Видалення"
    print(f"\n===== {action_verb} параметра =====")

  
    class_name, entity_list = select_target_class(PARAMETER_ASSIGNMENT_TARGETS)
    if not class_name:
        return
    
    parameters_map = PARAMETER_ASSIGNMENT_TARGETS[class_name]


    display_entity_list(entity_list, class_name, assignable=False)
    try:
        entity_id = int(input(f"Введіть ID об'єкта {class_name}: "))
        entity_obj = find_entity_by_id(entity_list, entity_id)

        if not entity_obj:
            print(f"❌ Об'єкт {class_name} з ID {entity_id} не знайдено.")
            return

    except ValueError:
        print("❌ Невірний формат ID.")
        return


    print("\nЯкий параметр Ви хочете змінити/видалити?")
    param_names = list(parameters_map.keys())
    for i, name in enumerate(param_names):
        current_value = getattr(entity_obj, name)
        print(f"{i + 1}. {name} (Поточне: {current_value})")
    
    try:
        param_choice = int(input("Введіть номер параметра: "))
        if not 1 <= param_choice <= len(param_names):
            print("❌ Невірний вибір.")
            return
        param_name = param_names[param_choice - 1]
    except ValueError:
        print("❌ Невірний формат введення.")
        return
    

    if assign:
        possible_values = parameters_map[param_name]
        if possible_values:
            print(f"Можливі значення для '{param_name}': {', '.join(map(str, possible_values))}")
        
        new_value = input(f"Введіть нове значення для '{param_name}' (або залиште порожнім, щоб скасувати): ")
        
        if new_value:
            
            try:
              
                if type(getattr(entity_obj, param_name)) is int or param_name.endswith('count'):
                    final_value: Any = int(new_value)
                elif type(getattr(entity_obj, param_name)) is float or param_name.startswith('power'):
                    final_value = float(new_value)
                else:
                    final_value = new_value
            except ValueError:
                print("❌ Невірний формат значення для цього поля (очікувалося число). Дію скасовано.")
                return

            setattr(entity_obj, param_name, final_value)
            print(f"✅ Параметр '{param_name}' успішно ПРИЗНАЧЕНО об'єкту ID {entity_id}. Нове значення: {final_value}")
        else:
            print("Дію скасовано.")
    
    else: 
        setattr(entity_obj, param_name, None)
        print(f"✅ Параметр '{param_name}' успішно ВИДАЛЕНО (встановлено в None) для об'єкта ID {entity_id}.")


def menu_main():
    """Головне меню програми."""
    while True:
        print("\n" + "=" * 40)
        print("          СИСТЕМА УПРАВЛІННЯ СКЛАДОМ")
        print("=" * 40)
        print("Що Ви бажаєте зробити?")
        print("1. Призначити працівника (Worker)")
        print("2. Видалити працівника (Unassign Worker)")
        print("3. Призначити/Змінити параметр (Set Parameter)")
        print("4. Видалити параметр (Unset Parameter)")
        print("5. Вихід")
        
        choice = input("Ваш вибір (1-5): ")

        if choice == '1':
            handle_worker_assignment(assign=True)
        elif choice == '2':
            handle_worker_assignment(assign=False)
        elif choice == '3':
            handle_parameter_assignment(assign=True)
        elif choice == '4':
            handle_parameter_assignment(assign=False)
        elif choice == '5':
            print("Завершення роботи. До побачення! 👋")
            sys.exit()
        else:
            print("❌ Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    menu_main()