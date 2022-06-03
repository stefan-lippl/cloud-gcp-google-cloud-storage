from google.cloud import storage
import os 
from argparse import ArgumentParser
import sys

class GCPDownloader():
    def download_file(self, bucket_name: str, filename: str, src_filename: str, src_pwd: str):
        """
        ARGS
        bucket_name
            (required, str) Name of the GCP bucket
        filename
            (required, str) Name of the file which should get downloaded
        src_filename
            (required, str) Name of file after download
        src_pwd
            (required, str) Path where file should be located. If path not exists, path will get created

        RETURN
        True if download successfull, False if not
        """
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/Users/stefanlippl/dev/wef_final/spatial-risk-mapping/cloud/gcp/key/wildfire-forecasting-70bb79e32916.json'

        # Make sure the path is correct and add trailing / if not exists
        
        if src_pwd[-1] != '/':
            src_pwd = src_pwd + '/'

        if not os.path.exists(src_pwd):
            os.makedirs(src_pwd)
            print(f'Created directory: {src_pwd}')
        
        # Initialise a client
        storage_client = storage.Client()
        # Create a bucket object for our bucket
        bucket = storage_client.get_bucket(bucket_name)

        # Create a blob object from the filepath
        blob = bucket.blob(filename)

        try:
            # Download the file to a destination
            blob.download_to_filename(src_pwd + src_filename)
            print('Download successfull')
            return True
        except:
            print('Error')
            return False
