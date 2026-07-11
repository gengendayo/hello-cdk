# AWS CDK Serverless Backend Demo

## 概要
AWS Cloud Development Kit (CDK) と Python を用いて、サーバーレスなバックエンドAPI環境を構築した学習用プロジェクトです。
クラウドインフラをコード（IaC: Infrastructure as Code）で定義し、構築から解体までのプロセスを自動化する実践的なアプローチを検証しました。

## アーキテクチャ
本システムは、以下のAWSサービスを連携させたシンプルなサーバーレス構成です。

- **Amazon API Gateway**: クライアントからのリクエストを受け付けるエンドポイント
- **AWS Lambda (Python)**: 中間処理を行うバックエンドロジック
- **Amazon DynamoDB**: データを格納するNoSQLデータベース

APIにアクセスが発生するとLambda関数が起動し、環境変数からテーブル名を読み取ってDynamoDBへアクセスし、格納されているデータを全件取得（Scan）してJSON形式で返却します。

## 使用技術
- **AWS CDK v2**
- **Python 3.x**
- **AWS IAM** / **CloudWatch** (実行権限とログ管理)

## 環境構築と実行手順

1. **デプロイ（構築）**
   ```bash
   cdk deploy "Dev/*"