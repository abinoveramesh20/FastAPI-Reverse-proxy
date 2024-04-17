from fastapi import FastAPI, Form, HTTPException
from fastapi.responses import HTMLResponse

app = FastAPI()

html_form = """
<!DOCTYPE html>
<html>
<head>
    <title>Voting Eligibility Checker</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .container {
            background-color: black;
            color: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        input[type="text"], input[type="number"], button {
            width: 100%;
            padding: 10px;
            margin: 5px 0;
            border: 1px solid #ccc;
            border-radius: 5px;
            box-sizing: border-box;
            font-size: 16px;
        }
        label {
            font-size: 18px;
        }
        button {
            background-color: #4CAF50;
            color: white;
            border: none;
            cursor: pointer;
        }
        button:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>Voting Eligibility Checker</h2>
        <form method="post">
            <label for="name">Enter your name:</label><br>
            <input type="text" id="name" name="name" required><br>
            <label for="age">Enter your age:</label><br>
            <input type="number" id="age" name="age" required><br>
            <button type="submit">Submit</button>
        </form>
        <div id="result" style="margin-top: 20px;"></div>
    </div>
    <script>
        const form = document.querySelector('form');
        form.addEventListener('submit', async (event) => {
            event.preventDefault();
            const formData = new FormData(form);
            const response = await fetch('/', {
                method: 'POST',
                body: formData
            });
            const result = await response.text();
            document.getElementById('result').innerHTML = result;
        });
    </script>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
async def get_age_form():
    return html_form

@app.post("/", response_class=HTMLResponse)
async def process_age(name: str = Form(...), age: int = Form(...)):
    if age >= 18:
        return f"<h3>Hello {name}!! You are eligible to vote!</h3>"
    else:
        return f"<h3>Sorry, {name}. You must be 18 or older to vote.</h3>"
