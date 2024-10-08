# Use a simple Ubuntu image
FROM python:3.9.12-slim as builder

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install necessary packages
RUN apt-get update && \
    apt-get install -y python3 python3-pip libpq-dev gcc sshpass && \
    rm -rf /var/lib/apt/lists/*

# Create application directories
RUN mkdir -p /usr/src/app/media
RUN mkdir -p /usr/src/app/static
WORKDIR /usr/src/app

# Copy requirements file and install Python dependencies
COPY ./backend/requirements.txt /usr/src/app/requirements.txt
RUN pip3 install --upgrade pip && \
    pip3 install -r requirements.txt

# Copy the script and application code
COPY ./backend/scrypt.sh /usr/src/app/scrypt.sh
COPY ./backend /usr/src/app/

# Make the script executable
RUN chmod +x /usr/src/app/scrypt.sh

EXPOSE 8000
## Set the entry point
ENTRYPOINT ["/usr/src/app/scrypt.sh"]
# I've enabled ssh tunnel for prod, so it's more doesn't necessary
