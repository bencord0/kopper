import logging

from rest_framework.decorators import api_view
from rest_framework.response import Response

log = logging.getLogger(__name__)


@api_view(['GET', 'POST'])
def handle_event(request):
    log.info(request.body)
    return Response()
