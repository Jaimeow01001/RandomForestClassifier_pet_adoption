# Pet Adoption Likelihood Prediction API

API สำหรับทำนายโอกาสการรับเลี้ยงสัตว์ โดยใช้โมเดล RandomForestClassifier

## รายละเอียดโปรเจค
โปรเจคนี้เป็นระบบ API ที่ใช้ FastAPI สำหรับทำนายโอกาสการรับเลี้ยงสัตว์จากข้อมูลต่าง ๆ เช่น ประเภทสัตว์ สายพันธุ์ อายุ สี ขนาด น้ำหนัก สุขภาพ ระยะเวลาที่อยู่ในศูนย์รับเลี้ยง ค่าธรรมเนียม และเจ้าของเดิม โดยใช้โมเดลที่เทรนไว้แล้ว (RandomForestClassifier) และไฟล์ columns สำหรับจัดรูปแบบข้อมูล

## โครงสร้างไฟล์
- `main.py` : ไฟล์หลักสำหรับรัน FastAPI และกำหนด endpoint
- `best_model_Rb_nobinned.pkl` : ไฟล์โมเดลที่เทรนแล้ว
- `columns_Rb_nobinned.pkl` : ไฟล์ columns สำหรับจัดรูปแบบข้อมูล
- `pet_adoption_data.csv` : ข้อมูลสัตว์ที่ใช้เทรนโมเดล
- `ML_Project_65123481.ipynb` : Jupyter Notebook สำหรับการวิเคราะห์และเทรนโมเดล
- `mapping.pkl` : ไฟล์ mapping สำหรับข้อมูล

## วิธีการใช้งาน
1. ติดตั้ง dependencies ที่จำเป็น เช่น fastapi, uvicorn, joblib, pandas

```bash
pip install fastapi uvicorn joblib pandas
```

2. รัน API ด้วยคำสั่ง

```bash
uvicorn main:app --host 127.0.0.1 --port 5016 --reload
```

3. เข้าใช้งาน API ได้ที่
- `GET /` : ตรวจสอบสถานะ API
- `POST /prediction` : ส่งข้อมูลสัตว์เพื่อทำนายโอกาสการรับเลี้ยง

### ตัวอย่างการเรียกใช้งาน
ส่งข้อมูลผ่าน POST request ไปที่ `/prediction` พร้อมข้อมูล เช่น

```json
{
  "PetType": "Dog",
  "Breed": "Labrador",
  "AgeMonths": 12,
  "Color": "Black",
  "Size": "Large",
  "WeightKg": 20.5,
  "Vaccinated": 1,
  "HealthCondition": 0,
  "TimeInShelterDays": 30,
  "AdoptionFee": 500,
  "PreviousOwner": 0
}
```

API จะตอบกลับผลการทำนาย เช่น

```json
{
  "prediction": [1]
}
```

## ข้อมูลเพิ่มเติม
- โมเดลที่ใช้เป็น RandomForestClassifier
- สามารถปรับแต่งข้อมูล input ได้ตาม columns ที่กำหนด

## ผู้พัฒนา
- Jaimeow01001

---
**หมายเหตุ:** หากต้องการนำไป deploy หรือใช้งานจริง ควรตรวจสอบ dependencies และ security เพิ่มเติม
