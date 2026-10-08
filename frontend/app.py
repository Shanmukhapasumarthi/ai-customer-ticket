import requests
import streamlit as st


API_URL = "http://backend:8000"


st.set_page_config(
    page_title="AI Support Ticket",
    page_icon="🎫",
    layout="centered",
)


st.title("AI Support Ticket System")
st.write("Submit your issue and our system will classify your ticket.")


customer_name = st.text_input(
    "Name",
    placeholder="Enter your name",
)

customer_email = st.text_input(
    "Email",
    placeholder="Enter your email",
)

message = st.text_area(
    "Describe your issue",
    placeholder="Tell us what happened...",
    height=150,
)


if st.button("Submit Ticket", type="primary"):

    if not customer_name or not customer_email or not message:
        st.warning("Please fill in all fields.")

    else:
        try:
            response = requests.post(
                f"{API_URL}/tickets",
                json={
                    "customer_name": customer_name,
                    "customer_email": customer_email,
                    "message": message,
                },
                timeout=10,
            )

            if response.status_code == 200:
                ticket = response.json()

                st.success("Ticket created successfully!")

                st.subheader("Ticket Details")

                st.write(
                    f"**Ticket ID:** {ticket['ticket_id']}"
                )

                st.write(
                    f"**Category:** {ticket['category']}"
                )

                st.write(
                    f"**Priority:** {ticket['priority']}"
                )

                st.write(
                    f"**Status:** {ticket['status']}"
                )

            else:
                st.error(
                    f"Failed to create ticket: {response.text}"
                )

        except requests.RequestException:
            st.error(
                "Could not connect to the support ticket API."
            )