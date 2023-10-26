# 🌟 QRATOR - QR Generator 🌟

## Description

QRATOR is a Flask application that generates QR codes. It allows users to convert URLs into QR codes by customizing various parameters such as background color, center color, and edge color. The generated QR codes can be downloaded as PNG files. 💻🎨📲

## Installation

To run this application, ensure you have the following prerequisites installed:

- Python (version 3.x.x) 🐍

1. Clone the repository:

   ```
   git clone <repository_url>
   ```

2. Navigate to the project directory:

   ```
   cd QRATOR
   ```

3. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

## Usage

Follow the steps below to set up and run the QRATOR application:

1. Start the application:

   ```
   python app.py
   ```

   The QRATOR application will be accessible at `http://localhost:5000/`. 🚀

## Project Structure

The project contains the following structure:

- `static/`: Folder containing static assets such as CSS, JavaScript, and images.
- `templates/`: Folder containing HTML templates for the web pages.
- `app.py`: Main Flask application file.
- `requirements.txt`: File specifying the required dependencies for the project.

## API Endpoints

The QRATOR application provides the following API endpoints:

- `GET /`: Home page of the application. 🏠
- `GET /convert?`, parameters:
  - `url_for_qr`: The URL that will be converted to a QR code. 🔗
  - `bg-color`: The background color of the QR code (options: white, black, blue, red, purple). 🎨
  - `center-color`: The center color of the QR code (options: white, black, blue, red, purple). 🌈
  - `edge-color`: The edge color of the QR code (options: white, black, blue, red, purple). ⚙️

## How to Generate QR Codes

1. Access the home page of the application at `http://localhost:5000/`.
2. Enter the URL that you want to convert into a QR code. 🌐
3. Select the desired background color, center color, and edge color for the QR code. 🎨
4. Click the "Convert" button. 🔄
5. The QR code will be generated and displayed on the page. 📷
6. To download the QR code as a PNG file, click the "Download" button. 💾

## Contributing

If you'd like to contribute to this project, please fork the repository, make your changes, and create a pull request. We welcome any improvements or bug fixes you may have. Your contributions are greatly appreciated! 🤝

## Authors

- [Saksham Tolani](https://github.com/SakshamTolani) 🙋‍♂️

## License

This project is licensed under the [MIT License](LICENSE). 📝

## Acknowledgements

- [Flask](https://flask.palletsprojects.com) 🌐
- [qrcode](https://github.com/lincolnloop/python-qrcode) 🧪
