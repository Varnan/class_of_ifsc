# server_health_check.py
import logging
try:
    import httplib
except:
    import http.client as httplib
    
from django.test import Client
logger = logging.getLogger('health')

from django.db import DEFAULT_DB_ALIAS, connections
from django.db.migrations.loader import MigrationLoader

logger = logging.getLogger('health')


def migrations_have_applied():
    """
    Check if there are any migrations that haven't been applied yet
    """

    connection = connections[DEFAULT_DB_ALIAS]
    loader = MigrationLoader(connection)

    graph = loader.graph

    # Count unapplied migrations
    num_unapplied_migrations = 0
    for app_name in loader.migrated_apps:
        for node in graph.leaf_nodes(app_name):
            for plan_node in graph.forwards_plan(node):
                if plan_node not in loader.applied_migrations:
                    num_unapplied_migrations += 1

    return num_unapplied_migrations == 0


def page_response(path, expected_status=httplib.OK):
    """
    Make an internal (fake) HTTP request to check a page returns the expected
    status code.

    """
    client = Client()
    try:
        response = client.get(path)
    except Exception as e:
        logger.error("Error from %s: %s", path, e)
        return False

    result = response.status_code == expected_status

    if not result:
        # Log healthcheck errors to Loggly so we can debug failing deployments
        # where the new instances fail the healthcheck.
        logger.error("Response from %s was %s, not %s",
                     path, response.status_code, status)
    return result