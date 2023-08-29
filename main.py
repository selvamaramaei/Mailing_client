from datetime import date
import pandas as pd
from sending_email import send_email


URL = "C:\\Users\\90534\\Documents\\Python-projeleri\\Sending-email\\email_data_.xlsx"


# reading excel file
def load_df(url):
    df = pd.read_excel(url)
    return df
 

def query_data_and_send_emails(df):
    email_counter = 0
    for _, row in df.iterrows():
        if pd.notnull(row["E-mail"]) and isinstance(row["E-mail"],str) :
            send_email(
                subject="Her İşletmeye Özel MYFİ İnternet",
                receiver_email=row["E-mail"],
                company=row["Firma-ünvanı"]
            )
            email_counter += 1 
    return f"total email sent : {email_counter}"    
    


df = load_df(URL)
result = query_data_and_send_emails(df)
print(result)

