FROM node:10-alpine

# Create working directory
RUN mkdir /opt/client
WORKDIR /opt/client

# Install app dependencies
COPY package.json package-lock.json ./
RUN npm set progress=false && npm ci

# Add node_module binaries on PATH
ENV PATH /opt/client/node_modules/.bin:$PATH

# Copy over source code
COPY . .

# Build the source
RUN npm run build

# Run the server
EXPOSE 3000
CMD [ "npm", "run", "start" ]
