from src.controllers.controllers import list_projects_handler, get_project_by_id_handler, create_project_handler, delete_project_handler


def route_handler(event, context):
    """
    The main Lambda handler function.

    Args:
        event (dict): The event containing the project details.
        context (object): The context object.

    Returns:
        dict: A dictionary containing the project details.
    """
    if event["routeKey"] == "GET /projects":
        return list_projects_handler(event, context)
    elif event["routeKey"] == "GET /projects/{id}":
        return get_project_by_id_handler(event, context)
    elif event["routeKey"] == "PUT /projects":
        return create_project_handler(event, context)
    elif event["routeKey"] == "DELETE /projects/{id}":
        return delete_project_handler(event, context)
    else:
        return {
            "statusCode": 400,
            "body": "Unsupported route: " + event["routeKey"]
        }
