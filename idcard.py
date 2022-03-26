import random
import datetime
import qrcode

from PIL import Image, ImageDraw, ImageFont
import os

image = Image.new('RGB', (1000, 900), (255, 255, 255))
draw = ImageDraw.Draw(image)

font = ImageFont.truetype('arial.ttf', size=45)

os.system("Title: ID CARD Generator with QR Code by Rohan Kasabe")

d_date = datetime.datetime.now()
reg_format_date = d_date.strftime(
    "  %d-%m-%Y\t\t\t\t\t ID CARD Generator\t\t\t\t\t  %I:%M:%S %p")
print(
    '+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print(reg_format_date)
print(
    '+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

# starting position of the message
(x, y) = (50, 50)
company = input('\nEnter Your Company Name: ')

color = 'rgb(0, 0, 0)'  # black color
font = ImageFont.truetype('arial.ttf', size=80)
draw.text((x, y), company, fill=color, font=font)

# adding an unique id number. You can manually take it from user
(x, y) = (600, 75)
idno = random.randint(10000000, 90000000)
message = str('ID: ' + str(idno))
color = 'rgb(0, 0, 0)'  # black color
font = ImageFont.truetype('arial.ttf', size=60)
draw.text((x, y), message, fill=color, font=font)

# For the Name
(x, y) = (50, 250)
name = input('Enter Your Full Name: ')

fname = str('Name: ' + str(name))
color = 'rgb(0, 0, 0)'  # black color
font = ImageFont.truetype('arial.ttf', size=45)
draw.text((x, y), fname, fill=color, font=font)

# For the gender
(x, y) = (50, 350)
gender = input('Enter Your Gender: ')
fgender = str('Gender: ' + str(gender))
color = 'rgb(0, 0, 0)'  # black color
draw.text((x, y), fgender, fill=color, font=font)

# For the Age
(x, y) = (400, 350)
age = int(input('Enter Your Age: '))
fage = str('Age: ' + str(age))
color = 'rgb(0, 0, 0)'  # black color
draw.text((x, y), fage, fill=color, font=font)

# For the DOB
(x, y) = (50, 450)
dob = input('Enter Your Date Of Birth: ')
fdob = str('Date of Birth: ' + str(dob))
color = 'rgb(0, 0, 0)'  # black color
draw.text((x, y), fdob, fill=color, font=font)

# For the Blood Group
(x, y) = (50, 550)
blood_group = input('Enter Your Blood Group: ')
flood_group = str('Blood Group: ' + str(blood_group))
color = 'rgb(255, 0, 0)'  # black color
draw.text((x, y), flood_group, fill=color, font=font)

# For the Mob No
(x, y) = (50, 650)
No = int(input('Enter Your Mobile Number: '))

fNo = str('Mobile Number: ' + str(No))
color = 'rgb(0, 0, 0)'  # black color
draw.text((x, y), fNo, fill=color, font=font)

# For the Address
(x, y) = (50, 750)
address = input('Enter Your Address: ')
faddress = str('Address: ' + str(address))
color = 'rgb(0, 0, 0)'  # black color
draw.text((x, y), faddress, fill=color, font=font)

# save the edited image

image.save(str(name) + '.png')

# this info. is added in QR code, also add other things
QR = qrcode.make(str(company) + '\n' + str(name)+'\n' + str(idno))
QR.save(str(idno) + '.bmp')

ID = Image.open(name + '.png')
QR = Image.open(str(idno) + '.bmp')  # 25x25
ID.paste(QR, (650, 350))
ID.save(name + '.png')

print(('\n\n\nYour ID Card Successfully created in a PNG file ' + name + '.png'))
