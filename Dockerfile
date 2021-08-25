# Base Image
FROM python:rc-buster
# Create app's directory
WORKDIR /Huffman-App
# Copy all the contents of the current directory to the image's directory
COPY . .
# Install dependencies
RUN pip3 install -r requirements.txt
# Expose required ports
EXPOSE 8000
# Run application with 3 working processes
CMD ["gunicorn","-b","0.0.0.0:8000","-w","3","run:huffman_app"]