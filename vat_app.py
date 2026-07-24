import streamlit as st
st.title("เเอปพลิเคชันคำนวณราคาสินค้ารวม VAT 7%")
price = st.number_input ("กรอกราคาสินค้า")
vat= price * 0.07
net_price = price + vat
st.divider()
st.write (" นางสาวพิชชานันทน์ วรรณก้อน เลขที่ 13 ม.4/6")
st.header ( f"๓าษีมูลค่าเพิ่ม ( VAT 7% ): {vat:2f} บาท")
st.header(f"• ราคาสุทธิ: {net_price:.2f} บาท")
