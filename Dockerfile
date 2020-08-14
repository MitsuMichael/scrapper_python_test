
# Use an official Python runtime as a parent image
FROM python:3.7.0

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip --no-cache-dir install -r requirements.txt

# Make port 8080 available to the world outside this container
EXPOSE 5000

#CMD ["flask", "run", "--host=0.0.0.0"]
ENTRYPOINT ["python"] 
CMD ["app.py"] 