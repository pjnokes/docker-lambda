# Datacrunch's Lambda Docker

This is the template to use [Serverless' Framework](https://www.serverless.com/) in deploying AWS Lambda functions with a few commands.

## Pre-requisites:

1. Ensure the latest version of NodeJS is installed
2. Python is installed
3. The Serverless framework installed by running `npm install -g serverless`
4. The AWS CLI installed. [Directions here.](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
5. A somewhat recent version of Docker installed.

## How to clone this repository
**Note: if using powershell as your shell, the "sls" alias command won't natively work. If using Powershell, you will need to type out "serverless" instead of "sls" when running commands.**

1. Navigate to the client's folder in sharepoint
2. Create a new folder for this code to live in
3. Open up a shell in this folder (git bash preferred for me on windows)
4. Run `sls create --template-url https://github.com/pjnokes/docker-lambda --path=NEW-PROJECT-NAME` This will clone this template into the folder with the new name you put for the path variable.

## How to configure the template

### Initial Configuration

1. If your python code is in a jupyter notebook, convert it into a .py file and place in this folder directory
2. Configure AWS CLI credentials if you haven't already:
    1. Go to the client's AWS and navigate to the IAM service.
    2. Click "Users" on the left-hand side.
    3. Click "Add users" on the right
    ![Steps 2 and 3](/images/AWS_steps_2_3.png)
    4. Give this user a name. Maybe something like "CLIENTNAME_datacrunch_programmatic"
    5. Click "Access key - Programmatic access"
    ![Steps 4 and 5](/images/aws_steps_4_5.png)
    6. Click "Attach existing policies directly"
    7. Click "AdministratorAccess". If your user doesn't have AdministratorAccess, you may have to give only specific permission for what you have access to.
    ![Steps 6 and 7](/images/aws_steps_6_7.png)
    8. Click "Next: tags".
    9. Click "Next: review".
    10. Click "Create user".
    11. Copy the Access Key ID and Secret Access Key that are shown. Note this Secret Access Key will only show once.
    12. In a terminal, type `aws configure --profile=<CLIENT-NAME>`
    13. Enter in the Access Key ID and Secret Access Key when prompted to do so.
    14. Enter the default region for the client. Typically it is Northern Virginia (us-east-1), Ohio (us-east-2), or Oregon (us-west-1). Pick the one closest to the client. Don't use Northern California as charges are more expensive there.

### Edit Template

1. Edit `serverless.yml` in the following places (You will see prompts on what to put in each location):
    1. `service: <SERVICE-NAME-HERE>`
    2. `region: ${env:AWS_REGION, 'us-east-1'}`
    3. `profile: <AWS-CLI-PROFILE-NAME-HERE>`
    4. `name: <NAME-OF-FUNCTION-HERE>`
    5. `description: <Description here if desired>`
    6. `timeout: 60`
    7. `memorySize: 1024`
    8. `schedule: cron(0 8 * * ? *)`
2. Edit `Dockerfile` in the following places:
    1. `COPY test.py ./`
    2. `CMD [ "test.handler" ]`
3. Edit `/.vscode/tasks.json` in the following places:
    1. `"tag": "docker-lambda:latest",`
    2. `"file": "test.py"`
4. Edit `requirements.txt` with your packages needed. Pro tip: you can run the generate requirements.txt from a python file by [running this library](https://pypi.org/project/pipreqs/).

### Wrap-up and Deploy

1. Delete the `test.py`, `images` folder, this readme (or modify it)
2. Don't forget to push your code + dockerfile into a git repository on our gitlab server
3. Deploy your code with `sls deploy`
4. Double check it and run it in AWS Lambda to ensure it works as expected.

## Miscellaneous

### Selenium
    [Adapt this project](https://github.com/umihico/docker-selenium-lambda) if you are wanting to use Selenium in your docker file.