### Prerequisites

Before you begin, ensure you have the following installed:

Python 3.x
pip (Python package installer)
Django (if not included in requirements)
Setup Instructions

1. Clone the Repository
First, clone the repository to your local machine:
git clone https://github.com/yourusername/ecommerce-site.git cd ecommerce-site

2. Create a Virtual Environment
To create a virtual environment, run the following commands:

For Windows: python -m venv venv
For macOS/Linux: python3 -m venv venv

3. Activate the Virtual Environment
Activate the virtual environment using the following command:

For Windows: venv\Scripts\activate
For macOS/Linux: source venv/bin/activate

4. Install Dependencies
Once the virtual environment is activated, install the required packages:
pip install -r requirements.txt

5. Apply Migrations
Run the following command to apply database migrations:
python manage.py makemigrations
python manage.py migrate

6. Run the Development Server
Start the development server with the following command:
python manage.py runserver

7. Access Master User
To access a superuser (master user) who can add products, go to http://127.0.0.1:8000/admin enter this username and password:
Username: itmgt
Password: password