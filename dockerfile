# Use the latest Python 3.12 slim image
FROM python:3.12-slim

# Set non-interactive mode for apt-get
ENV DEBIAN_FRONTEND=noninteractive

# Update package lists and install required packages.
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    openssh-server \
    sudo \
    vim \
    git \
    less \
    mariadb-server \
    mariadb-client \
    python3-venv && \
    rm -rf /var/lib/apt/lists/*

# Create the runtime directory for SSH
RUN mkdir -p /var/run/sshd

# Create a user (default is "student") and add to sudo group.
# (This user name will later be matched with the environment variable.)
RUN useradd -ms /bin/bash student && echo "student:student" | chpasswd && adduser student sudo

# Enforce best practices by requiring pip to operate inside a virtual environment.
# This will cause any attempt to run pip without first doing something like:
#   python -m venv venv && source venv/bin/activate
# to result in an error.
ENV PIP_REQUIRE_VIRTUALENV=1

# Set the working directory.
# Note: This may be overmounted by a volume mount from Vagrant.
WORKDIR /home/student/app

# Expose SSH (22), Streamlit (8501), and MariaDB (3306) ports.
EXPOSE 22 8501 3306

# Copy our entrypoint script into the image.
COPY entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh

# Run the entrypoint script.
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
