def compare_phones(phone1, phone2):

    return {
        "display": {
            phone1.name: phone1.display,
            phone2.name: phone2.display
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