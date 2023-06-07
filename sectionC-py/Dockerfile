FROM python:3.9

# working directory in the container
WORKDIR /app

# required files to the working directory
COPY sayTheNumber.py .
COPY test.py .

# command to run the unit tests
CMD ["python3", "test.py"]
