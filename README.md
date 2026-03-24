# G9 Shoe Store - E-Commerce Backend API

A robust, modular, and fully containerized REST API backend for an e-commerce shoe store. Architected with Python and Django, this system is decoupled into distinct service domains (Users, Products, Orders, Payments) to ensure scalability, maintainability, and clean separation of concerns. 

The application is configured for production environments, utilizing Docker for containerization, Gunicorn as the application server, and Nginx as a reverse proxy.

## 🚀 System Architecture
Client requests are routed through an **Nginx** reverse proxy, which serves media/static files and forwards dynamic requests to a **Gunicorn** application server running the **Django** backend. The entire stack is orchestrated using **Docker Compose**.

## ✨ Key Features
* **Modular Domain Design:** Clean architecture with isolated apps for `users`, `products`, `orders`, and `payments`.
* **User Authentication & Authorization:** Secure user registration, login, and token-based authentication.
* **Product Catalog Management:** Dynamic inventory tracking, product categorization, and media handling for shoe images.
* **Order Processing:** Seamless cart management, order checkout, and status tracking.
* **Payment Integration:** Secure payment processing architecture ready for third-party gateway integration.
* **Production-Ready Deployment:** Fully containerized with Docker, a custom `entrypoint.sh` for database migrations, and Gunicorn/Nginx configuration.

## 🛠️ Tech Stack
* **Framework:** Python, Django, Django REST Framework (DRF)
* **Server & Proxy:** Gunicorn, Nginx
* **Database:** SQLite (Configurable for PostgreSQL in production)
* **Containerization:** Docker, Docker Compose

## ⚙️ Local Development & Setup

### Prerequisites
* [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/) installed on your machine.
* Git

### Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Nyolmo/G9-Shoe-Store.git](https://github.com/Nyolmo/G9-Shoe-Store.git)
   cd G9-Shoe-Store
   Environment Variables:
2. Create a .env file in the root directory and configure your environment variables (refer to .env.example if available, or set your Django SECRET_KEY, DEBUG status, and database credentials).
3. 3.Build and Run the Docker Containers:
The project includes a production-ready docker-compose file. Run the following command to build the image and start the services:

##Bash
docker-compose -f docker-compose.prod.yml up -d --build
4.** Access the Application:

The API backend is now running and routed through Nginx.

Access the API at: http://localhost/ (or your configured domain/port).

Access the Django Admin panel at: http://localhost/admin/
**project structure:**

G9-Shoe-Store/
├── ecommerce_backend/      # Core project settings and URL routing
├── users/                  # User management and authentication
├── products/               # Product catalog, categories, and inventory
├── orders/                 # Cart, checkout, and order history
├── payments/               # Payment gateway processing logic
├── nginx/                  # Nginx reverse proxy configuration
├── media/                  # User-uploaded product images
├── Dockerfile              # Instructions to build the Django image
├── docker-compose.prod.yml # Production service orchestration
├── entrypoint.sh           # Pre-start script (migrations, static files)
└── gunicorn.conf.py        # Gunicorn server configuration




👨‍💻 Author
Rodney Nyolmo Kiptoo

LinkedIn: (https://www.linkedin.com/in/rodney-nyolmo-230562295/)

GitHub: https://github.com/Nyolmo

If you find this repository helpful, please consider giving it a ⭐!



   
