# Base image
FROM registry.access.redhat.com/ubi8/python-36:latest

USER root

# Set working directory
RUN mkdir /opt/server
WORKDIR /opt/server

# Add and install requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Add rest of files
COPY . .

# Run server
EXPOSE 5000
CMD flask run --host 0.0.0.0
