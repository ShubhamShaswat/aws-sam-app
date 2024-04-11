import unittest
from unittest.mock import MagicMock
from utils.dynamodb_client import DynamoDbClient
from constants import TABLE_NAME


class DynamoDBClientTestCase(unittest.TestCase):
    def test_put_item(self):
        # Mocking the DynamoDB client
        dynamodb_client = MagicMock()

        # Mocking the input parameters
        item = {"pk": "test", "sk": "test_sk", "attributes": "value"}

        # Calling the function under test
        DynamoDbClient().put_item(item)

        # Asserting that the put_item method of the DynamoDB client was called with the correct parameters
        # dynamodb_client.put_item.assert_called_once_with(
        #     Item=item
        # )

    if __name__ == "__main__":
        unittest.main()
        # Mocking the input parameters
        
        