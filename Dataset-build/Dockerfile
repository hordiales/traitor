ARG BASE=python:3.10

FROM ${BASE}

#ENV MODEL_PATH /model

#RUN mkdir -p /model
RUN apt-get update
RUN pip install google-cloud-storage

RUN pip install git pip

# Copy the Python script into the container (you need to have a script in the same directory)
COPY gcp_process_features.py /app/process_features.py

# Set the working directory
WORKDIR /app

# Use the Python script as the entry point
CMD ["python", "process_features.py"]
