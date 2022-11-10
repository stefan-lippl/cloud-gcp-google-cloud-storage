# Cloud components

## Initial login
Download the credentials and put the .json in the folder `key`

<br>

***

<br>

### Download Objects
```python
from cloud.gcp.gcp_cloudstorage_download_file import GCPDownloader

downloader = GCPDownloader()
downloader.download_file(
    bucket_name: str, 
    filename: str, 
    src_filename: str, 
    src_pwd: str
)
```

<br>

### Upload Objects
```python
from cloud.gcp.gcp_cloudstorage_upload_object import GCPFileUploader

uploader = GCPFileUploader()
downloader.download(
    bucket_name: str
    source_file_name: str
    destination_blob_name: str
)
```

<br>

### List objects
```python
from cloud.gcp.gcp_cloudstorage_list_objects import GCPObjectLister

lister = GCPObjectLister()
lister.download(
    bucket_name: str
)
```# aws_gcp
