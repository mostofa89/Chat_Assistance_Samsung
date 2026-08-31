class SpecificationAgent:

    def __init__(self, db):

        self.db = db


    def get_specification(
        self,
        phone
    ):

        return {
            "phone": phone.name,
            "display": phone.display,
            "processor": phone.chipset,
            "ram": phone.ram,
            "storage": phone.storage,
            "camera": phone.main_camera,
            "battery": phone.battery
        }