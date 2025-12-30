from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="Smart Agriculture API", description="Predictive Irrigation System")

# -------------------------------
# PAGE 1 : HOME PAGE
# -------------------------------
@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
    <head>
        <title>Smart Agriculture</title>
    </head>
    <body style="text-align:center; font-family:Arial">

        <h1>🌾 Smart Agriculture – Predictive Irrigation</h1>
        <p>Click the button to launch the dashboard</p>

        <form action="/dashboard">
            <button style="padding:15px; font-size:18px;">
                🚀 Launch Dashboard
            </button>
        </form>

    </body>
    </html>
    """

# -------------------------------
# PAGE 2 : DASHBOARD PAGE
# -------------------------------
@app.get("/dashboard", response_class=HTMLResponse)
def dashboard():
    return """
    <html>
    <head>
        <title>Dashboard</title>
    </head>
    <body style="text-align:center; font-family:Arial">

        <h2>📊 Irrigation Prediction Dashboard</h2>

        <iframe
            src="https://your-streamlit-app.streamlit.app"
            width="100%"
            height="600"
            style="border:none;">
        </iframe>

        <br><br>
        <a href="/">
            <button style="padding:10px;">⬅ Back to Home</button>
        </a>

    </body>
    </html>
    """

# -------------------------------
# MAIN
# -------------------------------
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)