import json
import ibm_boto3
from ibm_botocore.client import Config

def main(params):
    try:
        cos_credentials = {
            "apikey": "mjSkKbNFvSsfVTE5FCaBW0Fl4reVa-de5lp05vFCZW73",
            "iam_service_endpoint": "crn:v1:bluemix:public:iam-identity::a/917f666bfcf4453aa90206d94fc5f545::serviceid:ServiceId-e3e3036d-cea8-4e95-b091-f57f4cfbc949",
            "resource_instance_id": "crn:v1:bluemix:public:cloud-object-storage:global:a/917f666bfcf4453aa90206d94fc5f545:8c6ae645-980b-44c8-9b96-8d52ee0af397::",
            "endpoint": " crn:v1:bluemix:public:cloud-object-storage:global:a/917f666bfcf4453aa90206d94fc5f545:8c6ae645-980b-44c8-9b96-8d52ee0af397:bucket:naanmudhalvanproject ",
        }

        
        cos_client = ibm_boto3.client(
            "s3",
            ibm_api_key_id=cos_credentials["apikey"],
            ibm_service_instance_id=cos_credentials["resource_instance_id"],
            ibm_auth_endpoint=cos_credentials["iam_service_endpoint"],
            config=Config(signature_version="oauth"),
            endpoint_url=cos_credentials["endpoint"],
        )

       
        iot_data = params["iot_data"]

       
        bucket_name = "iot-data-bucket"
        object_name = "iot_data.json"
        data = json.dumps(iot_data)

        
        cos_client.put_object(Bucket=bucket_name, Key=object_name, Body=data)

        return {"message": "IoT data uploaded successfully"}
    except Exception as e:
        return {"error": str(e)}
