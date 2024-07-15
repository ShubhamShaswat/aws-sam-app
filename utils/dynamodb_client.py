from decimal import Decimal
from io import BytesIO
import json
import logging
import os
from pprint import pprint
import requests
from zipfile import ZipFile
import boto3
from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError
from constants import TABLE_NAME

logger = logging.getLogger(__name__)


class DynamoDbClient:
    def __init__(self):
        self.client = boto3.client("dynamodb")
        self.resource = boto3.resource("dynamodb")
        self.table = self.resource.Table(TABLE_NAME)

    def exists(self, table_name):
        """
        Determines whether a table exists. As a side effect, stores the table in
        a member variable.

        :param table_name: The name of the table to check.
        :return: True when the table exists; otherwise, False.
        """
        try:
            table = self.resource.Table(table_name)
            table.load()
            exists = True
        except ClientError as err:
            if err.response["Error"]["Code"] == "ResourceNotFoundException":
                exists = False
            else:
                logger.error(
                    "Couldn't check for existence of %s. Here's why: %s: %s",
                    table_name,
                    err.response["Error"]["Code"],
                    err.response["Error"]["Message"],
                )
                raise
        else:
            self.table = table
        return exists

    def get_item(self, pk, sk):
        """
        Gets data from the table for a specific item.

        :param pk: The partition key of the item.
        :param sk: The sort key of the item.
        :return: The data about the requested item.
        """
        try:
            response = self.table.get_item(Key={"pk": pk, "sk": sk})
        except ClientError as err:
            logger.error(
                "Couldn't get item %s from table %s. Here's why: %s: %s",
                pk,
                self.table.name,
                err.response["Error"]["Code"],
                err.response["Error"]["Message"],
            )
            raise
        else:
            return response["Item"]

    def query_items(self, pk, sk):
        """
        Queries for items that were released in the specified year.

        :param year: The year to query.
        :return: The list of movies that were released in the specified year.
        """
        try:
            response = self.table.query(
                KeyConditionExpression=Key("pk").eq(pk)
                & Key("sk").begins_with(sk)
            )
        except ClientError as err:
            logger.error(
                "Couldn't query for movies released in %s. Here's why: %s: %s",
                pk,
                err.response["Error"]["Code"],
                err.response["Error"]["Message"],
            )
            raise
        else:
            return response["Items"]
    
    def put_item(self, item):
        """
        Adds an item to the table.

        :param item: The item to add.
        """
        try:
            self.table.put_item(Item=item)
        except ClientError as err:
            logger.error(
                "Couldn't put item %s in table %s. Here's why: %s: %s",
                item,
                self.table.name,
                err.response["Error"]["Code"],
                err.response["Error"]["Message"],
            )
            raise

    def delete_item(self, pk, sk):
        """
        Deletes an item from the table.

        :param pk: The partition key of the item.
        :param sk: The sort key of the item.
        """
        try:
            self.table.delete_item(Key={"pk": pk, "sk": sk})
        except ClientError as err:
            logger.error(
                "Couldn't delete item %s from table %s. Here's why: %s: %s",
                pk,
                self.table.name,
                err.response["Error"]["Code"],
                err.response["Error"]["Message"],
            )
            raise

    def update_item(self, pk, sk, update_expression,
                    expression_attribute_values):
        """
        Updates an item in the table.

        :param pk: The partition key of the item.
        :param sk: The sort key of the item.
        :param update_expression: The update expression.
        :param expression_attribute_values: The expression attribute values.
        """
        try:
            self.table.update_item(
                Key={"pk": pk, "sk": sk},
                UpdateExpression=update_expression,
                ExpressionAttributeValues=expression_attribute_values,
            )
        except ClientError as err:
            logger.error(
                "Couldn't update item %s in table %s. Here's why: %s: %s",
                pk,
                self.table.name,
                err.response["Error"]["Code"],
                err.response["Error"]["Message"],
            )
            raise
        
