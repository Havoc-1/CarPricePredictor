# Car Price Predictor

This project is a web-based application for predicting car prices using machine learning techniques. It is built with Django and utilizes various libraries for data processing and model training.

## Project Structure

```
car_price_predictor
├── car_price_predictor
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── manage.py
├── requirements.txt
├── README.md
├── app
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   ├── urls.py
│   ├── templates
│   │   └── app
│   │       └── index.html
│   └── static
│       └── app
│           └── style.css
├── scripts
│   ├── ai_chat_analyst_script.py
└── .gitignore
```

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd car_price_predictor
   ```

2. **Create a virtual environment**:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```
   pip install -r requirements.txt
   ```

4. **Run migrations**:
   ```
   python manage.py migrate
   ```

5. **Run the development server**:
   ```
   python manage.py runserver
   ```

6. **Access the application**:
   Open your web browser and go to `http://127.0.0.1:8000/`.

## Usage

The application provides a user-friendly interface to input car details and predict the price based on the trained machine learning model. 

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for details.