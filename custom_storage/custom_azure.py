from django.core.files.storage import Storage
from azure.storage.blob import BlobService

class PublicAzureStorage(AzureStorage):
    account_name = 'jiaojiaogao1'
    account_key = '3digaHhgPK+BOiaYdPxO6ozXgkSBv1jiqNDHRamffmhpHDZuWmE6YSsHUY01Igoccg1hGLeXdzIgE8DX15zYwQ=='
    azure_container = 'slidefiles'
    expiration_secs = None

    def geturl(self, name):
        return '%s/%s/%s' % ('http://jiaojiaogao1.blob.core.windows.net', 'slidefiles', name)