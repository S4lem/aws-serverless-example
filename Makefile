

start-api:
	sam build
	sam local start-api

deploy:
	sam build
	sam deploy --stack-name TodosApp --capabilities CAPABILITY_IAM --tags "project=TodoApp" --resolve-s3
