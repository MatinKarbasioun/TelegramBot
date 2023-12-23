FROM jfrog.farabixo.tech/algorithm-docker/base/python-mssql-git-client:17

LABEL authors="Matin Karbasioun"

# Create and set the working directory
WORKDIR /app

# Install Requirements File
RUN pip install --upgrade pip

COPY requirements.txt /app/requirements.txt

# Install requirement.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Expose port 8000 for the Django application
EXPOSE 8000

# Run Gunicorn with your Django project
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]