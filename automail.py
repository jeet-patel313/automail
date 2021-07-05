import smtplib
import random
from email.message import EmailMessage

print("Password Generator by Jeet Patel (I_am_Dope)")
emailaddress = input("enter email address: ")
websitename = input("enter website name: ")

#variables for email sending
EmailAdd = "EMAIADDESS@gmail.com" #enter email here
Pass = "PASSWORD" #enter password here

#variables for password generator
char1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
char2 = char1.lower()
char3 = "@!#$&*"
char4 = "123456789"

def message():
	password = gopass()
	print("Your Password for", emailaddress, "on", websitename, "is" , password)
	Question = input("Are you satisfied with this password?(Y/N): ")
	if Question == ("Y"):
		data = ["\nwebsitename: ", websitename," email: ", emailaddress," password: ", password]
		#writing in file
		file = open("creds.txt", "a")
		file.writelines(data)
		file.close()
		print("[+]Your password has been saved")
			
		#sending email
		msg = EmailMessage()
		msg["Subject"] = "Password for "+websitename+" from automail"
		msg["From"] = EmailAdd
		msg["To"] = emailaddress
		msg.set_content("website: "+websitename+"\nemail: "+emailaddress+"\npassword: "+password)		
		with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
			smtp.login(EmailAdd, Pass)
			smtp.send_message(msg)
			smtp.quit()
		print("[+]An email of the credentials has been sent to you")	
	elif Question == ("N"):
		print("[-]Your password has been dumped")
		message()
	else:
		print("[!]Your password has not been saved (Enter Y or N)")

#function that generates 14 digit random password
def gopass():
	password = ""
	for _ in range(4):
		password += random.choice(char1)

	for _ in range(4):
		password += random.choice(char2)
	
	for _ in range(3):
		password += random.choice(char3)

	for _ in range(3):
		password += random.choice(char4)

	password_final = list(password)
	shuff = random.shuffle(password_final)
	passwd = "".join(password_final)
	return passwd
	
message()
