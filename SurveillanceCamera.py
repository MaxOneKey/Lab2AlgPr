class SurveillanceCamera:
    def __init__(self, camera_id, type, resolution, location, storage_capacity,
                 assigned_guard, status, recording, firmware_version, last_service_by):
        self.camera_id = camera_id
        self.type = type
        self.resolution = resolution
        self.location = location
        self.storage_capacity = storage_capacity
        self.assigned_guard = assigned_guard
        self.status = status
        self.recording = recording
        self.firmware_version = firmware_version
        self.last_service_by = last_service_by
        self.alerts = []

    def start_recording(self):
        self.recording = True

    def stop_recording(self):
        self.recording = False

    def service(self, technician_name):
        self.last_service_by = technician_name
        self.firmware_version = "1.0.1"

    def deactivate(self):
        self.status = "вимкнена"

    def get_status(self):
        return f"Камера {self.camera_id}: {self.status}, запис: {self.recording}"


cameras = {}

cameras[1] = SurveillanceCamera(1, "IP", "1080p", "Вхід A", 128, "G1", "активна", False, "1.0.0", "технік 1")
cameras[2] = SurveillanceCamera(2, "нічна", "720p", "Вхід B", 256, "G2", "активна", True, "1.0.0", "технік 2")
cameras[3] = SurveillanceCamera(3, "відео", "4K", "Вхід C", 512, "G3", "вимкнена", False, "1.0.0", "технік 3")
cameras[4] = SurveillanceCamera(4, "IP", "1080p", "Вхід D", 128, "G4", "активна", True, "1.0.0", "технік 4")
cameras[5] = SurveillanceCamera(5, "нічна", "720p", "Вхід E", 256, "G5", "вимкнена", False, "1.0.0", "технік 5")
cameras[6] = SurveillanceCamera(6, "відео", "4K", "Вхід F", 512, "G6", "активна", True, "1.0.0", "технік 6")
cameras[7] = SurveillanceCamera(7, "IP", "1080p", "Вхід G", 128, "G7", "активна", False, "1.0.0", "технік 7")
cameras[8] = SurveillanceCamera(8, "нічна", "720p", "Вхід H", 256, "G8", "вимкнена", False, "1.0.0", "технік 8")
cameras[9] = SurveillanceCamera(9, "відео", "4K", "Вхід I", 512, "G9", "активна", True, "1.0.0", "технік 9")
cameras[10] = SurveillanceCamera(10, "IP", "1080p", "Вхід J", 128, "G10", "активна", False, "1.0.0", "технік 10")
cameras[11] = SurveillanceCamera(11, "нічна", "720p", "Вхід K", 256, "G11", "вимкнена", False, "1.0.0", "технік 11")
cameras[12] = SurveillanceCamera(12, "відео", "4K", "Вхід L", 512, "G12", "активна", True, "1.0.0", "технік 12")
cameras[13] = SurveillanceCamera(13, "IP", "1080p", "Вхід M", 128, "G13", "активна", False, "1.0.0", "технік 13")
cameras[14] = SurveillanceCamera(14, "нічна", "720p", "Вхід N", 256, "G14", "вимкнена", False, "1.0.0", "технік 14")
cameras[15] = SurveillanceCamera(15, "відео", "4K", "Вхід O", 512, "G15", "активна", True, "1.0.0", "технік 15")