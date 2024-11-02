# Translation App

## Requirements
- Ensure you have [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/) installed on your machine.

## Running the Application

1. **Navigate to the Project Directory**:
   ```bash
   cd path/to/your/project
   ```

2. **Build and Start the Application**:
   ```bash
   docker build -t ettranslation-flask_app .
   docker run -p 5000:5000 --name translation_app ettranslation-flask_app
   ```

3. **Access the Application**: Open your web browser and go to `http://127.0.0.1:5000`.

## Stopping the Application

To stop the application, you can press `Ctrl+C` in the terminal where you ran `docker-compose up`. Alternatively, run:
```bash
docker-compose down
