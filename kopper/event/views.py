import logging
import json

from pprint import pformat

from rest_framework.decorators import api_view
from rest_framework.response import Response

log = logging.getLogger(__name__)


@api_view(['POST'])
def event(request):
    envelope = json.loads(request.body)

    events = envelope.get('events', [])
    for event in events:
        handler = EVENT_HANDLERS.get(event['action'], handle_unknown_event)
        handler(event)

    return Response()


def handle_unknown_event(event):
    log.info(pformat(event))


def handle_pull(event):
    log.info("ignoring pull event")


def handle_push(event):
    log.info("handling push event")

    target = event["target"]

    sub_handler = PUSH_EVENT_HANDLERS.get(target['mediaType'], handle_unknown_event)
    sub_handler(event)


def handle_push_layer(event):
    host = event["request"]["host"]
    image = event["target"]["repository"]
    digest = event["target"]["digest"]

    log.info(f"New layer for {host}/{image} {digest}")


def handle_push_manifest(event):
    host = event["request"]["host"]
    image = event["target"]["repository"]
    tag = event["target"]["tag"]

    log.info(f"New image {host}/{image}:{tag}")


EVENT_HANDLERS = {
    'pull': handle_pull,
    'push': handle_push,
}

PUSH_EVENT_HANDLERS = {
    'application/octet-stream': handle_push_layer,
    'application/vnd.docker.distribution.manifest.v2+json': handle_push_manifest,
}
