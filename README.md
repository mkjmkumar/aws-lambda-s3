## LocalStack
```
# aws configure
AWS Access Key ID [None]: test
AWS Secret Access Key [None]: test
Default region name [None]: us-east-1
Default output format [None]: json
```
# Verify Credentials 
```
cat ~/.aws/credentials
[default]
aws_access_key_id = test
aws_secret_access_key = test
```

# Edit to add the endpoint URL
```
vi ~/.aws/config
[default]
region = us-east-1
output = json
endpoint_url = http://host.docker.internal:4566
```


## ◆LocalStack test-bucket
```
# awslocal s3api create-bucket --bucket test-bucket
{
    "Location": "/test-bucket"
}
```

# awslocal s3 ls
2022-12-02 13:39:30 test-bucket
```
# vi test.txt
test.file
# cat test.txt
test.file
# awslocal s3 ls
2022-12-02 13:39:30 test-bucket
# awslocal s3 cp test.txt s3://test-bucket
upload: ./test.txt to s3://test-bucket/test.txt
# awslocal s3 ls test-bucket
2022-12-02 13:45:42         10 test.txt
```
```
# rm test.txt
# awslocal s3 cp s3://test-bucket/test.txt ./
download: s3://test-bucket/test.txt to ./test.txt
# vi test.txt
test.file

# cat test.txt
test.file
```

touch test2.txt
```
import boto3

def main() :
    client = boto3.client('s3', aws_access_key_id='test', aws_secret_access_key='test', region_name='us-east-1', endpoint_url='http://host.docker.internal:4566')
    response = client.list_buckets()
    client.upload_file('./test2.txt','test-bucket', 'test2.txt')
    print('upload complate')

if __name__ == "__main__":
    main()
#  python3 test.py
upload complate
```

```
# awslocal s3 ls s3://test-bucket
2022-12-30 20:48:30         11 test.txt
2022-12-30 23:53:08         12 test2.txt
```


## Lambda
```
lambda.py 
```

# zip lambda.zip lambda.py
  adding: lambda.py (deflated 42%)
```

```
# aws lambda create-function --function-name test --runtime python3.8 --handler lambda.lambda_handler --role arn:aws:iam::000000000000:role/lambda-role --zip-file fileb://lambda.zip
{
    "FunctionName": "test",
    "FunctionArn": "arn:aws:lambda:us-east-1:000000000000:function:test",
    "Runtime": "python3.8",
    "Role": "arn:aws:iam::000000000000:role/lambda-role",
    "Handler": "lambda.lambda_handler",
    "CodeSize": 514,
    "Description": "",
    "Timeout": 3,
    "MemorySize": 128,
    "LastModified": "2024-01-02T03:47:24.199735+0000",
    "CodeSha256": "tDeUS74lB3XlK5GGUHwA3P9G+5SZKAcC/fRDRm75DcQ=",
    "Version": "$LATEST",
    "TracingConfig": {
        "Mode": "PassThrough"
    },
    "RevisionId": "8bf0417d-395b-4f76-bd23-7e14a7430a59",
    "State": "Pending",
    "StateReason": "The function is being created.",
    "StateReasonCode": "Creating",
    "PackageType": "Zip",
    "Architectures": [
        "x86_64"
    ],
    "EphemeralStorage": {
        "Size": 512
    },
    "SnapStart": {
        "ApplyOn": "None",
        "OptimizationStatus": "Off"
    },
    "RuntimeVersionConfig": {
        "RuntimeVersionArn": "arn:aws:lambda:us-east-1::runtime:8eeff65f6809a3ce81507fe733fe09b835899b99481ba22fd75b5a7338290ec1"
    }
}
```
# aws lambda invoke --function-name test output.log
{
    "StatusCode": 200,
    "ExecutedVersion": "$LATEST"
}
```
# cat ./output.log
"create file2024-01-02-03-48-33.txt"
```
awslocal s3 ls s3://test-bucket
2024-01-02 03:48:33         16 2024-01-02-03-48-33.txt
2024-01-02 03:37:36         11 test.txt
2024-01-02 03:44:09          0 test2.txt
```

