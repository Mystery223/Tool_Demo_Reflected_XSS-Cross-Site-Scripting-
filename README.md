# Tool Demo: Reflected XSS (Cross-Site Scripting)

## Description
This project demonstrates a simple web application vulnerable to Reflected Cross-Site Scripting (XSS). It is intended for educational purposes to understand how XSS vulnerabilities work and how to mitigate them.

## Project Structure
```
app.py                # Main application file
static/
    css/
        style.css     # Stylesheet for the application
templates/
    index.html        # HTML template for the application
```

## Features
- Demonstrates a Reflected XSS vulnerability.
- Simple web interface to test and understand XSS attacks.

## Requirements
- Python 3.8 or higher
- Flask

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd Tool_Demo_Reflected_XSS(Cross-Site Scripting)
   ```
3. Install the required dependencies:
   ```bash
   pip install flask
   ```

## Usage
1. Run the application:
   ```bash
   python app.py
   ```
2. Open your web browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```
3. Test the application and observe the behavior of Reflected XSS.

## Disclaimer
This project is for educational purposes only. Do not use this code in production environments. Always follow ethical guidelines and obtain proper authorization before testing for vulnerabilities.

## License
This project is licensed under the MIT License. See the LICENSE file for details.