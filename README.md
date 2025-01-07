# Document Processing Task

This is a RESTful API project developed using Django and Django REST Framework that allows users to:
 - Upload a **PDF** or an **image** in the formats "pdf", "jpg", "jpeg", and "png".
 - Retrieve a specific image.
 - Rotate an image with a specific angle
 - Delete an image.
 - List all PDFs
 - Retrieve a specific PDF
 - Convert a PDF to images
 - Delete a PDF.

## Requirements

- Python (version 3.10.15)
- Django (version 5.1.4)
- Django REST Framework (version 3.15.2)

## Installation

### Using Docker

You can run the project using docker,

1. Create .env file and get the keys from the example.env file
2. Build and run docker compose (check commands in [Helpful commands](#helpful-commands))

#### Helpful commands

- docker compose build : you need this command just for the first time to build your dockerfile
- docker compose up: use this command each time you want to run the container
- docker compose exec app <command> : to run a specific command at the container, for example, to access the Django shell

### Using local environment

1. Create a virtual environment:

   `virtualenv venv`
   or
   `python3 -m venv venv`

2. Activate the virtual environment:

   - For Windows:
     `venv\Scripts\activate`

   - For macOS/Linux:  
      `source venv/bin/activate`

3. Install the project dependencies:

   `pip install -r requirements.txt`

4. Set up the database:

   `python manage.py migrate`

## Usage

1. Start the development server:

   `python manage.py runserver`

2. Open your web browser and navigate to http://127.0.0.1:8000/ to access the API.

### API Documentation

- The API documentation can be found at:
  `http://127.0.0.1:8000/api/docs/`
