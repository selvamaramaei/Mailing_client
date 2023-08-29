import os
import smtplib
from email.message import EmailMessage
from email.utils import formataddr
from pathlib import Path
from dotenv import load_dotenv


PORT = 587
EMAİL_SERVER = 'mail.myfi.com.tr'


# load the environment variables
Current_dir = Path(__file__).resolve().parent if "__file__" in locals() else Path.cwd()
envars = Current_dir / ".env"
load_dotenv(envars)


# read enviroment variables 
sender_email = os.getenv("EMAİL")
password_email = os.getenv("PASSWORD")




def send_email(subject,receiver_email , company):
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = formataddr(("MYFİ" , f"{sender_email}"))
    msg["To"] = receiver_email
    msg["BCC"] = sender_email

    # plain text version 
    msg.set_content(
        f"""\
                Sayın {company}

        Kurumsal ihtiyaçlara özel teknoloji çözümleriyle , işinizin internet bağlantısı artık kesintisiz ve hızlı 

        Myfi sizlerle...

        Firmaların teknolojik altyapı ihtiyaçlarına çözüm sunuyor ve müşterilerine kesintisiz bir deneyim sunuyor.

        Tüm kurumsal işletmelerin metro Ethernet, fiber , Airfiber , P2P çözümleri ile yüksek hızlı veri transferi ve güvenli internet bağlantısı ihtiyaçlarını karşılıyoruz.
 
        """
    )

    # adding the html version 
    msg.add_alternative(
    f""" \
<html>
  <head>
    <style>
      body {{
          font-family: Arial, sans-serif;
          font-size: 20px;
          background-color: #f0f0f0; 
          margin: 0; 
          padding: 25px;
      }}
      .email-container {{
          max-width: 600px; 
          margin: 0 auto; 
          background-color: #ffffff; 
          padding: 25px;
      }}
      .image-container {{
          text-align: center; 
      }}
      img {{           
          max-width: 100%;
      }}
    </style>
  </head>
  <body>
    <div class="email-container">
      <p><strong>Sayın {company}</strong></p>
      <p>Kurumsal ihtiyaçlara özel teknoloji çözümleriyle, işinizin internet bağlantısı artık kesintisiz ve hızlı<br>
      Myfi sizlerle...</p>

      <p>Firmaların teknolojik altyapı ihtiyaçlarına çözüm sunuyor ve müşterilerine kesintisiz bir deneyim sunuyor.<br>
      Tüm kurumsal işletmelerin metro Ethernet, fiber, Airfiber, P2P çözümleri ile yüksek hızlı veri transferi ve güvenli internet bağlantısı ihtiyaçlarını karşılıyoruz.</p>
        
      <div class="image-container">
        <a href="https://myfi.com.tr">
          <img src="https://iili.io/HyzZnON.md.jpg" alt="HyzZnON.md.jpg" border="0">
        </a>
      </div>
    </div>
  </body>
</html>
    """,
    subtype="html",
)
    with smtplib.SMTP(EMAİL_SERVER , PORT) as server :
        server.starttls()
        server.login(sender_email , password_email)
        server.sendmail(sender_email , receiver_email , msg.as_string())
