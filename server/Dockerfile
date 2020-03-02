# Base image
FROM registry.access.redhat.com/ubi8/python-36:latest

USER root

# Set working directory
ENV APP_ROOT=/opt/server
RUN mkdir ${APP_ROOT}

# Set permissions to app dir for generic users
RUN chmod -R u+x ${APP_ROOT} && \
    chgrp -R 0 ${APP_ROOT} && \
    chmod -R g=u ${APP_ROOT} /etc/passwd
USER 1001

WORKDIR ${APP_ROOT}

# Add and install requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Add rest of files
COPY . .

# Run server
EXPOSE 5000
CMD python manage.py run -h 0.0.0.0
