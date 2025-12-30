# ---------------------------------------------
# IMPORT REQUIRED LIBRARIES
# ---------------------------------------------
# FastAPI is used to create API-based web apps
from fastapi import FastAPI

# HTMLResponse allows us to return HTML pages
from fastapi.responses import HTMLResponse


# ---------------------------------------------
# CREATE FASTAPI APPLICATION OBJECT
# ---------------------------------------------
# This 'app' is the main API instance
app = FastAPI()


# ---------------------------------------------
# ROUTE 1: HOME PAGE (LAUNCH PAGE)
# URL: http://localhost:8000/
# ---------------------------------------------
@app.get("/", response_class=HTMLResponse)
def home():
    """
    This function returns the HOME PAGE of the website.
    It contains:
    - Title
    - Image
    - Launch button
    Clicking the button navigates to the next page (/resources).
    """

    return """
    <html>
    <head>
        <title>Smart Agriculture Portal</title>

        <!-- Internal CSS for styling -->
        <style>
            body {
                font-family: Arial;
                background: linear-gradient(to right, #43cea2, #185a9d);
                text-align: center;
                color: white;
            }

            .card {
                margin-top: 60px;
                padding: 30px;
            }

            button {
                padding: 15px 25px;
                font-size: 18px;
                background-color: #0d6efd;
                color: white;
                border: none;
                border-radius: 10px;
                cursor: pointer;
            }

            button:hover {
                background-color: #084298;
            }

            img {
                width: 320px;
                border-radius: 15px;
                margin-top: 20px;
            }
        </style>
    </head>

    <body>
        <div class="card">
            <h1>🌾 Smart Agriculture Information System</h1>
            <p>Click below to access official agriculture resources</p>

            <!-- Agriculture-related image -->
            <img src="https://images.unsplash.com/photo-1500937386664-56f7d1f7a6f0">

            <br><br>

            <!-- Launch button -->
            <!-- When clicked, it moves to /resources page -->
            <form action="/resources">
                <button>🚀 Launch Agriculture Resources</button>
            </form>
        </div>
    </body>
    </html>
    """


# ---------------------------------------------
# ROUTE 2: RESOURCES PAGE
# URL: http://localhost:8000/resources
# ---------------------------------------------
@app.get("/resources", response_class=HTMLResponse)
def resources():
    """
    This function returns the SECOND PAGE.
    It provides:
    - Agriculture information
    - Buttons linking to official government websites
    - Back button to return to home page
    """

    return """
    <html>
    <head>
        <title>Government Agriculture Resources</title>

        <!-- Internal CSS for second page -->
        <style>
            body {
                font-family: Arial;
                background-color: #f0fdf4;
                color: #14532d;
                text-align: center;
            }

            .box {
                margin: 50px;
                padding: 30px;
                background-color: white;
                border-radius: 15px;
                box-shadow: 0px 0px 15px #aaa;
            }

            button {
                padding: 14px 22px;
                font-size: 16px;
                background-color: #16a34a;
                color: white;
                border: none;
                border-radius: 8px;
                margin: 10px;
                cursor: pointer;
            }

            button:hover {
                background-color: #166534;
            }

            img {
                width: 280px;
                border-radius: 12px;
            }

            a {
                text-decoration: none;
            }
        </style>
    </head>

    <body>
        <div class="box">
            <h2>🌱 Official Government Agriculture Websites</h2>

            <!-- Agriculture image -->
            <img src="https://images.unsplash.com/photo-1592982537447-6c4f84a59e07">

            <p>Select trusted government resources:</p>

            <!-- India Agriculture Ministry -->
            <a href="https://agricoop.nic.in/" target="_blank">
                <button>🇮🇳 India – Ministry of Agriculture</button>
            </a>

            <!-- India National Agriculture Portal -->
            <a href="https://www.india.gov.in/topics/agriculture" target="_blank">
                <button>🇮🇳 India – National Agriculture Portal</button>
            </a>

            <!-- USA Department of Agriculture -->
            <a href="https://www.usda.gov/" target="_blank">
                <button>🇺🇸 USA – Department of Agriculture</button>
            </a>

            <br><br>

            <!-- Back button to return to home page -->
            <a href="/">
                <button>⬅ Back to Home</button>
            </a>
        </div>
    </body>
    </html>
    """