```
lambda2.py
```
ZIP作成
```
# zip lambda2.zip lambda2.py
```
# aws lambda create-function --function-name test2  --runtime python3.8 --handler lambda2.lambda_handler --role arn:aws:iam::000000000000:role/lambda-role  --zip-file fileb://lambda2.zip
{
    "FunctionName": "test2",
    "FunctionArn": "arn:aws:lambda:us-east-1:000000000000:function:test2",
    "Runtime": "python3.8",
    "Role": "arn:aws:iam::000000000000:role/lambda-role",
    "Handler": "lambda2.lambda_handler",
    "CodeSize": 627,
    "Description": "",
    "Timeout": 3,
    "MemorySize": 128,
    "LastModified": "2024-01-02T03:52:49.103099+0000",
    "CodeSha256": "+qCCSpN5LX9J4WG9EuDLTlPl3XmschVVweHs9XJ+klw=",
    "Version": "$LATEST",
    "TracingConfig": {
        "Mode": "PassThrough"
    },
    "RevisionId": "3c85a2fd-af28-4d4f-93ff-681d0a0baa3b",
    "State": "Pending",
    "StateReason": "The function is being created.",
    "StateReasonCode": "Creating",
    "PackageType": "Zip",
    "Architectures": [
        "x86_64"
    ],
    "EphemeralStorage": {
        "Size": 512
    },
    "SnapStart": {
        "ApplyOn": "None",
        "OptimizationStatus": "Off"
    },
    "RuntimeVersionConfig": {
        "RuntimeVersionArn": "arn:aws:lambda:us-east-1::runtime:8eeff65f6809a3ce81507fe733fe09b835899b99481ba22fd75b5a7338290ec1"
    }
}
```
# aws lambda invoke --function-name test2 result2.log
{
    "StatusCode": 200,
    "ExecutedVersion": "$LATEST"
}

```
# cat result2.log
"create file2024-01-02-03-54-03.txt"
```
# awslocal s3 ls s3://test-bucket
2024-01-02 03:48:33         16 2024-01-02-03-48-33.txt
2024-01-02 03:54:03         16 2024-01-02-03-54-03.txt
2024-01-02 03:37:36         11 test.txt
2024-01-02 03:44:09          0 test2.txt
```

## Lambda(test3)
```
test3.py
```
ZIP
```
# zip lambda3.zip test3.py
```
# aws lambda create-function --function-name test3  --runtime python3.8 --handler test3.handler --role arn:aws:iam::000000000000:role/lambda-role  --zip-file fileb://lambda3.zip
{
    "FunctionName": "test3",
    "FunctionArn": "arn:aws:lambda:us-east-1:000000000000:function:test3",
    "Runtime": "python3.8",
    "Role": "arn:aws:iam::000000000000:role/lambda-role",
    "Handler": "test3.handler",
    "CodeSize": 480,
    "Description": "",
    "Timeout": 3,
    "MemorySize": 128,
    "LastModified": "2024-01-02T03:56:27.517094+0000",
    "CodeSha256": "zJs6uz6C7saF9u5F586FN7LHjFlglDmpkdzfcSPMwXw=",
    "Version": "$LATEST",
    "TracingConfig": {
        "Mode": "PassThrough"
    },
    "RevisionId": "dd4f5dda-2ee7-4b2c-ac51-18160c87ce68",
    "State": "Pending",
    "StateReason": "The function is being created.",
    "StateReasonCode": "Creating",
    "PackageType": "Zip",
    "Architectures": [
        "x86_64"
    ],
    "EphemeralStorage": {
        "Size": 512
    },
    "SnapStart": {
        "ApplyOn": "None",
        "OptimizationStatus": "Off"
    },
    "RuntimeVersionConfig": {
        "RuntimeVersionArn": "arn:aws:lambda:us-east-1::runtime:8eeff65f6809a3ce81507fe733fe09b835899b99481ba22fd75b5a7338290ec1"
    }
}
```
# aws lambda invoke --function-name test3 result3.log
{
    "StatusCode": 200,
    "ExecutedVersion": "$LATEST"
}
```
# cat result3.log
{"message":"a-object placed into S3"}
```
# awslocal s3 ls s3://
2024-01-02 03:33:20 test-bucket
2024-01-02 03:57:02 a-bucket
```
# awslocal s3 ls s3://a-bucket
2024-01-02 03:57:02          9 a-object
```
