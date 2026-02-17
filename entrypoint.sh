#!/bin/bash
# entrypoint.sh
# This script starts SSH, MySQL/MariaDB, and optionally Streamlit based on environment variables.

# Ensure the SSH runtime directory exists.
mkdir -p /var/run/sshd

# Ensure the MySQL/MariaDB socket directory exists and set proper ownership.
mkdir -p /run/mysqld
chown -R mysql:mysql /run/mysqld

# Start the SSH daemon directly.
nohup /usr/sbin/sshd > /dev/null 2>&1 &

# Start MariaDB/MySQL directly through mysqld_safe.
nohup mysqld_safe --datadir=/var/lib/mysql > /dev/null 2>&1 &

# Optional: start Streamlit if RUN_STREAMLIT is set to "yes".
if [ "$RUN_STREAMLIT" = "yes" ]; then
  echo "Starting Streamlit..."
  nohup streamlit run /home/$SSH_USERNAME/app/main.py > /dev/null 2>&1 &
fi

# Optional: wait a few seconds to allow services to initialize.
sleep 5

# Print a simple status message (for debugging/educational purposes).
echo "sshd and mysqld are now running."
if [ "$RUN_STREAMLIT" = "yes" ]; then
  echo "Streamlit is running."
fi
echo "You can try connecting to MySQL with: mysql -u root -p"
echo "And SSH using: ssh \$SSH_USERNAME@localhost -p 2222"

# Keep the container running.
tail -f /dev/null
