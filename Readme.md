# Flask App Readme

## Introduction
This is a Flask web application. The project uses `venv` for managing dependencies.

## Setup

### Prerequisites
- Python 3.x
- `venv` module

### Installation

1. Clone the repository:
    ```sh
    git clone <repository_url>
    cd <repository_folder>
    ```

2. Create a virtual environment:
    ```sh
    python -m venv venv
    ```

3. Activate the virtual environment:

    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source venv/bin/activate
        ```

4. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Running the App

1. Ensure the virtual environment is activated.
2. Run the Flask app:
    ```sh
    flask run
    ```

## Project Structure
```
/project_folder
│   app.py
│   requirements.txt
│   README.md
│
└───venv
└───templates
└───static
```

## Contributing
Feel free to submit issues and enhancement requests.

## License
This project is licensed under the MIT License.
