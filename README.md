Mathematical Operations Web Server


The Mathematical Operations Web Server is a Flask-based web application that allows users to perform mathematical calculations by sending mathematical expressions as part of the URL. It also maintains a history of the past 20 operations and their results.

Features

-Perform basic arithmetic operations like addition, subtraction, multiplication, and division.

-Calculate the power of a number, compute the square root, and find factorials.

-Flexible URL format for easy input of mathematical expressions.

-View the history of the last 20 operations by entering /history in the URL.

-Persistent history: The history of operations is saved to a JSON file and can be accessed even after restarting the server.

-Output formatting: Responses are provided in structured JSON format, including operator symbols.

-Designed to be user-friendly and convenient for quick calculations.



Getting Started

-Prerequisites: You need Python and Flask installed on your system to run this application.

-Clone the Repository: git clone https://github.com/yourusername/math-operations-web-server.git

-Install Dependencies: pip install Flask

-Run the Server: Navigate to the project directory and run python app.py. The server will start on http://127.0.0.1:5000/.\


Usage

-Open a web browser and navigate to http://127.0.0.1:5000/.

-To perform a calculation, input the desired mathematical expression in the URL. For example, /2/plus/3 will calculate "2 + 3".

-To view the history of past operations, enter /history in the URL.

-The server will respond with the result of the calculation in a JSON format.







