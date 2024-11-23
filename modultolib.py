import pandas as pd
import streamlit as st
import pickle


# Modelni yuklash
model_path = "xgb_model.pkl"  # Yuklangan fayl bilan bir xil joyda saqlang
try:
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
except FileNotFoundError:
    st.error(f"Model fayli topilmadi: {model_path}. Iltimos, faylni to'g'ri joylashtiring.")
    st.stop()
except Exception as e:
    st.error(f"Modelni yuklashda xato: {str(e)}")
    st.stop()

# Streamlit interfeysini bezash
st.set_page_config(page_title="Diabetes Bashorat Dasturi", page_icon="🩺", layout="centered")

# Foydalanuvchi interfeysini yaratish
st.title("Diabetes Bashorat Dasturi")

# Foydalanuvchi ma'lumotlarini kiritish
pregnancies = st.number_input("Homiladorlik soni", 0, 20)
glucose = st.number_input("Qon shakar darajasi (Glucose)", 0, 200)
blood_pressure = st.number_input("Qon bosimi (Blood Pressure)", 0, 120)
skin_thickness = st.number_input("Teridagi qalinlik (Skin Thickness)", 0, 100)
insulin = st.number_input("Insulin darajasi", 0, 800)
bmi = st.number_input("BMI", 0.0, 50.0)
diabetes_pedigree_function = st.number_input("Diabetes pediqree funktsiyasi", 0.0, 2.5)
age = st.number_input("Yosh", 0, 120)
# Natijani hisoblash
if st.button("Hisoblash"):
    input_data = [[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age]]
    prediction = model.predict(input_data)  # Model yordamida bashorat qiling
    st.success(f"Bashorat: {'Diabet' if prediction[0] == 1 else 'Diabet emas'}")


