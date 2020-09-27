# Charles Stolz Lab section 3 creating a Dockerfile
# 09-26-2020
# Use an existing docker image as base
FROM node:alpine

#Working directory to copy application files
WORKDIR /usr/app

#copy package.json
COPY ./package.json ./

# Download and install a dependency
RUN npm install

#copy files
COPY ./ ./

# Tell the image what to do when it starts as a container
# Default command
CMD ["npm", "start"]