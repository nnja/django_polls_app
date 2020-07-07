import logging

from django.apps import AppConfig

logger = logging.getLogger(__name__)


class PollsConfig(AppConfig):
    name = 'polls'

    def ready(self):
        import os
        from django.conf import settings
        if os.environ.get('RUN_MAIN'):
            database_info = settings.DATABASES['default']
            logger.info(
                'Connecting to database host: %s with engine: %s',
                database_info['HOST'],
                database_info['ENGINE'])
            if settings.DEBUG:
                # Print URLs in DEBUG mode to be able to ctrl+click to open
                print('\nPolls app: http://127.0.0.1:8000/polls/')
                print('Admin site: http://127.0.0.1:8000/admin/\n')
