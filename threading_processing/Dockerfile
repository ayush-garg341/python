FROM alpine:3.6
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
RUN apk update && apk add python3
RUN apk add gcc python3-dev musl-dev linux-headers
RUN python3 -m pip install --upgrade pip
COPY * /usr/src/app
