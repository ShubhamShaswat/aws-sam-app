import json
from utils.dynamodb_client import DynamoDbClient


def list_projects():
    """
    Retrieves a list of projects from DynamoDB and prints each project.

    Returns:
        dict: A dictionary containing the project details.
    """
    dynamodb_client = DynamoDbClient()
    projects = dynamodb_client.query_items(pk="PROJECTDETAILS", sk="PROJECT#")
    return projects


def get_project_by_id(project_id):
    """
    Retrieves a project from DynamoDB based on the given project ID.

    Args:
        project_id (str): The ID of the project to retrieve.

    Returns:
        dict: A dictionary containing the project details.
    """
    dynamodb_client = DynamoDbClient()
    project = dynamodb_client.get_item(
        pk="PROJECTDETAILS",
        sk=f"PROJECT#{project_id}"
    )
    return project


def create_project(event):
    """
    Creates a project in DynamoDB based on the given event.

    Args:
        event (dict): The event containing the project details.

    Returns:
        dict: A dictionary containing the project details.
    """
    dynamodb_client = DynamoDbClient()
    event = json.loads(event['body'])
    event["pk"] = "PROJECTDETAILS"
    event["sk"] = f"PROJECT#{event['id']}"
    project = event
    dynamodb_client.put_item(item=project)
    return project


def delete_project(project_id):
    """
    Deletes a project from DynamoDB based on the given event.

    Args:
        event (dict): The event containing the project ID.

    Returns:
        dict: A dictionary containing the project details.
    """
    dynamodb_client = DynamoDbClient()
    project = dynamodb_client.delete_item(
        pk="PROJECTDETAILS",
        sk=f"PROJECT#{project_id}"
    )
    return project