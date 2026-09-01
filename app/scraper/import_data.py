from app.database.connection import SessionLocal
from app.database.models import Phone


phones = [

    {
        "name": "Samsung Galaxy S21",
        "release_date": "January 2021",
        "status": "Available",
        "source_url": "https://www.gsmarena.com/samsung_galaxy_s21_5g-10626.php",

        "technology": "GSM / CDMA / HSPA / EVDO / LTE / 5G",
        "two_g_bands": None,
        "three_g_bands": None,
        "four_g_bands": None,
        "five_g_bands": None,
        "speed": "HSPA / LTE / 5G",

        "dimensions": "151.7 x 71.2 x 7.9 mm",
        "weight": "169 g",
        "build": "Glass front, plastic back, aluminum frame",
        "sim": "Nano-SIM + eSIM",
        "ip_rating": "IP68",

        "display_type": "Dynamic AMOLED 2X",
        "display_size": "6.2 inches",
        "display_resolution": "1080 x 2400 pixels",
        "display_protection": "Corning Gorilla Glass Victus",
        "display_refresh_rate": "120 Hz",
        "display_brightness": None,

        "os": "Android 11, One UI 3.1",
        "chipset": "Exynos 2100 / Snapdragon 888",
        "cpu": "Octa-core",
        "gpu": "Mali-G78 MP14 / Adreno 660",

        "ram": "8 GB",
        "storage": "128 GB / 256 GB",
        "card_slot": "No",

        "main_camera": "12 MP",
        "ultrawide_camera": "12 MP",
        "telephoto_camera": "64 MP",
        "depth_camera": None,
        "main_camera_features": "Dual Pixel PDAF, OIS",
        "main_camera_video": "Up to 8K",

        "selfie_camera": "10 MP",
        "selfie_video": "4K",

        "loudspeaker": "Stereo speakers",
        "headphone_jack": "No",

        "wlan": "Wi-Fi 802.11 a/b/g/n/ac/6",
        "bluetooth": "5.0",
        "gps": "GPS, GLONASS, GALILEO, BDS",
        "nfc": "Yes",
        "radio": "No",
        "usb": "USB Type-C 3.2",

        "sensors": "Fingerprint, accelerometer, gyro, proximity, compass, barometer",

        "battery": "4000 mAh",
        "charging": "25W wired",
        "wireless_charging": "15W",

        "colors": "Phantom Gray, Phantom White, Phantom Violet, Phantom Pink",
        "price": None,
        "models": None
    },


    {
        "name": "Samsung Galaxy S21+",
        "release_date": "January 2021",
        "status": "Available",
        "source_url": "https://www.gsmarena.com/samsung_galaxy_s21+_5g-10625.php",

        "technology": "GSM / CDMA / HSPA / EVDO / LTE / 5G",
        "two_g_bands": None,
        "three_g_bands": None,
        "four_g_bands": None,
        "five_g_bands": None,
        "speed": "HSPA / LTE / 5G",

        "dimensions": "161.5 x 75.6 x 7.8 mm",
        "weight": "200 g",
        "build": "Glass front, glass back, aluminum frame",
        "sim": "Nano-SIM + eSIM",
        "ip_rating": "IP68",

        "display_type": "Dynamic AMOLED 2X",
        "display_size": "6.7 inches",
        "display_resolution": "1080 x 2400 pixels",
        "display_protection": "Corning Gorilla Glass Victus",
        "display_refresh_rate": "120 Hz",
        "display_brightness": None,

        "os": "Android 11, One UI 3.1",
        "chipset": "Exynos 2100 / Snapdragon 888",
        "cpu": "Octa-core",
        "gpu": "Mali-G78 MP14 / Adreno 660",

        "ram": "8 GB",
        "storage": "128 GB / 256 GB",
        "card_slot": "No",

        "main_camera": "12 MP",
        "ultrawide_camera": "12 MP",
        "telephoto_camera": "64 MP",
        "depth_camera": None,
        "main_camera_features": "Dual Pixel PDAF, OIS",
        "main_camera_video": "Up to 8K",

        "selfie_camera": "10 MP",
        "selfie_video": "4K",

        "loudspeaker": "Stereo speakers",
        "headphone_jack": "No",

        "wlan": "Wi-Fi 802.11 a/b/g/n/ac/6",
        "bluetooth": "5.0",
        "gps": "GPS, GLONASS, GALILEO, BDS",
        "nfc": "Yes",
        "radio": "No",
        "usb": "USB Type-C 3.2",

        "sensors": "Fingerprint, accelerometer, gyro, proximity, compass, barometer",

        "battery": "4800 mAh",
        "charging": "25W wired",
        "wireless_charging": "15W",

        "colors": "Phantom Black, Phantom Silver, Phantom Violet, Phantom Pink",
        "price": None,
        "models": None
    },


    {
        "name": "Samsung Galaxy S21 Ultra",
        "release_date": "January 2021",
        "status": "Available",
        "source_url": "https://www.gsmarena.com/samsung_galaxy_s21_ultra_5g-10596.php",

        "technology": "GSM / CDMA / HSPA / EVDO / LTE / 5G",
        "two_g_bands": None,
        "three_g_bands": None,
        "four_g_bands": None,
        "five_g_bands": None,
        "speed": "HSPA / LTE / 5G",

        "dimensions": "165.1 x 75.6 x 8.9 mm",
        "weight": "227 g",
        "build": "Glass front, glass back, aluminum frame",
        "sim": "Nano-SIM + eSIM",
        "ip_rating": "IP68",

        "display_type": "Dynamic AMOLED 2X",
        "display_size": "6.8 inches",
        "display_resolution": "1440 x 3200 pixels",
        "display_protection": "Corning Gorilla Glass Victus",
        "display_refresh_rate": "120 Hz",
        "display_brightness": None,

        "os": "Android 11, One UI 3.1",
        "chipset": "Exynos 2100 / Snapdragon 888",
        "cpu": "Octa-core",
        "gpu": "Mali-G78 MP14 / Adreno 660",

        "ram": "12 GB / 16 GB",
        "storage": "128 GB / 256 GB / 512 GB",
        "card_slot": "No",

        "main_camera": "108 MP",
        "ultrawide_camera": "12 MP",
        "telephoto_camera": "10 MP + 10 MP",
        "depth_camera": None,
        "main_camera_features": "Laser autofocus, Dual Pixel PDAF, OIS",
        "main_camera_video": "Up to 8K",

        "selfie_camera": "40 MP",
        "selfie_video": "4K",

        "loudspeaker": "Stereo speakers",
        "headphone_jack": "No",

        "wlan": "Wi-Fi 802.11 a/b/g/n/ac/6",
        "bluetooth": "5.2",
        "gps": "GPS, GLONASS, GALILEO, BDS",
        "nfc": "Yes",
        "radio": "No",
        "usb": "USB Type-C 3.2",

        "sensors": "Fingerprint, accelerometer, gyro, proximity, compass, barometer",

        "battery": "5000 mAh",
        "charging": "25W wired",
        "wireless_charging": "15W",

        "colors": "Phantom Black, Phantom Silver",
        "price": None,
        "models": None
    },


    {
        "name": "Samsung Galaxy S22",
        "release_date": "February 2022",
        "status": "Available",
        "source_url": "https://www.gsmarena.com/samsung_galaxy_s22_5g-11253.php",

        "technology": "GSM / CDMA / HSPA / EVDO / LTE / 5G",
        "two_g_bands": None,
        "three_g_bands": None,
        "four_g_bands": None,
        "five_g_bands": None,
        "speed": "HSPA / LTE / 5G",

        "dimensions": "146 x 70.6 x 7.6 mm",
        "weight": "167 g",
        "build": "Glass front, glass back, aluminum frame",
        "sim": "Nano-SIM + eSIM",
        "ip_rating": "IP68",

        "display_type": "Dynamic AMOLED 2X",
        "display_size": "6.1 inches",
        "display_resolution": "1080 x 2340 pixels",
        "display_protection": "Gorilla Glass Victus+",
        "display_refresh_rate": "120 Hz",
        "display_brightness": None,

        "os": "Android 12, One UI 4.1",
        "chipset": "Exynos 2200 / Snapdragon 8 Gen 1",
        "cpu": "Octa-core",
        "gpu": "Xclipse 920 / Adreno 730",

        "ram": "8 GB",
        "storage": "128 GB / 256 GB",
        "card_slot": "No",

        "main_camera": "50 MP",
        "ultrawide_camera": "12 MP",
        "telephoto_camera": "10 MP",
        "depth_camera": None,
        "main_camera_features": "Dual Pixel PDAF, OIS",
        "main_camera_video": "Up to 8K",

        "selfie_camera": "10 MP",
        "selfie_video": "4K",

        "loudspeaker": "Stereo speakers",
        "headphone_jack": "No",

        "wlan": "Wi-Fi 802.11 a/b/g/n/ac/6",
        "bluetooth": "5.2",
        "gps": "GPS, GLONASS, GALILEO, BDS",
        "nfc": "Yes",
        "radio": "No",
        "usb": "USB Type-C 3.2",

        "sensors": "Fingerprint, accelerometer, gyro, proximity, compass, barometer",

        "battery": "3700 mAh",
        "charging": "25W wired",
        "wireless_charging": "15W",

        "colors": "Phantom Black, White, Green, Pink Gold",
        "price": None,
        "models": None
    },


    {
        "name": "Samsung Galaxy S22+",
        "release_date": "February 2022",
        "status": "Available",
        "source_url": "https://www.gsmarena.com/samsung_galaxy_s22+_5g-11236.php",

        "technology": "GSM / CDMA / HSPA / EVDO / LTE / 5G",
        "two_g_bands": None,
        "three_g_bands": None,
        "four_g_bands": None,
        "five_g_bands": None,
        "speed": "HSPA / LTE / 5G",

        "dimensions": "157.4 x 75.8 x 7.6 mm",
        "weight": "195 g",
        "build": "Glass front, glass back, aluminum frame",
        "sim": "Nano-SIM + eSIM",
        "ip_rating": "IP68",

        "display_type": "Dynamic AMOLED 2X",
        "display_size": "6.6 inches",
        "display_resolution": "1080 x 2340 pixels",
        "display_protection": "Gorilla Glass Victus+",
        "display_refresh_rate": "120 Hz",
        "display_brightness": None,

        "os": "Android 12, One UI 4.1",
        "chipset": "Exynos 2200 / Snapdragon 8 Gen 1",
        "cpu": "Octa-core",
        "gpu": "Xclipse 920 / Adreno 730",

        "ram": "8 GB",
        "storage": "128 GB / 256 GB",
        "card_slot": "No",

        "main_camera": "50 MP",
        "ultrawide_camera": "12 MP",
        "telephoto_camera": "10 MP",
        "depth_camera": None,
        "main_camera_features": "Dual Pixel PDAF, OIS",
        "main_camera_video": "Up to 8K",

        "selfie_camera": "10 MP",
        "selfie_video": "4K",

        "loudspeaker": "Stereo speakers",
        "headphone_jack": "No",

        "wlan": "Wi-Fi 802.11 a/b/g/n/ac/6",
        "bluetooth": "5.2",
        "gps": "GPS, GLONASS, GALILEO, BDS",
        "nfc": "Yes",
        "radio": "No",
        "usb": "USB Type-C 3.2",

        "sensors": "Fingerprint, accelerometer, gyro, proximity, compass, barometer",

        "battery": "4500 mAh",
        "charging": "45W wired",
        "wireless_charging": "15W",

        "colors": "Phantom Black, White, Green, Pink Gold",
        "price": None,
        "models": None
    },


    {
        "name": "Samsung Galaxy S22 Ultra",
        "release_date": "February 2022",
        "status": "Available",
        "source_url": "https://www.gsmarena.com/samsung_galaxy_s22_ultra_5g-11251.php",

        "technology": "GSM / CDMA / HSPA / EVDO / LTE / 5G",
        "two_g_bands": None,
        "three_g_bands": None,
        "four_g_bands": None,
        "five_g_bands": None,
        "speed": "HSPA / LTE / 5G",

        "dimensions": "163.3 x 77.9 x 8.9 mm",
        "weight": "228 g",
        "build": "Glass front, glass back, aluminum frame",
        "sim": "Nano-SIM + eSIM",
        "ip_rating": "IP68",

        "display_type": "Dynamic AMOLED 2X",
        "display_size": "6.8 inches",
        "display_resolution": "1440 x 3088 pixels",
        "display_protection": "Gorilla Glass Victus+",
        "display_refresh_rate": "120 Hz",
        "display_brightness": None,

        "os": "Android 12, One UI 4.1",
        "chipset": "Exynos 2200 / Snapdragon 8 Gen 1",
        "cpu": "Octa-core",
        "gpu": "Xclipse 920 / Adreno 730",

        "ram": "8 GB / 12 GB",
        "storage": "128 GB / 256 GB / 512 GB / 1 TB",
        "card_slot": "No",

        "main_camera": "108 MP",
        "ultrawide_camera": "12 MP",
        "telephoto_camera": "10 MP + 10 MP",
        "depth_camera": None,
        "main_camera_features": "Laser AF, OIS",
        "main_camera_video": "Up to 8K",

        "selfie_camera": "40 MP",
        "selfie_video": "4K",

        "loudspeaker": "Stereo speakers",
        "headphone_jack": "No",

        "wlan": "Wi-Fi 802.11 a/b/g/n/ac/6e",
        "bluetooth": "5.2",
        "gps": "GPS, GLONASS, GALILEO, BDS",
        "nfc": "Yes",
        "radio": "No",
        "usb": "USB Type-C 3.2",

        "sensors": "Fingerprint, accelerometer, gyro, proximity, compass, barometer",

        "battery": "5000 mAh",
        "charging": "45W wired",
        "wireless_charging": "15W",

        "colors": "Phantom Black, White, Green, Burgundy",
        "price": None,
        "models": None
    },


    {
        "name": "Samsung Galaxy S23",
        "release_date": "February 2023",
        "status": "Available",
        "source_url": "https://www.gsmarena.com/samsung_galaxy_s23-12082.php",

        "technology": "GSM / CDMA / HSPA / EVDO / LTE / 5G",
        "two_g_bands": None,
        "three_g_bands": None,
        "four_g_bands": None,
        "five_g_bands": None,
        "speed": "HSPA / LTE / 5G",

        "dimensions": "146.3 x 70.9 x 7.6 mm",
        "weight": "168 g",
        "build": "Glass front, glass back, aluminum frame",
        "sim": "Nano-SIM + eSIM",
        "ip_rating": "IP68",

        "display_type": "Dynamic AMOLED 2X",
        "display_size": "6.1 inches",
        "display_resolution": "1080 x 2340 pixels",
        "display_protection": "Gorilla Glass Victus 2",
        "display_refresh_rate": "120 Hz",
        "display_brightness": None,

        "os": "Android 13, One UI 5.1",
        "chipset": "Snapdragon 8 Gen 2 for Galaxy",
        "cpu": "Octa-core",
        "gpu": "Adreno 740",

        "ram": "8 GB",
        "storage": "128 GB / 256 GB",
        "card_slot": "No",

        "main_camera": "50 MP",
        "ultrawide_camera": "12 MP",
        "telephoto_camera": "10 MP",
        "depth_camera": None,
        "main_camera_features": "Dual Pixel PDAF, OIS",
        "main_camera_video": "Up to 8K",

        "selfie_camera": "12 MP",
        "selfie_video": "4K",

        "loudspeaker": "Stereo speakers",
        "headphone_jack": "No",

        "wlan": "Wi-Fi 802.11 a/b/g/n/ac/6e",
        "bluetooth": "5.3",
        "gps": "GPS, GLONASS, GALILEO, BDS",
        "nfc": "Yes",
        "radio": "No",
        "usb": "USB Type-C 3.2",

        "sensors": "Fingerprint, accelerometer, gyro, proximity, compass, barometer",

        "battery": "3900 mAh",
        "charging": "25W wired",
        "wireless_charging": "15W",

        "colors": "Phantom Black, Cream, Green, Lavender",
        "price": None,
        "models": None
    },


    {
        "name": "Samsung Galaxy S23+",
        "release_date": "February 2023",
        "status": "Available",
        "source_url": "https://www.gsmarena.com/samsung_galaxy_s23+-12083.php",

        "technology": "GSM / CDMA / HSPA / EVDO / LTE / 5G",
        "two_g_bands": None,
        "three_g_bands": None,
        "four_g_bands": None,
        "five_g_bands": None,
        "speed": "HSPA / LTE / 5G",

        "dimensions": "157.8 x 76.2 x 7.6 mm",
        "weight": "196 g",
        "build": "Glass front, glass back, aluminum frame",
        "sim": "Nano-SIM + eSIM",
        "ip_rating": "IP68",

        "display_type": "Dynamic AMOLED 2X",
        "display_size": "6.6 inches",
        "display_resolution": "1080 x 2340 pixels",
        "display_protection": "Gorilla Glass Victus 2",
        "display_refresh_rate": "120 Hz",
        "display_brightness": None,

        "os": "Android 13, One UI 5.1",
        "chipset": "Snapdragon 8 Gen 2 for Galaxy",
        "cpu": "Octa-core",
        "gpu": "Adreno 740",

        "ram": "8 GB",
        "storage": "256 GB / 512 GB",
        "card_slot": "No",

        "main_camera": "50 MP",
        "ultrawide_camera": "12 MP",
        "telephoto_camera": "10 MP",
        "depth_camera": None,
        "main_camera_features": "Dual Pixel PDAF, OIS",
        "main_camera_video": "Up to 8K",

        "selfie_camera": "12 MP",
        "selfie_video": "4K",

        "loudspeaker": "Stereo speakers",
        "headphone_jack": "No",

        "wlan": "Wi-Fi 802.11 a/b/g/n/ac/6e",
        "bluetooth": "5.3",
        "gps": "GPS, GLONASS, GALILEO, BDS",
        "nfc": "Yes",
        "radio": "No",
        "usb": "USB Type-C 3.2",

        "sensors": "Fingerprint, accelerometer, gyro, proximity, compass, barometer",

        "battery": "4700 mAh",
        "charging": "45W wired",
        "wireless_charging": "15W",

        "colors": "Phantom Black, Cream, Green, Lavender",
        "price": None,
        "models": None
    },


    {
        "name": "Samsung Galaxy S23 Ultra",
        "release_date": "February 2023",
        "status": "Available",
        "source_url": "https://www.gsmarena.com/samsung_galaxy_s23_ultra-12024.php",

        "technology": "GSM / CDMA / HSPA / EVDO / LTE / 5G",
        "two_g_bands": None,
        "three_g_bands": None,
        "four_g_bands": None,
        "five_g_bands": None,
        "speed": "HSPA / LTE / 5G",

        "dimensions": "163.4 x 78.1 x 8.9 mm",
        "weight": "234 g",
        "build": "Glass front, glass back, aluminum frame",
        "sim": "Nano-SIM + eSIM",
        "ip_rating": "IP68",

        "display_type": "Dynamic AMOLED 2X",
        "display_size": "6.8 inches",
        "display_resolution": "1440 x 3088 pixels",
        "display_protection": "Gorilla Glass Victus 2",
        "display_refresh_rate": "120 Hz",
        "display_brightness": None,

        "os": "Android 13, One UI 5.1",
        "chipset": "Snapdragon 8 Gen 2 for Galaxy",
        "cpu": "Octa-core",
        "gpu": "Adreno 740",

        "ram": "8 GB / 12 GB",
        "storage": "256 GB / 512 GB / 1 TB",
        "card_slot": "No",

        "main_camera": "200 MP",
        "ultrawide_camera": "12 MP",
        "telephoto_camera": "10 MP + 10 MP",
        "depth_camera": None,
        "main_camera_features": "Laser AF, OIS",
        "main_camera_video": "Up to 8K",

        "selfie_camera": "12 MP",
        "selfie_video": "4K",

        "loudspeaker": "Stereo speakers",
        "headphone_jack": "No",

        "wlan": "Wi-Fi 802.11 a/b/g/n/ac/6e",
        "bluetooth": "5.3",
        "gps": "GPS, GLONASS, GALILEO, BDS",
        "nfc": "Yes",
        "radio": "No",
        "usb": "USB Type-C 3.2",

        "sensors": "Fingerprint, accelerometer, gyro, proximity, compass, barometer",

        "battery": "5000 mAh",
        "charging": "45W wired",
        "wireless_charging": "15W",

        "colors": "Green, Cream, Lavender, Phantom Black",
        "price": None,
        "models": None
    },


    {
        "name": "Samsung Galaxy S24",
        "release_date": "January 2024",
        "status": "Available",
        "source_url": "https://www.gsmarena.com/samsung_galaxy_s24-12773.php",

        "technology": "GSM / CDMA / HSPA / EVDO / LTE / 5G",
        "two_g_bands": None,
        "three_g_bands": None,
        "four_g_bands": None,
        "five_g_bands": None,
        "speed": "HSPA / LTE / 5G",

        "dimensions": "147 x 70.6 x 7.6 mm",
        "weight": "167 g",
        "build": "Glass front, glass back, aluminum frame",
        "sim": "Nano-SIM + eSIM",
        "ip_rating": "IP68",

        "display_type": "Dynamic LTPO AMOLED 2X",
        "display_size": "6.2 inches",
        "display_resolution": "1080 x 2340 pixels",
        "display_protection": "Gorilla Glass Victus 2",
        "display_refresh_rate": "120 Hz",
        "display_brightness": None,

        "os": "Android 14, One UI 6.1",
        "chipset": "Exynos 2400 / Snapdragon 8 Gen 3",
        "cpu": "Deca-core / Octa-core",
        "gpu": "Xclipse 940 / Adreno 750",

        "ram": "8 GB",
        "storage": "128 GB / 256 GB / 512 GB",
        "card_slot": "No",

        "main_camera": "50 MP",
        "ultrawide_camera": "12 MP",
        "telephoto_camera": "10 MP",
        "depth_camera": None,
        "main_camera_features": "Dual Pixel PDAF, OIS",
        "main_camera_video": "Up to 8K",

        "selfie_camera": "12 MP",
        "selfie_video": "4K",

        "loudspeaker": "Stereo speakers",
        "headphone_jack": "No",

        "wlan": "Wi-Fi 802.11 a/b/g/n/ac/6e/7",
        "bluetooth": "5.3",
        "gps": "GPS, GLONASS, GALILEO, BDS",
        "nfc": "Yes",
        "radio": "No",
        "usb": "USB Type-C 3.2",

        "sensors": "Fingerprint, accelerometer, gyro, proximity, compass, barometer",

        "battery": "4000 mAh",
        "charging": "25W wired",
        "wireless_charging": "15W",

        "colors": "Onyx Black, Marble Gray, Cobalt Violet, Amber Yellow",
        "price": None,
        "models": None
    },


    {
        "name": "Samsung Galaxy S24+",
        "release_date": "January 2024",
        "status": "Available",
        "source_url": "https://www.gsmarena.com/samsung_galaxy_s24+-12772.php",

        "technology": "GSM / CDMA / HSPA / EVDO / LTE / 5G",
        "two_g_bands": None,
        "three_g_bands": None,
        "four_g_bands": None,
        "five_g_bands": None,
        "speed": "HSPA / LTE / 5G",

        "dimensions": "158.5 x 75.9 x 7.7 mm",
        "weight": "196 g",
        "build": "Glass front, glass back, aluminum frame",
        "sim": "Nano-SIM + eSIM",
        "ip_rating": "IP68",

        "display_type": "Dynamic LTPO AMOLED 2X",
        "display_size": "6.7 inches",
        "display_resolution": "1440 x 3120 pixels",
        "display_protection": "Gorilla Glass Victus 2",
        "display_refresh_rate": "120 Hz",
        "display_brightness": None,

        "os": "Android 14, One UI 6.1",
        "chipset": "Exynos 2400 / Snapdragon 8 Gen 3",
        "cpu": "Deca-core / Octa-core",
        "gpu": "Xclipse 940 / Adreno 750",

        "ram": "12 GB",
        "storage": "256 GB / 512 GB",
        "card_slot": "No",

        "main_camera": "50 MP",
        "ultrawide_camera": "12 MP",
        "telephoto_camera": "10 MP",
        "depth_camera": None,
        "main_camera_features": "Dual Pixel PDAF, OIS",
        "main_camera_video": "Up to 8K",

        "selfie_camera": "12 MP",
        "selfie_video": "4K",

        "loudspeaker": "Stereo speakers",
        "headphone_jack": "No",

        "wlan": "Wi-Fi 802.11 a/b/g/n/ac/6e/7",
        "bluetooth": "5.3",
        "gps": "GPS, GLONASS, GALILEO, BDS",
        "nfc": "Yes",
        "radio": "No",
        "usb": "USB Type-C 3.2",

        "sensors": "Fingerprint, accelerometer, gyro, proximity, compass, barometer",

        "battery": "4900 mAh",
        "charging": "45W wired",
        "wireless_charging": "15W",

        "colors": "Onyx Black, Marble Gray, Cobalt Violet, Amber Yellow",
        "price": None,
        "models": None
    },


    {
        "name": "Samsung Galaxy S24 Ultra",
        "release_date": "January 2024",
        "status": "Available",
        "source_url": "https://www.gsmarena.com/samsung_galaxy_s24_ultra-12771.php",

        "technology": "GSM / CDMA / HSPA / EVDO / LTE / 5G",
        "two_g_bands": None,
        "three_g_bands": None,
        "four_g_bands": None,
        "five_g_bands": None,
        "speed": "HSPA / LTE / 5G",

        "dimensions": "162.3 x 79 x 8.6 mm",
        "weight": "232 g",
        "build": "Glass front, titanium frame, glass back",
        "sim": "Nano-SIM + eSIM",
        "ip_rating": "IP68",

        "display_type": "Dynamic LTPO AMOLED 2X",
        "display_size": "6.8 inches",
        "display_resolution": "1440 x 3120 pixels",
        "display_protection": "Gorilla Glass Armor",
        "display_refresh_rate": "120 Hz",
        "display_brightness": None,

        "os": "Android 14, One UI 6.1",
        "chipset": "Snapdragon 8 Gen 3 for Galaxy",
        "cpu": "Octa-core",
        "gpu": "Adreno 750",

        "ram": "12 GB",
        "storage": "256 GB / 512 GB / 1 TB",
        "card_slot": "No",

        "main_camera": "200 MP",
        "ultrawide_camera": "12 MP",
        "telephoto_camera": "10 MP + 50 MP",
        "depth_camera": None,
        "main_camera_features": "Laser AF, OIS",
        "main_camera_video": "Up to 8K",

        "selfie_camera": "12 MP",
        "selfie_video": "4K",

        "loudspeaker": "Stereo speakers",
        "headphone_jack": "No",

        "wlan": "Wi-Fi 802.11 a/b/g/n/ac/6e/7",
        "bluetooth": "5.3",
        "gps": "GPS, GLONASS, GALILEO, BDS",
        "nfc": "Yes",
        "radio": "No",
        "usb": "USB Type-C 3.2",

        "sensors": "Fingerprint, accelerometer, gyro, proximity, compass, barometer",

        "battery": "5000 mAh",
        "charging": "45W wired",
        "wireless_charging": "15W",

        "colors": "Titanium Black, Titanium Gray, Titanium Violet, Titanium Yellow",
        "price": None,
        "models": None
    },


    {
        "name": "Samsung Galaxy S25",
        "release_date": "January 2025",
        "status": "Available",
        "source_url": "https://www.gsmarena.com/samsung_galaxy_s25-13350.php",

        "technology": "GSM / CDMA / HSPA / LTE / 5G",
        "two_g_bands": None,
        "three_g_bands": None,
        "four_g_bands": None,
        "five_g_bands": None,
        "speed": "HSPA / LTE / 5G",

        "dimensions": "146.9 x 70.5 x 7.2 mm",
        "weight": "162 g",
        "build": "Glass front, glass back, aluminum frame",
        "sim": "Nano-SIM + eSIM",
        "ip_rating": "IP68",

        "display_type": "Dynamic LTPO AMOLED 2X",
        "display_size": "6.2 inches",
        "display_resolution": "1080 x 2340 pixels",
        "display_protection": "Gorilla Glass Victus 2",
        "display_refresh_rate": "120 Hz",
        "display_brightness": None,

        "os": "Android 15, One UI 7",
        "chipset": "Snapdragon 8 Elite",
        "cpu": "Octa-core",
        "gpu": "Adreno",

        "ram": "12 GB",
        "storage": "128 GB / 256 GB / 512 GB",
        "card_slot": "No",

        "main_camera": "50 MP",
        "ultrawide_camera": "12 MP",
        "telephoto_camera": "10 MP",
        "depth_camera": None,
        "main_camera_features": "Dual Pixel PDAF, OIS",
        "main_camera_video": "Up to 8K",

        "selfie_camera": "12 MP",
        "selfie_video": "4K",

        "loudspeaker": "Stereo speakers",
        "headphone_jack": "No",

        "wlan": "Wi-Fi",
        "bluetooth": "5.4",
        "gps": "GPS, GLONASS, GALILEO, BDS",
        "nfc": "Yes",
        "radio": "No",
        "usb": "USB Type-C",

        "sensors": "Fingerprint, accelerometer, gyro, proximity, compass",

        "battery": "4000 mAh",
        "charging": "25W wired",
        "wireless_charging": "15W",

        "colors": "Navy, Silver Shadow, Icyblue, Mint",
        "price": None,
        "models": None
    },


    {
        "name": "Samsung Galaxy S25+",
        "release_date": "January 2025",
        "status": "Available",
        "source_url": "https://www.gsmarena.com/samsung_galaxy_s25+-13349.php",

        "technology": "GSM / CDMA / HSPA / LTE / 5G",
        "two_g_bands": None,
        "three_g_bands": None,
        "four_g_bands": None,
        "five_g_bands": None,
        "speed": "HSPA / LTE / 5G",

        "dimensions": "158.4 x 75.8 x 7.3 mm",
        "weight": "190 g",
        "build": "Glass front, glass back, aluminum frame",
        "sim": "Nano-SIM + eSIM",
        "ip_rating": "IP68",

        "display_type": "Dynamic LTPO AMOLED 2X",
        "display_size": "6.7 inches",
        "display_resolution": "1440 x 3120 pixels",
        "display_protection": "Gorilla Glass Victus 2",
        "display_refresh_rate": "120 Hz",
        "display_brightness": None,

        "os": "Android 15, One UI 7",
        "chipset": "Snapdragon 8 Elite",
        "cpu": "Octa-core",
        "gpu": "Adreno",

        "ram": "12 GB",
        "storage": "256 GB / 512 GB",
        "card_slot": "No",

        "main_camera": "50 MP",
        "ultrawide_camera": "12 MP",
        "telephoto_camera": "10 MP",
        "depth_camera": None,
        "main_camera_features": "Dual Pixel PDAF, OIS",
        "main_camera_video": "Up to 8K",

        "selfie_camera": "12 MP",
        "selfie_video": "4K",

        "loudspeaker": "Stereo speakers",
        "headphone_jack": "No",

        "wlan": "Wi-Fi",
        "bluetooth": "5.4",
        "gps": "GPS, GLONASS, GALILEO, BDS",
        "nfc": "Yes",
        "radio": "No",
        "usb": "USB Type-C",

        "sensors": "Fingerprint, accelerometer, gyro, proximity, compass",

        "battery": "4900 mAh",
        "charging": "45W wired",
        "wireless_charging": "15W",

        "colors": "Navy, Silver Shadow, Icyblue, Mint",
        "price": None,
        "models": None
    },


    {
        "name": "Samsung Galaxy S25 Ultra",
        "release_date": "January 2025",
        "status": "Available",
        "source_url": "https://www.gsmarena.com/samsung_galaxy_s25_ultra-13322.php",

        "technology": "GSM / CDMA / HSPA / LTE / 5G",
        "two_g_bands": None,
        "three_g_bands": None,
        "four_g_bands": None,
        "five_g_bands": None,
        "speed": "HSPA / LTE / 5G",

        "dimensions": "162.8 x 77.6 x 8.2 mm",
        "weight": "218 g",
        "build": "Glass front, titanium frame, glass back",
        "sim": "Nano-SIM + eSIM",
        "ip_rating": "IP68",

        "display_type": "Dynamic LTPO AMOLED 2X",
        "display_size": "6.9 inches",
        "display_resolution": "1440 x 3120 pixels",
        "display_protection": "Gorilla Armor 2",
        "display_refresh_rate": "120 Hz",
        "display_brightness": None,

        "os": "Android 15, One UI 7",
        "chipset": "Snapdragon 8 Elite for Galaxy",
        "cpu": "Octa-core",
        "gpu": "Adreno",

        "ram": "12 GB / 16 GB",
        "storage": "256 GB / 512 GB / 1 TB",
        "card_slot": "No",

        "main_camera": "200 MP",
        "ultrawide_camera": "50 MP",
        "telephoto_camera": "10 MP + 50 MP",
        "depth_camera": None,
        "main_camera_features": "Laser AF, OIS",
        "main_camera_video": "Up to 8K",

        "selfie_camera": "12 MP",
        "selfie_video": "4K",

        "loudspeaker": "Stereo speakers",
        "headphone_jack": "No",

        "wlan": "Wi-Fi",
        "bluetooth": "5.4",
        "gps": "GPS, GLONASS, GALILEO, BDS",
        "nfc": "Yes",
        "radio": "No",
        "usb": "USB Type-C",

        "sensors": "Fingerprint, accelerometer, gyro, proximity, compass",

        "battery": "5000 mAh",
        "charging": "45W wired",
        "wireless_charging": "15W",

        "colors": "Titanium Black, Titanium Gray, Titanium Silverblue",
        "price": None,
        "models": None
    },


    {
        "name": "Samsung Galaxy Note20",
        "release_date": "August 2020",
        "status": "Available",
        "source_url": "https://www.gsmarena.com/samsung_galaxy_note20-10338.php",

        "technology": "GSM / CDMA / HSPA / EVDO / LTE / 5G",
        "two_g_bands": None,
        "three_g_bands": None,
        "four_g_bands": None,
        "five_g_bands": None,
        "speed": "HSPA / LTE / 5G",

        "dimensions": "161.6 x 75.2 x 8.3 mm",
        "weight": "192 g",
        "build": "Glass front, plastic back, aluminum frame",
        "sim": "Nano-SIM",
        "ip_rating": "IP68",

        "display_type": "Super AMOLED Plus",
        "display_size": "6.7 inches",
        "display_resolution": "1080 x 2400 pixels",
        "display_protection": "Gorilla Glass 5",
        "display_refresh_rate": "60 Hz",
        "display_brightness": None,

        "os": "Android 10, One UI 2.5",
        "chipset": "Exynos 990 / Snapdragon 865+",
        "cpu": "Octa-core",
        "gpu": "Mali-G77 MP11 / Adreno 650",

        "ram": "8 GB",
        "storage": "128 GB / 256 GB",
        "card_slot": "No",

        "main_camera": "12 MP",
        "ultrawide_camera": "12 MP",
        "telephoto_camera": "64 MP",
        "depth_camera": None,
        "main_camera_features": "Dual Pixel PDAF, OIS",
        "main_camera_video": "Up to 8K",

        "selfie_camera": "10 MP",
        "selfie_video": "4K",

        "loudspeaker": "Stereo speakers",
        "headphone_jack": "No",

        "wlan": "Wi-Fi 802.11 a/b/g/n/ac/6",
        "bluetooth": "5.0",
        "gps": "GPS, GLONASS, GALILEO, BDS",
        "nfc": "Yes",
        "radio": "No",
        "usb": "USB Type-C 3.2",

        "sensors": "Fingerprint, accelerometer, gyro, proximity, compass, barometer",

        "battery": "4300 mAh",
        "charging": "25W wired",
        "wireless_charging": "15W",

        "colors": "Mystic Gray, Mystic Green, Mystic Bronze",
        "price": None,
        "models": None
    },


    {
        "name": "Samsung Galaxy Note20 Ultra",
        "release_date": "August 2020",
        "status": "Available",
        "source_url": "https://www.gsmarena.com/samsung_galaxy_note20_ultra-10261.php",

        "technology": "GSM / CDMA / HSPA / EVDO / LTE / 5G",
        "two_g_bands": None,
        "three_g_bands": None,
        "four_g_bands": None,
        "five_g_bands": None,
        "speed": "HSPA / LTE / 5G",

        "dimensions": "164.8 x 77.2 x 8.1 mm",
        "weight": "208 g",
        "build": "Glass front, glass back, aluminum frame",
        "sim": "Nano-SIM + eSIM",
        "ip_rating": "IP68",

        "display_type": "Dynamic AMOLED 2X",
        "display_size": "6.9 inches",
        "display_resolution": "1440 x 3088 pixels",
        "display_protection": "Gorilla Glass Victus",
        "display_refresh_rate": "120 Hz",
        "display_brightness": None,

        "os": "Android 10, One UI 2.5",
        "chipset": "Exynos 990 / Snapdragon 865+",
        "cpu": "Octa-core",
        "gpu": "Mali-G77 MP11 / Adreno 650",

        "ram": "8 GB / 12 GB",
        "storage": "128 GB / 256 GB / 512 GB",
        "card_slot": "microSDXC",

        "main_camera": "108 MP",
        "ultrawide_camera": "12 MP",
        "telephoto_camera": "12 MP",
        "depth_camera": "Laser AF sensor",
        "main_camera_features": "Laser AF, OIS",
        "main_camera_video": "Up to 8K",

        "selfie_camera": "10 MP",
        "selfie_video": "4K",

        "loudspeaker": "Stereo speakers",
        "headphone_jack": "No",

        "wlan": "Wi-Fi 802.11 a/b/g/n/ac/6",
        "bluetooth": "5.0",
        "gps": "GPS, GLONASS, GALILEO, BDS",
        "nfc": "Yes",
        "radio": "No",
        "usb": "USB Type-C 3.2",

        "sensors": "Fingerprint, accelerometer, gyro, proximity, compass, barometer",

        "battery": "4500 mAh",
        "charging": "25W wired",
        "wireless_charging": "15W",

        "colors": "Mystic Bronze, Mystic Black, Mystic White",
        "price": None,
        "models": None
    },


    {
        "name": "Samsung Galaxy Z Fold5",
        "release_date": "July 2023",
        "status": "Available",
        "source_url": "https://www.gsmarena.com/samsung_galaxy_z_fold5-12418.php",

        "technology": "GSM / CDMA / HSPA / EVDO / LTE / 5G",
        "two_g_bands": None,
        "three_g_bands": None,
        "four_g_bands": None,
        "five_g_bands": None,
        "speed": "HSPA / LTE / 5G",

        "dimensions": "154.9 x 129.9 x 6.1 mm unfolded",
        "weight": "253 g",
        "build": "Glass front, glass back, aluminum frame",
        "sim": "Nano-SIM + eSIM",
        "ip_rating": "IPX8",

        "display_type": "Foldable Dynamic AMOLED 2X",
        "display_size": "7.6 inches",
        "display_resolution": "1812 x 2176 pixels",
        "display_protection": "Gorilla Glass Victus 2",
        "display_refresh_rate": "120 Hz",
        "display_brightness": None,

        "os": "Android 13, One UI 5.1.1",
        "chipset": "Snapdragon 8 Gen 2",
        "cpu": "Octa-core",
        "gpu": "Adreno 740",

        "ram": "12 GB",
        "storage": "256 GB / 512 GB / 1 TB",
        "card_slot": "No",

        "main_camera": "50 MP",
        "ultrawide_camera": "12 MP",
        "telephoto_camera": "10 MP",
        "depth_camera": None,
        "main_camera_features": "Dual Pixel PDAF, OIS",
        "main_camera_video": "Up to 8K",

        "selfie_camera": "10 MP cover camera / 4 MP under-display",
        "selfie_video": "4K",

        "loudspeaker": "Stereo speakers",
        "headphone_jack": "No",

        "wlan": "Wi-Fi 802.11 a/b/g/n/ac/6e",
        "bluetooth": "5.3",
        "gps": "GPS, GLONASS, GALILEO, BDS",
        "nfc": "Yes",
        "radio": "No",
        "usb": "USB Type-C 3.2",

        "sensors": "Fingerprint, accelerometer, gyro, proximity, compass, barometer",

        "battery": "4400 mAh",
        "charging": "25W wired",
        "wireless_charging": "15W",

        "colors": "Icy Blue, Phantom Black, Cream",
        "price": None,
        "models": None
    },


    {
        "name": "Samsung Galaxy Z Flip5",
        "release_date": "July 2023",
        "status": "Available",
        "source_url": "https://www.gsmarena.com/samsung_galaxy_z_flip5-12252.php",

        "technology": "GSM / CDMA / HSPA / EVDO / LTE / 5G",
        "two_g_bands": None,
        "three_g_bands": None,
        "four_g_bands": None,
        "five_g_bands": None,
        "speed": "HSPA / LTE / 5G",

        "dimensions": "165.1 x 71.9 x 6.9 mm unfolded",
        "weight": "187 g",
        "build": "Glass front, glass back, aluminum frame",
        "sim": "Nano-SIM + eSIM",
        "ip_rating": "IPX8",

        "display_type": "Foldable Dynamic AMOLED 2X",
        "display_size": "6.7 inches",
        "display_resolution": "1080 x 2640 pixels",
        "display_protection": "Gorilla Glass Victus 2",
        "display_refresh_rate": "120 Hz",
        "display_brightness": None,

        "os": "Android 13, One UI 5.1.1",
        "chipset": "Snapdragon 8 Gen 2",
        "cpu": "Octa-core",
        "gpu": "Adreno 740",

        "ram": "8 GB",
        "storage": "256 GB / 512 GB",
        "card_slot": "No",

        "main_camera": "12 MP",
        "ultrawide_camera": "12 MP",
        "telephoto_camera": None,
        "depth_camera": None,
        "main_camera_features": "Dual Pixel PDAF, OIS",
        "main_camera_video": "Up to 4K",

        "selfie_camera": "10 MP",
        "selfie_video": "4K",

        "loudspeaker": "Stereo speakers",
        "headphone_jack": "No",

        "wlan": "Wi-Fi 802.11 a/b/g/n/ac/6e",
        "bluetooth": "5.3",
        "gps": "GPS, GLONASS, GALILEO, BDS",
        "nfc": "Yes",
        "radio": "No",
        "usb": "USB Type-C 3.2",

        "sensors": "Fingerprint, accelerometer, gyro, proximity, compass, barometer",

        "battery": "3700 mAh",
        "charging": "25W wired",
        "wireless_charging": "15W",

        "colors": "Mint, Graphite, Cream, Lavender",
        "price": None,
        "models": None
    },


    {
        "name": "Samsung Galaxy A54 5G",
        "release_date": "March 2023",
        "status": "Available",
        "source_url": "https://www.gsmarena.com/samsung_galaxy_a54-12070.php",

        "technology": "GSM / HSPA / LTE / 5G",
        "two_g_bands": None,
        "three_g_bands": None,
        "four_g_bands": None,
        "five_g_bands": None,
        "speed": "HSPA / LTE / 5G",

        "dimensions": "158.2 x 76.7 x 8.2 mm",
        "weight": "202 g",
        "build": "Glass front, glass back, plastic frame",
        "sim": "Nano-SIM + eSIM",
        "ip_rating": "IP67",

        "display_type": "Super AMOLED",
        "display_size": "6.4 inches",
        "display_resolution": "1080 x 2340 pixels",
        "display_protection": "Gorilla Glass 5",
        "display_refresh_rate": "120 Hz",
        "display_brightness": None,

        "os": "Android 13, One UI 5.1",
        "chipset": "Exynos 1380",
        "cpu": "Octa-core",
        "gpu": "Mali-G68 MP5",

        "ram": "6 GB / 8 GB",
        "storage": "128 GB / 256 GB",
        "card_slot": "microSDXC",

        "main_camera": "50 MP",
        "ultrawide_camera": "12 MP",
        "telephoto_camera": None,
        "depth_camera": "5 MP",
        "main_camera_features": "OIS",
        "main_camera_video": "4K",

        "selfie_camera": "32 MP",
        "selfie_video": "4K",

        "loudspeaker": "Stereo speakers",
        "headphone_jack": "No",

        "wlan": "Wi-Fi 802.11 a/b/g/n/ac/6",
        "bluetooth": "5.3",
        "gps": "GPS, GLONASS, GALILEO, BDS",
        "nfc": "Yes",
        "radio": "No",
        "usb": "USB Type-C 2.0",

        "sensors": "Fingerprint, accelerometer, gyro, proximity, compass",

        "battery": "5000 mAh",
        "charging": "25W wired",
        "wireless_charging": "No",

        "colors": "Lime, Graphite, Violet, White",
        "price": None,
        "models": None
    }

]

db = SessionLocal()


try:

    for phone_data in phones:

        # Check whether phone already exists
        existing_phone = (
            db.query(Phone)
            .filter(
                Phone.name == phone_data["name"]
            )
            .first()
        )

        if existing_phone:

            print(
                f"Already exists: "
                f"{phone_data['name']}"
            )

            continue

        phone = Phone(**phone_data)

        db.add(phone)

        print(
            f"Added: {phone_data['name']}"
        )

    db.commit()

    print("\nAll phones inserted successfully!")


except Exception as e:

    db.rollback()

    print("Error:", e)


finally:

    db.close()