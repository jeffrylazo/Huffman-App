# Base Image
FROM python:rc-buster
# Create app's directory
WORKDIR /Huffman-Web-App
# Copy all the contents of the current directory to the image's directory
COPY . .
# Install dependencies
RUN pip3 install -r requirements.txt
# Expose required ports
EXPOSE 8080
# Run application
CMD ["uwsgi","app.ini"]