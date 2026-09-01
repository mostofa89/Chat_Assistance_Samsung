def compare_phones(phone1, phone2):
    def display_summary(phone):
        return {
            "type": phone.display_type,
            "size": phone.display_size,
            "resolution": phone.display_resolution,
            "protection": phone.display_protection,
            "refresh_rate": phone.display_refresh_rate,
            "brightness": phone.display_brightness,
        }

    return {
        "display": {
            phone1.name: display_summary(phone1),
            phone2.name: display_summary(phone2)
        },

        "processor": {
            phone1.name: phone1.chipset,
            phone2.name: phone2.chipset
        },

        "ram": {
            phone1.name: phone1.ram,
            phone2.name: phone2.ram
        },

        "camera": {
            phone1.name: phone1.main_camera,
            phone2.name: phone2.main_camera
        },

        "battery": {
            phone1.name: phone1.battery,
            phone2.name: phone2.battery
        }
    }
