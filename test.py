import streamlit as st

col1, col2 = st.columns(2)

with col1:
    price_1 = st.text_input(label="ПЕРШИЙ", placeholder="Ціна першого продукту", key="price_1")
    weight_1 = st.text_input(label="", placeholder="Вага/об'єм першого продукту", key="weight_1")

with col2:
    price_2 = st.text_input(label="ДРУГИЙ", placeholder="Ціна другого продукту", key="price_2")
    weight_2 = st.text_input(label="", placeholder="Вага/об'єм другого продукту", key="weight_2")

# Перетворення введених значень в числа
price_1 = float(price_1.replace(',', '.')) if price_1 else None
weight_1 = float(weight_1.replace(',', '.')) if weight_1 else None
price_2 = float(price_2.replace(',', '.')) if price_2 else None
weight_2 = float(weight_2.replace(',', '.')) if price_2 else None

# Вирівнювання кнопки по центру
col1, col2, col3 = st.columns([1, 1, 3])
with col3:
    button_clicked = st.button("**Порівняти**")

if button_clicked:
    try:
        q1 = round((price_1 * 100) / weight_1, 2)
        q2 = round((price_2 * 100) / weight_2, 2)
        if q1 < q2:
            profit = round((q2 * weight_1 - price_1 * 100) / 100, 2)
            st.write(f"Краще взяти перший продукт, він вигідніше на {profit} грн")
        elif q1 > q2:
            profit = round((q1 * weight_2 - price_2 * 100) / 100, 2)
            st.write(f"Краще взяти другий продукт, він вигідніше на {profit} грн")
        else:
            st.write("Друже, ціна ідентична, бери що гарніше")
    except ValueError:
        st.write("Ого, ти примудрився натупити в такому простому застосунку xD")
