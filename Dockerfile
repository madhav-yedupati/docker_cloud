# Use a lightweight base image (even smaller than python:3.9-slim)
FROM python:3.9-alpine

# Set working directory
WORKDIR /app

# Copy only necessary files to minimize the image size
COPY script.py /app/
COPY home/data /home/data/

# Install dependencies efficiently
RUN pip install --no-cache-dir requests

# Ensure script.py has execute permissions (optional but good practice)
RUN chmod +x /app/script.py

# Run the script on container start
CMD ["python", "/app/script.py"]
