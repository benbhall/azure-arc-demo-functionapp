import logging
import base64
import os
import azure.functions as func
from azure.storage.blob import BlobServiceClient

def main(myblob: func.InputStream):
    connection_string = os.getenv("AzureWebJobsStorage")
    service_client = BlobServiceClient.from_connection_string(connection_string)
    client = service_client.get_container_client("demo-container")
    for blob in client.list_blobs():
        existing_md5 = blob.content_settings.content_md5
        newfile_md5 = base64.b64decode(myblob.blob_properties.get('ContentMD5'))
        if f"{blob.container}/{blob.name}" != myblob.name and existing_md5 == newfile_md5:
            logging.info(f"Blob {myblob.name} already exists as {blob.name}. Deleting  {blob.name}.")
            client.delete_blob(blob.name)
            return