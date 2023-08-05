from azure.identity import DefaultAzureCredential
from azure.mgmt.containerservice import ContainerServiceClient
from kubernetes import client, config

def delete_all_pods(kube_config, resource_group):
    try:
        # Load Kubernetes configuration
        config.load_kube_config(config_file=kube_config)

        # Create Kubernetes API client
        v1 = client.CoreV1Api()

        # List all pods in all namespaces
        pods = v1.list_pod_for_all_namespaces(watch=False)

        # Delete all pods
        for pod in pods.items:
            v1.delete_namespaced_pod(pod.metadata.name, pod.metadata.namespace)

        print("All pods deleted successfully.")

    except Exception as e:
        print(f"Error deleting pods: {e}")

def main():
    # Azure subscription ID, resource group name, and Kubernetes config path
    subscription_id = "your_subscription_id"
    resource_group = "your_resource_group"
    kube_config = "path_to_kube_config.yaml"

    try:
        # Authenticate to Azure using DefaultAzureCredential
        credentials = DefaultAzureCredential()
        cs_client = ContainerServiceClient(credentials, subscription_id)

        # Get all managed Kubernetes clusters in the resource group
        clusters = cs_client.managed_clusters.list_by_resource_group(resource_group)

        # Iterate over clusters and delete pods
        for cluster in clusters:
            print(f"Deleting pods in Kubernetes cluster: {cluster.name}")
            kube_config = cluster.kube_config
            delete_all_pods(kube_config, resource_group)
            print("-" * 30)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
