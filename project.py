# Using this we could send a email using python .
# This emailer was made by : S D Sriram ,A student Studying in 7th Grade 
# Hope you like this!!
# You don't have to import anything ...........
import smtplib

#All the input fields
input_of_email = str(input("Enter your email: ")) 
input_of_password = str(input("Enter yor password:  ")) 
input_of_recv_email = str(input("Enter the recv. email: "))
input_of_message = str(input("Enter the message that you want to send : "))
# Defining the variables and making it easy to read 
sender_email =(input_of_email)
rec_email = (input_of_recv_email)
password = (input_of_password)


server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()# Making a connection
server.login(sender_email,password)
print('Login was successful')
server.sendmail(sender_email , input_of_message) # After making a connection, send the mail to recv.
print ("Message has been sent "+ input_of_recv_email)
