from kubernetes import client, config

config.load_kube_config()

apps = client.AppsV1Api()
custom_objects = client.CustomObjectsApi()


def _flatten_labels(d):
    return ','.join([
        f'{k}={v}' for k, v in d.items()
    ])

def get_deployments(labels, namespace="default"):
    return apps.list_namespaced_deployment(
        namespace,
        label_selector=_flatten_labels(labels),
    )


def get_dynamic_deployments(namespace="default"):
    return custom_objects.list_namespaced_custom_object(
        "condi.me",
        "v1",
        namespace,
        "dynamicdeployments",
    )
