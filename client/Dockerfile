FROM node:10

# Set working directory
WORKDIR /opt/client

# A wildcard is used to ensure both package.json AND package-lock.json are copied
COPY package*.json ./

## Install only the packages defined in the package-lock.json (faster than the normal npm install)
RUN npm install

# Copy the contents of the project to the image
COPY . .

# Build the source
RUN npm run build

EXPOSE 3000
CMD ["npm", "run", "start"]
