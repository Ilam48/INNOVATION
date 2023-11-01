def automate_smart_home(iot_data):
    if iot_data['motion_detected']:
        adjust_thermostat(iot_data['temperature'])
        if iot_data['time_of_day'] == "night":
            turn_on_lights()
            if iot_data['room'] == "bedroom":
                play_sleep_music()
    if iot_data['door_open']:
        activate_security_camera()
        if iot_data['room'] == "front_door":
            send_security_alert()
    if iot_data['smoke_detected']:
        if iot_data['room'] == "kitchen":
            activate_fire_suppression()
iot_data_1 = {
    "device_id": "motion-sensor-smpbj-01215101455",
    "sensor_type": "motion",
    "timestamp": "2023-10-25T14:30:00",
    "data": {
        "motion_detected": True,
        "room": "living_room",
        "intensity": 0.85,
        "temperature": 23,
        "time_of_day": "night"
    }
}

iot_data_2 = {
    "device_id": "door-sensor-kcdve-02345457231",
    "sensor_type": "door",
    "timestamp": "2023-10-25T15:15:00",
    "data": {
        "door_open": True,
        "room": "front_door",
        "temperature": 19,
        "time_of_day": "evening"
    }
}

iot_data_3 = {
    "device_id": "smoke-sensor-qweas-01283453289",
    "sensor_type": "smoke",
    "timestamp": "2023-10-25T16:45:00",
    "data": {
        "smoke_detected": True,
        "room": "kitchen",
        "temperature": 26,
        "time_of_day": "morning"
    }
}

automate_smart_home(iot_data_1)
automate_smart_home(iot_data_2)
automate_smart_home(iot_data_3)
