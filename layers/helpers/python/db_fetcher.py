import boto3, uuid, os

class DatabaseManager:
    region = os.getenv("AWS_REGION") # env var always available
    
    dynamo = boto3.resource('dynamodb', region)

    @classmethod
    def get_list_item_db(cls, table_name):
        table = cls.dynamo.Table(table_name)
        try:
            list_items = table.scan()
        except Exception as e:
            print(e)
            raise
        return list_items['Items']
    
    @classmethod
    def get_item_db(cls, table_name, id_item):
        table = cls.dynamo.Table(table_name)

        try:
            item = table.get_item(Key={'id': id_item})['Item']
        except KeyError:
            return None
        except Exception:
            raise
        return item

    @classmethod
    def add_item_db(cls, table_name, item):
        
        if not item.get('id'):
            item['id'] = str(uuid.uuid4())

        expected_dict = {'id': {"Exists": False}}
        table = cls.dynamo.Table(table_name)
        table.put_item(Item=item, Expected=expected_dict)

        return item['id']

    @classmethod
    def delete_item_db(cls, table_name, id_item):
    
        table = cls.dynamo.Table(table_name)
    
        try:
            table.delete_item(Key={'id': id_item})
        except Exception as e:
            raise
        return True
