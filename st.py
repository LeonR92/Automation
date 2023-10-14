import streamlit as st
import pandas as pd
import glob
import time
import smtplib
from email.message import EmailMessage


def send_email(subject, body):
    # Set up email details
    EMAIL_ADDRESS = 'devopsgod99@gmail.com'
    EMAIL_PASSWORD = 'password'
    SMTP_SERVER = 'smtp-mail.outlook.com'
    SMTP_PORT = 587

    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = 'leonjy92@gmail.com'

    # Send the email
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
        smtp.starttls()
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)


# Get a list of all CSV files in the current directory
csv_files = glob.glob("*.csv")

# Read each CSV file into a DataFrame and append it to a list
dfs = [pd.read_csv(file) for file in csv_files]

# Concatenate all DataFrames in the list
df = pd.concat(dfs, ignore_index=True)

# Filter and display the metric
df_value = df.query("name == 'Alice'").size
st.metric("alarm", value=df_value)

# If the metric exceeds 40, send an email
if df_value > 82:
    send_email('AUFPASSEN MANN!!!!',
               f'The alarm metric for Alice has exceeded the threshold with a value of {df_value}.')

# Add a message about the refresh rate
st.write("This Streamlit app will refresh every minute.")

# Wait for 1 minute
time.sleep(60)

# Rerun the app after the delay
st.experimental_rerun()
