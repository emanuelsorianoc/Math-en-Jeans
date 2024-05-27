import streamlit as st
from streamlit.elements.widgets.slider import Step
l = st.number_input("Valor do Lado:")
n = st.number_input("Valor do Passo n:", step=1)
i = 1
r1 = 0.44444444444

if n != 1:
  while n != i:
    i = n + 1
    r1 = r1 * 0.44444444444

a = l * l * 1.73205080756887729362772 / 4

r3 = r1 - 1
r2 =  0.33333333333 * a
r = r2 * r3 / -0.55555555555
r = a + r

if st.button("Calcular"):
  st.write("Resultado", r)