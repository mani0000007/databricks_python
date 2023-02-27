import os
from databricks_cli.sdk.api_client import ApiClient
from databricks_cli.clusters.api import ClusterApi
api_client=ApiClient(
    host=os.getenv('DATABRICKS_HOST'),
    token=os.getenv('DATABRICKS_TOKEN')
)
clusters_api = ClusterApi(api_client)
cluster_list=clusters_api.list_clusters()
print('Cluster_Name','Cluster_Id')
for cluster in cluster_list['clusters']:
    print(f"{cluster['cluster_name']},{cluster['cluster_id']}")



os.environ['DATABRICKS_HOST'] = 'https://adb-7837751364337038.18.azuredatabricks.net'
os.environ['DATABRICKS_TOKEN'] = 'dapi4644ea1a25c2c3ac8a6c2fcb26f4538e-3'
