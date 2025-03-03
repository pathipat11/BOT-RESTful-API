from flask import Flask, request, jsonify
import pandas as pd
import joblib

app = Flask(__name__)

# โหลดโมเดลที่บันทึกไว้
model = joblib.load('./model/Ensemble_Model.pkl')

# Route หลัก (Home Route)
@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Employee Status Prediction API!"})

# Route สำหรับการทำนายผล
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # รับข้อมูลจาก JSON
        data = request.get_json()

        # รับค่าจากข้อมูล JSON
        age = int(data['age'])
        length_of_service = int(data['length_of_service'])
        gender = int(data['gender'])  # 0: Male, 1: Female
        marital_status = int(data['marital_status'])  # 0: Single, 1: Married
        salary = float(data['salary'])

        # สร้าง DataFrame สำหรับข้อมูลที่กรอก
        input_data = pd.DataFrame([[age, length_of_service, salary, gender, marital_status]],
                                  columns=['Age', 'Length_of_Service', 'Salary', 'Gender', 'Marital_Status'])

        # ทำนายผลลัพธ์
        prediction = model.predict(input_data)[0]

        # ส่งผลลัพธ์เป็น JSON
        result = 'Still Employed' if prediction == 1 else 'Resigned'
        return jsonify({
            "prediction": result,
            "age": age,
            "length_of_service": length_of_service,
            "salary": salary,
            "gender": gender,
            "marital_status": marital_status
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
