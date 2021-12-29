import json, os
from db_fetcher import DatabaseManager
from http_response import HttpResponse

TABLE_NAME_TODOS = os.environ["TABLE_NAME_TODOS"]

def lambda_handler(event, context):
    """
    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    method = event.get('httpMethod')
    endpoint = event.get('resource')
    path_parameters = event.get('pathParameters')
    payload = event.get('body')


    if method == 'GET' and endpoint == "/todos":
        # Get a list todos
        todos = DatabaseManager.get_list_item_db(table_name=TABLE_NAME_TODOS)
        return HttpResponse.success(todos)

    if method == 'POST' and endpoint == "/todos":
        # Add a new todo
        try:
            payload = json.loads(payload)
        except Exception as e:
            print(e)
            return HttpResponse.bad_request()

        if not payload.get('label'):
            return HttpResponse.bad_request()
        
        new_item_id = DatabaseManager.add_item_db(table_name=TABLE_NAME_TODOS, item=payload)
        return HttpResponse.success(message=f'Todo with id {new_item_id} added')

    if method == 'DELETE' and endpoint == "/todos/{todoId}":
        # remove a todo
        todo_id = path_parameters['todoId']
        try:
            DatabaseManager.delete_item_db(table_name=TABLE_NAME_TODOS, id_item=todo_id)
        except:
            return HttpResponse.internal_error()

        return HttpResponse.success(message=f'Todo with id {todo_id} deleted')

    return HttpResponse.not_found(message='Not found')
