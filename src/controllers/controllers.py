from src.models.models import list_projects, get_project_by_id, create_project, delete_project


def list_projects_handler(event, context):
    """
    Retrieves a list of projects from DynamoDB and prints each project.

    Args:
        event (dict): The event containing the project details.
        context (object): The context object.

    Returns:
        dict: A dictionary containing the project details.
    """
    return list_projects()


def get_project_by_id_handler(event, context):
    """
    Retrieves a project from DynamoDB based on the given project ID.

    Args:
        event (dict): The event containing the project details.
        context (object): The context object.

    Returns:
        dict: A dictionary containing the project details.
    """
    return get_project_by_id(event["pathParameters"]["id"])


def create_project_handler(event, context):
    """
    Creates a project in DynamoDB based on the given event.

    Args:
        event (dict): The event containing the project details.
        context (object): The context object.

    Returns:
        dict: A dictionary containing the project details.
    """
    return create_project(event)


def delete_project_handler(event, context):
    """
    Deletes a project from DynamoDB based on the given event.

    Args:
        event (dict): The event containing the project details.
        context (object): The context object.

    Returns:
        dict: A dictionary containing the project details.
    """
    return delete_project(event["pathParameters"]["id"])