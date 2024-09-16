import smtplib
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def emailApproval(
    docNO,
    docDate,
    status,
    company,
    creator,
    requester,
    totalAmount,
    ):
    if (requester == '') or (requester == None):
        requester = creator
        
    body = '''<!DOCTYPE html>
                  <html>
                  <head>
                    <meta http-equiv='content-type' content='text/html; charset=utf-8'>
                  <title>Page Title</title>
                  </head>
                  <body style='margin: 0px;'>

                    <table class='body-wrap' style='font-family: Helvetica Neue,Helvetica,Arial,sans-serif; box-sizing: border-box; font-size: 14px; width: 100%; background-color: #f6f6f6; margin: 0;padding:120px;' bgcolor='#f6f6f6'>
                      <tr style='font-family: Helvetica Neue,Helvetica,Arial,sans-serif; box-sizing: border-box; font-size: 14px; margin: 0;'>

                      <td class='container' width='600' style='font-family: Helvetica Neue,Helvetica,Arial,sans-serif; box-sizing: border-box; font-size: 14px;vertical-align: top; display: block !important; max-width: 600px !important; clear: both !important; margin: 0 auto;' valign='top'>
                      <div class='content' style='font-family: Helvetica Neue,Helvetica,Arial,sans-serif; box-sizing: border-box; font-size: 14px; max-width: 600px; display: block; margin: 0 auto; padding: 20px;'>
                      <table class='main' width='100%' cellpadding='0' cellspacing='0' itemprop='action' itemscope itemtype='http://schema.org/ConfirmAction' style='font-family: Helvetica Neue,Helvetica,Arial,sans-serif; box-sizing: border-box; font-size: 14px; border-radius: 3px; margin: 0; border: none;'>

                      <tr style='font-family: Helvetica Neue,Helvetica,Arial,sans-serif; box-sizing: border-box; font-size: 14px; margin: 0;'>
                      <td class='content-wrap' style='font-family: Helvetica Neue,Helvetica,Arial,sans-serif; box-sizing: border-box; font-size: 14px; vertical-align: top; margin: 0;padding: 30px;border: 3px solid #EBC781;border-radius: 7px; background-color: #fff;' valign='top'>
                      <meta itemprop='name' content='Confirm Email' style='font-family: Helvetica Neue,Helvetica,Arial,sans-serif; box-sizing: border-box; font-size: 14px; margin: 0;'/>
                      <table width='100%' cellpadding='0' cellspacing='0' style='font-family: Helvetica Neue,Helvetica,Arial,sans-serif; box-sizing: border-box; font-size: 14px; margin: 0;'>
                      <tr>
                      <td style='vertical-align: top; padding-bottom:30px;' align='center'><img srcset='https://www.dtgo.com/images/logo-dtgo.png,
                        https://www.dtgo.com/images/logo-dtgo@2x.png 2x' src='https://www.dtgo.com/images/logo-dtgo.png'></td>
                      </tr>
                      </td>
                      </tr>
                      <tr style='font-family: Helvetica Neue,Helvetica,Arial,sans-serif; box-sizing: border-box; font-size: 14px; margin: 0;'>
                      <td class='content-block' style='font-family: Helvetica Neue,Helvetica,Arial,sans-serif; box-sizing: border-box; font-size: 14px; vertical-align: top; margin: 0; padding: 0 0 20px;'valign='top'>
                        <p> Request for Entertainment Registration  ${docNO} ${status}.</p>

                          <p><b>Request Form Type :</b> Entertainment Registration</p>
                          <p><b>Document Number :</b> ${docNO}</p>
                          <p><b>Document Date :</b> ${docDate}</p>
                          <p><b>Status :</b> ${status}</p>
                          <p><b>Company :</b> ${company}</p>
                          <p><b>Requester :</b> ${requester}</p>
                          <p><b>Creater :</b> ${creator}</p>
                          <p><b>Total Amount :</b> ${totalAmount}</p>

                          <p>Please click here to open this document.</p>
                          <p>This email was sent to you for your reference.</p>
                          <p><a href="https://entertainment-registration.dtgo.com/#/" target="_blank" rel="noopener"><u>Please click here to open this document.</u></a></p>
                          <div style="border: none; border-bottom: solid #E5E5E5 1.0pt; mso-border-bottom-alt: solid #E5E5E5 .75pt; padding: 0cm 0cm 8.0pt 0cm;">&nbsp;</div>
                          <p>Best Regards,<br>Entertainment Registration System</p>
                          <p class="quiet">This is an automated notification. Do not reply.</p>

                      </td>
                      </tr>

                      </table>
                      </td>
                      </tr>
                      </table>

                      </div>

                      </tr>
                    </table>

                  </body>
                  </html>'''
                  
    body = body.replace('${docNO}', str(docNO))
    body = body.replace('${docDate}', str(docDate))
    body = body.replace('${status}', str(status))
    body = body.replace('${company}', str(company))
    body = body.replace('${creator}', str(creator))
    body = body.replace('${requester}', str(requester))
    body = body.replace('${totalAmount}', str(totalAmount))
    
    
    return body