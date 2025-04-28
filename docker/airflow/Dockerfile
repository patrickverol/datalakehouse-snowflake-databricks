FROM apache/airflow:2.4.2

# Switch to root user for system package installation
USER root

# Install system dependencies for DBT
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    git \
    vim \
    nano \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Create DBT directory and set permissions
RUN mkdir -p /opt/airflow/dbt && \
    chown -R airflow:root /opt/airflow/dbt

# Switch back to airflow user for pip installations
USER airflow

# Add requirements file
COPY --chown=airflow:root requirements.txt .

# Upgrade pip first
RUN pip install --upgrade pip

# Install Python dependencies
RUN pip install -r requirements.txt

# Set working directory for DBT
WORKDIR /opt/airflow/dbt