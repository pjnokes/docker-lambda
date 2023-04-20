FROM public.ecr.aws/lambda/python@sha256:ac758b6345b677eb6e72c2cd0f71c182eca773da5db1e17835a4ffef46dbc997 as build
# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

#OVERWRITE THE FIRST VALUE WITH YOUR PRIMARYFILE.py. KEEP THE "./"
COPY test.py ./

#OVERWRITE THE FOLLOWING VALUE WITH YOUR PRIMARYFILE.MAINMETHOD
CMD [ "test.handler" ]
