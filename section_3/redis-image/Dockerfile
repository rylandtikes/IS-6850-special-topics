# Charles Stolz Lab section 3 creating a Dockerfile
# 09-19-2020
# Use an existing docker image as base
FROM alpine
# Download and install a dependancy
RUN apk add --update gcc
RUN apk add --update redis

# Tell the image what to do when it starts as a container
CMD ["redis-server"]