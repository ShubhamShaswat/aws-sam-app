import json
from src.routes.routes import route_handler


def lambda_handler(event, context):
    print(event)
    body = {}
    statusCode = 200
    headers = {"Content-Type": "application/json"}

    try:
        response = route_handler(event, context)
        body = response
    except Exception as e:
        print(e)
        statusCode = 500
        body = {"status": "Error", "message": "Internal Server Error"}
    
    body = json.dumps(body)
    res = {
        "status": "Success",
        "message": "test messages",
        "data": body,
        "customCode": "TEST code",
    }
    return res


if __name__ == "__main__":
    from utils.dynamodb_client import DynamoDbClient

    # with open("output.json", "w") as f:
    #     items = DynamoDbClient().query_items("PROJECTDETAILS", "PROJECT#")
    #     json_data = json.dumps(items)
    #     f.write(json_data)
    #     f.close()

    item = {"pk": "test", "sk": "test_sk", "attributes": "value"}

    # # Calling the function under test
    # DynamoDbClient().put_item(item)

    # Example usage of the update_item method
    pk = "test"
    sk = "test_sk"
    update_expression = "SET attributes = :value"
    expression_attribute_values = {":value": "updated_value"}

    dynamo_client = DynamoDbClient()
    # dynamo_client.update_item(pk, sk, update_expression, expression_attribute_values)

    dynamo_client.delete_item("pk", "sk")
