# 🛒 E-commerce
This project is a comprehensive e-commerce platform built with Django.
It is designed to showcase Django's ORM capabilities, focusing on well-structured and optimized data models for products, users, orders, and payments.
The platform includes RESTful API endpoints with permissions tailored for buyers and suppliers.


## 📋 Features

- **Product Management**: Add, update, and delete products with categories and suppliers.
- **User Roles**: Two main user roles (buyers aka users and suppliers) with different permissions.
- **Order Management**: Create and manage orders with dynamic pricing based on discounts and quantity. 15% off for an item if a discount applied and 
- **API Endpoints**: RESTful API for managing products, orders, and reviews with role-based access control.
- **Reviews and Ratings**: Users can rate products and leave reviews.
- **Address Management**: Separate billing and shipping address management for orders.


## 🛠️ Technologies and Libraries
![Alt text for Logo1](https://camo.githubusercontent.com/0562f16a4ae7e35dae6087bf8b7805fb7e664a9e7e20ae6d163d94e56b94f32d/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f707974686f6e2d3336373041303f7374796c653d666f722d7468652d6261646765266c6f676f3d707974686f6e266c6f676f436f6c6f723d666664643534)
![Alt text for Logo2](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green) 
![Alt text for Logo3](https://img.shields.io/badge/django%20rest-ff1709?style=for-the-badge&logo=django&logoColor=white)
![Alt text for Logo3](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white) 
![Alt text for Logo3](https://img.shields.io/badge/Swagger-85EA2D?style=for-the-badge&logo=Swagger&logoColor=white)


## 🏁 Getting Started

These instructions will guide you through setting up the project on your local machine.

### Prerequisites

- Python 3.x
- pip
- Virtualenv (optional but recommended)
- PostgreSQL
- Other dependencies listed in `requirements.txt`
  
## Installation
### Setting Up a Virtual Environment 🔌 
1. **Clone the repository:**

  ```bash
  git clone git@github.com:Talantino/E-commerce.git
  ```

2. **Set up and activate a virtual environment:**

Creating a virtual environment is recommended to keep dependencies required by different projects separate.

- Install virtualenv if you haven't installed it yet:

    ```bash
    pip install virtualenv
    ```

- Create a virtual environment in the project directory:

    ```bash
    virtualenv venv
    ```

- Activate the virtual environment:

  - On Windows:

      ```bash
      venv\Scripts\activate
      ```

  - On Unix or MacOS:

      ```bash
      source venv/bin/activate
      ```

3. **Install dependencies:**

  With the virtual environment activated, install the project dependencies:

  ```bash
  pip install -r requirements.txt
  ```

4. **Configure the PostgreSQL database:**

    Ensure you have PostgreSQL installed and running. Create a database for this project and configure the database settings in your project's `settings.py` file.

5. **Perform database migrations:**

    Navigate to the `E-commerce` directory and apply migrations to set up your database schema:

    ```bash
    cd E-commerce
    python manage.py migrate
    ```

6. **Create a superuser:**

    Create a superuser for Django's admin panel with the following command:

    ```bash
    python manage.py createsuperuser
    ```

    Follow the prompts to set up the username, email, and password for the superuser.

7. **Run the project:**

    Start the Django development server:

    ```bash
    python manage.py runserver
    ```

    The project will be available at `http://127.0.0.1:8000/`.

## API Documentation and Testing

### 📗 Swagger UI

The project utilizes Django REST framework and drf-yasg for generating real-time API documentation using Swagger UI. This documentation provides a clear overview of all available API endpoints, their expected parameters, and response formats. Additionally, you can directly interact with the API through the Swagger UI to test endpoints.

To access the Swagger UI:
1. Ensure the project is running by following the [Installation](#installation) and [Running the server](#running-the-server) instructions.
2. Navigate to `/api/docs/` in your web browser. Example: `http://127.0.0.1:8000/api/docs/`

Here, you'll find a list of all API endpoints grouped by model. You can expand each endpoint to see detailed information and perform test requests directly from your browser.

### Testing API Endpoints

#### Using Swagger UI
1. Go to the Swagger UI page as described above.
2. Find the endpoint you wish to test and click on it to expand the section.
3. If required, click the "Try it out" button.
4. Enter any necessary parameters.
5. Click the "Execute" button to send a request to the API.
6. The response, including status code and payload, will be displayed directly in the UI.

#### Using `curl`
You can also test the API endpoints using `curl` from the command line. Here's an example of how to fetch a list of products:

```bash
curl -X GET "http://127.0.0.1:8000/api/products/" -H "accept: application/json"
```

### Using Postman
Postman is a popular tool for testing APIs. You can import the Swagger-generated documentation into Postman and use it to send requests to your API.

Open Postman and click the "Import" button.
Choose "Link" and paste the URL of your Swagger documentation. Example: http://127.0.0.1:8000/api/docs/?format=openapi
Once imported, you can select any endpoint, fill in any required parameters, and send requests to your API.
Note
Ensure you have appropriate permissions and are authenticated (if required by the endpoint) when testing protected API endpoints.

## Running the Server
To start the development server, use the following command:
```bash
python manage.py runserver
```
The server will start, and you can access the application and API at http://127.0.0.1:8000/

## 🤝 Contributing
Contributions to improve the project are welcome. Please feel free to fork the repository and submit pull requests.

## ✍️ Authors
Talantino - Initial work - git@github.com:Talantino

## ⚖️ License
This project is licensed under the MIT License - see the LICENSE.md file for details.

