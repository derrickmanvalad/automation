from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient

# Create a BlobServiceClient using DefaultAzureCredential
credential = DefaultAzureCredential()
blob_service_client = BlobServiceClient(account_url="https://youraccount.blob.core.windows.net", credential=credential)

# Now you can use blob_service_client to work with Azure Blob Storage
