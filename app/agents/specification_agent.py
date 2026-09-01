class SpecificationAgent:

    def __init__(self, db):
        self.db = db

    def get_specification(self, phone):

        return {
            "name": phone.name,

            "release": {
                "release_date": phone.release_date,
                "status": phone.status,
                "source_url": phone.source_url,
            },

            "network": {
                "technology": phone.technology,
                "speed": phone.speed,
            },

            "body": {
                "dimensions": phone.dimensions,
                "weight": phone.weight,
                "build": phone.build,
                "sim": phone.sim,
                "ip_rating": phone.ip_rating,
            },

            "display": {
                "type": phone.display_type,
                "size": phone.display_size,
                "resolution": phone.display_resolution,
                "protection": phone.display_protection,
                "refresh_rate": phone.display_refresh_rate,
                "brightness": phone.display_brightness,
            },

            "platform": {
                "os": phone.os,
                "chipset": phone.chipset,
                "cpu": phone.cpu,
                "gpu": phone.gpu,
            },

            "memory": {
                "ram": phone.ram,
                "storage": phone.storage,
                "card_slot": phone.card_slot,
            },

            "camera": {
                "main": phone.main_camera,
                "ultrawide": phone.ultrawide_camera,
                "telephoto": phone.telephoto_camera,
                "depth": phone.depth_camera,
                "features": phone.main_camera_features,
                "video": phone.main_camera_video,
            },

            "selfie_camera": {
                "camera": phone.selfie_camera,
                "video": phone.selfie_video,
            },

            "sound": {
                "loudspeaker": phone.loudspeaker,
                "headphone_jack": phone.headphone_jack,
            },

            "connectivity": {
                "wlan": phone.wlan,
                "bluetooth": phone.bluetooth,
                "gps": phone.gps,
                "nfc": phone.nfc,
                "radio": phone.radio,
                "usb": phone.usb,
            },

            "sensors": phone.sensors,

            "battery": {
                "capacity": phone.battery,
                "charging": phone.charging,
                "wireless_charging": phone.wireless_charging,
            },

            "other": {
                "colors": phone.colors,
                "price": phone.price,
                "models": phone.models,
            },
        }