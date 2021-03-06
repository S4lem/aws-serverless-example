# Todo-list Back-end Application with SAM

This project contains source code for a serverless Todos application using Python 3.8 and SAM (Serverless Application Model).

You will be able to add, remove and list the Todo-list.

It includes the following files and folders.
- lambdas - Code for the application's Lambda functions.
- layers - Code to avoid code duplication accross lambda functions.
- postman_collection.json - pre-made requests
- Makefile : command shortcuts
- template.yaml - A template that defines the application's AWS resources.

The application uses several AWS resources:
- Lambda Functions
- Layers
- Api Gateway
- DynamoDB
- CloudFormation


## Prerequisites :

* SAM CLI - [Install the SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
* [Python 3.8 installed](https://www.python.org/downloads/)
* Docker - [Install Docker community edition](https://hub.docker.com/search/?type=edition&offering=community)
* Run `aws configure` and set your region, AKI and SAK


## Run locally

To build and deploy your application for the first time, run the following in your shell:

```bash
make deploy
```

If you're on windows and don't have the `make` command available, just open the Makefile and run manually the subsequent commands.

Then, run the following command to start the API locally on port 3000.

```bash
make start-api
```

You're now free to test locally. You can also import the provided postman collection to Postman.



