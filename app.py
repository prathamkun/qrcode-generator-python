import streamlit as st
import qrcode
from io import BytesIO

st.title("UPI QR Code Generator")

upi_id = st.text_input("Enter your UPI ID")

if st.button("Generate QR"):
    if upi_id:
        upi_url = f"upi://pay?pa={upi_id}&pn=Recipient"
        qr = qrcode.make(upi_url)

        buffer = BytesIO()
        qr.save(buffer, format="PNG")

        st.image(buffer.getvalue(), caption="Scan to Pay")
        st.download_button(
            "Download QR Code",
            buffer.getvalue(),
            file_name="upi_qr.png",
            mime="image/png"
        )
    else:
        st.warning("Please enter a UPI ID")
