import sendgrid
from sendgrid.helpers.mail import *

def sendEmail(time):
    sg = sendgrid.SendGridAPIClient(apikey='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')
    from_email = Email('rajsherror404@gmail.com')
    to_email = Email('kirranreddy@gmail.com')
    subject = 'Travel Time'
    
    content = Content("text/plain", "Your travel time is " + time + " minutes. Less than usual traffic. ")
    
    mail = Mail(from_email,subject,to_email,content)
    
    response = sg.client.mail.send.post(request_body=mail.get())
    
    # print(response.status_code)
    # print(response.body)
    # print(response.headers)
    
    # return response

def main():
    a =1



if __name__ =='__main__':
    main()