#!/bin/bash
set -exv -o pipefail

# CD into workspace
cd /tmp/workspace

# Export environment variables into session
if [ -f /tmp/workspace/env.prod ]; then
    source /tmp/workspace/env.prod
fi

# Build the new container images
docker-compose -f docker-compose-cd.yml build

# Bring down any running containers and delete images
docker-compose -f docker-compose-cd.yml down || true
docker-compose -f docker-compose-cd.yml rm -f -v -s || true

# Run the new containers
docker-compose -f docker-compose-cd.yml up -d