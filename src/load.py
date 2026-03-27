import joblib

def load():
    model = joblib.load('.\\models\\sentiment.pkl')

    predict = model.predict(["ไอ้บ้า"])
    print("ผลลัพธ์:", "หยาบ" if predict[0] == 1 else "ไม่หยาบ")