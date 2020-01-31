# Base image
FROM registry.access.redhat.com/ubi8/python-36:latest

USER root

# Set working directory
RUN mkdir /opt/server
WORKDIR /opt/server

# Add and install requirements
COPY requirements.txt .
RUN source /opt/app-root/etc/scl_enable && \
    set -x && \
    pip install -U pip setuptools wheel && \
    cd /opt/server && pip install -r requirements.txt

# Add rest of files
COPY . .

# Run server
EXPOSE 5000
CMD python manage.py run -h 0.0.0.0
