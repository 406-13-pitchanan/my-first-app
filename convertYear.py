import streamlit as st

st.title("แอปพลิเคชันแปลง พ.ศ. เป็น ค.ศ.")

bh_year = st.number_input("กรอกปี พ.ศ.", value=2569)

ce_year = bh_year - 543

st.write(f"ปี ค.ศ. คือ {ce_year}")
