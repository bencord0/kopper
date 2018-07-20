import uuid

from django.db import models

from . import k8s


class Deployment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    host = models.CharField(max_length=128, null=False, blank=False, editable=False)
    image = models.CharField(max_length=128, null=False, blank=False, editable=False)
    tag = models.CharField(max_length=128, null=False, blank=False, editable=False)
    timestamp = models.DateTimeField(null=False)

    def __repr__(self):
        return f'Deployment {self.full_image_name}'

    @property
    def full_image_name(self):
        return f'{self.host}/{self.image}:{self.tag}'

    @property
    def image_name(self):
        return f'{self.host}/{self.image}'

    def handle_deployment(self):
        all_dynamic_deployments = k8s.get_dynamic_deployments()['items']
        my_dynamic_deployment = [d for d in all_dynamic_deployments if d['spec']['imageSource'] == self.image_name][0]

        target = my_dynamic_deployment['spec']['target']
        deployments = k8s.get_deployments(target['matchLabels']).items

        deployment_patch = self.create_deployment_patch(
            target['container'],
            target['containerImageTemplate'],
        )

        for deployment in deployments:
            print(f'patching {deployment.metadata.name}')
            k8s.apps.patch_namespaced_deployment(
                namespace='default',
                name=deployment.metadata.name,
                body=deployment_patch,
            )

    def create_deployment_patch(self, container_name, image_template):
        return {'spec': {'template': {'spec': {
            'containers': [
                {
                    'name': f'{container_name}',
                    'image': image_template.format(
                        host=self.host,
                        image=self.image,
                        tag=self.tag,
                    ),
                }
            ]
        }}}}
