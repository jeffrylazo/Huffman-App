# Huffman-Web-App

## Summary:
A simple web application that uses Huffman coding to achieve lossless compression and decompression of text.

## Composition:
1. Server Side - Python.
2. Client Side - HTML, CSS, JavaScript.

## Installation of dependencies:
pip3 install -r requirements.txt

## Run application:
1. Development: python3 run.py
2. Production: gunicorn -b 0.0.0.0:8000 -w 3 "run:huffman_app"