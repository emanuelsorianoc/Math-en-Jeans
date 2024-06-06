import streamlit as st
from streamlit.elements.widgets.slider import Step
l = st.number_input("Valor do Lado:")
n = st.number_input("Valor do Passo n:", step=1)
i = 1
r1 = 0.4444

if n != 1:
  while n != i:
    i = n + 1
    r1 = r1 * 0.4444

a = l * l * 1.732 / 4

r3 = r1 - 1
r2 =  0.333 * a
r = r2 * r3 / -0.555
r = a + r

if st.button("Calcular"):
  st.write("Resultado", r)
