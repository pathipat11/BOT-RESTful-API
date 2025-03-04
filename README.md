# BOT-RESTful-API

## About
This is a RESTful API designed for use with the **Line-Chatbot** project. It provides predictions for employee status using an ensemble machine learning model. The API receives user input from the chatbot and returns a prediction of whether an employee will stay or leave based on certain features.

## Features
- Receives JSON input with employee attributes
- Uses a pre-trained ensemble machine learning model to predict employee status
- Returns a prediction result in JSON format
- Deployed on Render for public access

## Deployment
This API is hosted on Render along with the **Line-Chatbot** project. Both services must be deployed together for full functionality.

### Project Dependencies
Ensure you have the following dependencies installed:

```
flask
flask-cors
gunicorn
numpy
pandas
joblib
scikit-learn==1.6.1
```

## API Endpoints

### 1. Home Route
- **URL:** `/`
- **Method:** `GET`
- **Response:**
  ```json
  {
    "message": "Welcome to the Employee Status Prediction API!"
  }
  ```

### 2. Prediction Route
- **URL:** `/predict`
- **Method:** `POST`
- **Request Body (JSON):**
  ```json
  {
    "age": 30,
    "length_of_service": 5,
    "salary": 30000,
    "gender": 0,
    "marital_status": 1
  }
  ```
- **Response (JSON):**
  ```json
  {
    "prediction": "ยังคงทำงานอยู่",
    "age": 30,
    "length_of_service": 5,
    "salary": 30000,
    "gender": 0,
    "marital_status": 1
  }
  ```

## How to Run Locally
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/BOT-RESTful-API.git
   ```
2. Navigate to the project directory:
   ```bash
   cd BOT-RESTful-API
   ```
3. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Mac/Linux
   venv\Scripts\activate     # On Windows
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Run the application:
   ```bash
   python app.py
   ```
6. The API should now be running on `http://127.0.0.1:5000/`

## Deployment on Render
To deploy this project on Render:
1. Push your code to a GitHub repository.
2. Go to [Render](https://render.com/).
3. Create a new **Web Service** and connect it to your repository.
4. Set the **Start Command** to:
   ```bash
   gunicorn app:app
   ```
5. Deploy the service and obtain the Render-hosted API URL.

## Related Projects
- **[Line-Chatbot](https://github.com/your-repo/Line-Chatbot)**: This API works together with the chatbot to provide predictions.
- **[Python-Web-Application-Ensemble_Techniques](https://github.com/your-repo/Python-Web-Application-Ensemble_techniques)**: The original model training project.

## License
This project is licensed under the MIT License.

## 📞 Contact
**Author:** pathipat.mattra@gmail.com & pathipat.m@kkumail.com