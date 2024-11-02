FROM python:3.12-slim

# Installing Rust, required for some Python packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    curl \
    build-essential \
    && curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Changing ownership of files to the root user
RUN chown -R root:root /app
RUN chmod +x /app/app.py 

EXPOSE 5000

CMD ["python", "app.py"]
