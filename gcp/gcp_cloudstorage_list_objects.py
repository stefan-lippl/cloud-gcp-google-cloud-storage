from google.cloud import storage
import os

class GCPObjectLister():
    def list_blobs(self, bucket_name: str):
        """Lists all the blobs in the bucket."""
        #bucket_name = "wef_noaa_weather_data_bucket"
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/Users/stefanlippl/dev/wef_final/spatial-risk-mapping/cloud/gcp/key/wildfire-forecasting-70bb79e32916.json'

        storage_client = storage.Client()

        # Note: Client.list_blobs requires at least package version 1.17.0.
        blobs = storage_client.list_blobs(bucket_name)

        return blobs