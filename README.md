# Customized Email Sender for Business Solutions

### This Python project provides a customizable email sending solution aimed at businesses looking to improve their internet connectivity with specialized technology solutions. The project utilizes the smtplib library to send personalized emails to recipients, offering information about MYFİ's tailored technology services. The emails are sent both in plain text and HTML format to ensure maximum readability and engagement.

## Features
### Dynamic Content: The email content is dynamically generated based on the recipient's company name, providing a personalized touch for each email.

### HTML Presentation: The emails are sent with an HTML version that offers a visually appealing layout. This engages recipients with an embedded image and well-formatted text, enhancing the overall email experience.

### Easy Integration: The project's modular structure makes it easy to integrate into various applications or workflows, ensuring that businesses can seamlessly incorporate this email sending functionality.

## usage
### Environment Variables Setup: The project uses environment variables to securely store sender email and password. These can be set up in the .env file in the project directory.

### Excel Data Source: The project reads recipient information from an Excel file, such as email addresses and company names. The path to the Excel file should be specified in the URL variable.

### Personalized Emails: The script reads the Excel data, generates personalized emails for each recipient's company, and sends them using the provided sender email.

### Execution: Run the script using your preferred Python environment. The script will read the Excel data and send personalized emails to the recipients.

## Requirements
### Python 3.x
### smtplib library
### email library
### pathlib library
### dotenv library
### pandas library
