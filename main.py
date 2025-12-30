from flask import Flask

app = Flask(_name_)

# ---------------------------------
# PAGE 1 : HOME PAGE
# ---------------------------------
@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>Smart Agriculture Portal</title>
        <style>
            body {
                font-family: Arial;
                background: linear-gradient(to right, #a8e063, #56ab2f);
                text-align: center;
                color: white;
            }
            .container {
                margin-top: 60px;
            }
            button {
                padding: 15px 25px;
                font-size: 18px;
                background-color: #2e7d32;
                color: white;
                border: none;
                border-radius: 8px;
                cursor: pointer;
                margin: 10px;
            }
            button:hover {
                background-color: #1b5e20;
            }
            img {
                width: 300px;
                border-radius: 15px;
                margin-top: 20px;
            }
        </style>
    </head>

    <body>
        <div class="container">
            <h1>🌾 Smart Agriculture Information Portal</h1>
            <p>Helping farmers with modern agriculture knowledge</p>

            <img src="https://images.unsplash.com/photo-1501004318641-b39e6451bec6" />

            <br><br>

            <form action="/info">
                <button>➡ Go to Agriculture Info Page</button>
            </form>

            <a href="https://www.india.gov.in/topics/agriculture" target="_blank">
                <button>🌱 Government Agriculture Resources</button>
            </a>
        </div>
    </body>
    </html>
    """

# ---------------------------------
# PAGE 2 : INFORMATION PAGE
# ---------------------------------
@app.route("/info")
def info():
    return """
    <html>
    <head>
        <title>Agriculture Awareness</title>
        <style>
            body {
                font-family: Arial;
                background-color: #f1f8e9;
                color: #2e7d32;
                text-align: center;
            }
            .box {
                margin: 50px;
                padding: 30px;
                background-color: white;
                border-radius: 15px;
                box-shadow: 0px 0px 10px gray;
            }
            img {
                width: 280px;
                border-radius: 10px;
            }
            button {
                padding: 12px 20px;
                font-size: 16px;
                background-color: #388e3c;
                color: white;
                border: none;
                border-radius: 6px;
                cursor: pointer;
            }
        </style>
    </head>

    <body>
        <div class="box">
            <h2>🌿 Importance of Smart Agriculture</h2>

            <img src="https://images.unsplash.com/photo-1592982537447-6c4f84a59e07" />

            <p>
                Smart agriculture uses technology to improve crop productivity,
                reduce water usage, and increase farmer income.
            </p>

            <p>
                Benefits include:
                <br>✔ Water conservation
                <br>✔ Crop yield improvement
                <br>✔ Weather-based farming
            </p>

            <a href="https://agricoop.nic.in/" target="_blank">
                <button>📘 Ministry of Agriculture (India)</button>
            </a>

            <br><br>

            <a href="/">
                <button>⬅ Back to Home</button>
            </a>
        </div>
    </body>
    </html>
    """

# ---------------------------------
# MAIN
# ---------------------------------
if _name_ == "_main_":
    app.run(port=5000, debug=True)