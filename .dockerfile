FROM python:3.9
WORKDIR /app

# Install Black and Pylint
RUN pip install black pylint

# Copy the code to the container
COPY . .

# Run Black to format the code
RUN black .

# Run Pylint to check the code
RUN pylint . > pylint.txt || true

# Add the files to the container
ADD . .

# Set the entrypoint
ENTRYPOINT ["python", "main.py"]
