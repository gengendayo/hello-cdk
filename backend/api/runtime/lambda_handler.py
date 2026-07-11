import json
import os
import boto3

# DynamoDBを操作するための準備
dynamodb = boto3.resource('dynamodb')

def handler(event, context):
    # api_stack.pyで設定した環境変数からテーブル名を読み込む
    table_name = os.environ.get('DYNAMODB_TABLE_NAME')
    table = dynamodb.Table(table_name)

    # DynamoDBのテーブルからデータを全件取得 (Scan)
    response = table.scan()

    # API Gateway（ブラウザ等）に返すための形式に整えて出力
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps(response)
    }