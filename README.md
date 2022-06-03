# Cloud components
The following described classes are runable and ready to use.

## Initial login
### AWS
Download credentials and put them in the env

### GCP
Download the credentials and put the .json in the folder `key`

<br>


## AWS

### Download Objects
```python
from cloud.aws.download_s3_file import AWSDownloader

downloader = AWSDownloader()
downloader.download(
    local_filename: str
    s3_bucket: str
    s3_object_key: str
)
```

<br>

### Create Bucket
```python
from cloud.aws.create_bucket.py import AWSCreateS3Bucket

creator = AWSCreateS3Bucket()
creator.create_bucket(
    bucket_name: str, 
    bucket_region: str = 'eu-central-1'
)
```

<br>

***

<br>

## GCP
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
