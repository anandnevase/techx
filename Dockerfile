# Base OS
FROM alpine:3.1

MAINTAINER Anand Nevase <anand.nevase@xoriant.com>

# Install required packages
RUN apk --update add python py-pip openssl ca-certificates yaml \
    # Install build dependencies
    && apk --update add --virtual build-dependencies python-dev build-base wget yaml-dev \
    # Remove the build dependencies
    && apk del build-dependencies

# Copy All the eggs for installation
WORKDIR /calculator
COPY ./dist /calculator
COPY ./scripts /calculator
EXPOSE 8080
# Build and install calculator package
RUN sh calculator.sh install
CMD ["sh", "calculator.sh", "run"]
