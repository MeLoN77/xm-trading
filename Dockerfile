# Use the official Python image
FROM python:3.10

# Set the working directory
WORKDIR /trade_xm_app

# Copy the requirements file
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files
COPY trade_xm_app ./trade_xm_app
COPY tests ./tests

# Set the PYTHONPATH environment variable
ENV PYTHONPATH=/trade_xm_app

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application (default)
CMD ["uvicorn", "trade_xm_app.main:app", "--host", "0.0.0.0", "--port", "8000"]
