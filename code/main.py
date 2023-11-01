import json

def main(params):
    try:
        iot_data = json.loads(params.get("iot_data", "{}"))
        print("Received IoT data:", iot_data)
        return {"message": "Data processed successfully"}
    except Exception as e:
        return {"error": str(e)}
