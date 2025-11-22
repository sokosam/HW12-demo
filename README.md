# HW12-demo

## Database Connection Test (Intentional Failure)

This project demonstrates a containerized application that attempts to connect to a non-existent database, designed to fail for testing purposes.

### Features

- Python application that attempts database connection
- 10-second delay before connection attempt (allows time to observe logs)
- Intentional failure with detailed error messages
- Containerized with Docker

### Running the Application

**Using Docker Compose (Recommended):**

```bash
docker-compose up --build
```

**Using Docker directly:**

```bash
# Build the image
docker build -t db-test-app .

# Run the container
docker run --name db-test-app db-test-app
```

### Expected Behavior

1. Container starts and displays "Starting application..."
2. Waits 10 seconds (you can monitor logs during this time)
3. Attempts to connect to database
4. Fails with connection error (intentional)
5. Container exits with error code

### Viewing Logs

```bash
# If using docker-compose
docker-compose logs -f

# If using docker directly
docker logs -f db-test-app
```

### Testing Notes

The application intentionally tries to connect to a non-existent database host (`nonexistent-database-host`) to simulate connection failures. This is useful for testing error handling, monitoring, and logging systems.
