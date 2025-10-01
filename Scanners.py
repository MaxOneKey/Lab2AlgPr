class Scanner:
    def __init__(self, scanner_id: int, scanner_type: str, status: str, location: str,
                 assigned_worker=None, last_scan_time: str=None, supported_formats=None,
                 connection_type: str="USB", created_date: str=None, last_service_date: str=None):
        self.scanner_id = scanner_id
        self.scanner_type = scanner_type
        self.status = status
        self.location = location
        self.assigned_worker = assigned_worker
        self.last_scan_time = last_scan_time
        self.supported_formats = supported_formats if supported_formats else []
        self.connection_type = connection_type
        self.created_date = created_date
        self.last_service_date = last_service_date

    def get_info(self):
        return (f"Scanner ID: {self.scanner_id}, Type: {self.scanner_type}, Status: {self.status}, "
                f"Location: {self.location}, Worker: {self.assigned_worker.name if self.assigned_worker else 'Немає'}, "
                f"Last scan: {self.last_scan_time}, Formats: {', '.join(self.supported_formats)}, "
                f"Connection: {self.connection_type}, Created: {self.created_date}, Last service: {self.last_service_date}")

    def update_status(self, new_status: str):
        self.status = new_status

    def assign_worker(self, worker):
        self.assigned_worker = worker

    def update_last_scan(self, scan_time: str):
        self.last_scan_time = scan_time

    def move_to(self, new_location: str):
        self.location = new_location


scanners = {}

scanners[301] = Scanner(301, "штрих-код", "активний", "Зона A", None, "08:00", ["EAN-13", "UPC"], "USB", "2023-01-10", "2024-04-01")
scanners[302] = Scanner(302, "QR", "неактивний", "Зона B", None, "09:30", ["QR"], "Wi-Fi", "2023-02-15", "2024-03-20")
scanners[303] = Scanner(303, "RFID", "активний", "Зона C", None, "10:00", ["ISO 15693"], "Wi-Fi", "2023-03-05", "2024-05-05")
scanners[304] = Scanner(304, "штрих-код", "зламаний", "Зона D", None, "11:15", ["EAN-13"], "USB", "2022-12-20", "2024-02-28")

