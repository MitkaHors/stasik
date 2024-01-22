import streamlit as st


st.markdown("<h1 style='text-align: center; font-family: Helvetica, sans-serif; font-weight: bold;'>Стасік</h1>",
            unsafe_allow_html=True)

col1, col2, col3 = st.columns([5, 2, 5])
with col2:
    image_path = "jew.png"
    st.image(image_path, width=100)

text = "Привіт, я Стасік!! Я допоможу вам обрати який з двох товарів вигідніше придбати!! Ми своїх не обманюємо!"
formatted_text = "<br>".join(text.split("! "))
styled_text = f"<div style='text-align: center; margin-bottom: 20px;'>{formatted_text}</div>"

st.markdown(styled_text, unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    price_1 = st.text_input(label="ПЕРШИЙ", placeholder="Ціна першого продукту", key="price_1")
    weight_1 = st.text_input(label="", placeholder="Вага/об'єм першого продукту", key="weight_1")

with col2:
    price_2 = st.text_input(label="ДРУГИЙ", placeholder="Ціна другого продукту", key="price_2")
    weight_2 = st.text_input(label="", placeholder="Вага/об'єм другого продукту", key="weight_2")

try:
    if price_1 and price_2 and weight_1 and weight_2:
        price_1 = float(price_1.replace(',', '.'))
        price_2 = float(price_2.replace(',', '.'))
        weight_1 = float(weight_1.replace(',', '.'))
        weight_2 = float(weight_2.replace(',', '.'))
    else:
        price_1 = None
        price_2 = None
        weight_1 = None
        weight_2 = None
except ValueError:
    st.write("Ого, ти примудрився натупити в такому простому застосунку. Молодець!")
# Обробка інших типів помилок
except Exception as e:
    st.write("{e}")


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
            st.write(f"Ой вей! Таки краще взяти перший продукт, він вигідніше на {profit} грн")
        elif q1 > q2:
            profit = round((q1 * weight_2 - price_2 * 100) / 100, 2)
            st.write(f"Так і шо ви думаєте, другий продукт вигідніше на {profit} грн")
        else:
            st.write("Друже, ціна ідентична! Мабуть це дилема Ескобара!")
    except TypeError:
        st.write()

st.markdown("<h4 style='text-align: center; font-family: Helvetica, sans-serif; font-size: 16px; font-weight: lighter; margin-top: 200px;'>Версія 1.0.1</h4>",
            unsafe_allow_html=True)


