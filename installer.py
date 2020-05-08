import os

def menu():
	print('''
╔══╗──╔╗╔╗
║╔╗╠═╦╣║╠╬═╦╦╦╦╦╗
║╠╣║║║║╚╣║║║║║╠║╣
╚╝╚╩╩═╩═╩╩╩═╩═╩╩╝

╔══╗
╚╗╔╩╦╦╦══╦╦╦╦╗
─║║╩╣╔╣║║║║╠║╣
─╚╩═╩╝╚╩╩╩═╩╩╝

[1] Ubuntu
[2] Debian
[3] Kali
[4] Kali Nethunter
[5] BlackBox
[6] Fedora
[7] CentOS
[8] OpenSUSE Leap
[9] OpenSUSE Tumbleweed
[10] Black Arch

[0] VNC
\n
''')

menu()

number = input("Введите номер дистрибутива : ")
if number == '1':
	os.system("pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Ubuntu/ubuntu.sh && bash ubuntu.sh")
elif number == '2':
	os.system("pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Debian/debian.sh && bash debian.sh")
elif number == '3':
	os.system("pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Kali/kali.sh && bash kali.sh")
elif number == '4':
	os.system("pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Nethunter/nethunter.sh && bash nethunter.sh")
elif number == '5':
	os.system("pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/BackBox/backbox.sh && bash backbox.sh")
elif number == '6':
	os.system("pkg install wget openssl-tool proot tar -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Fedora/fedora.sh && bash fedora.sh")
elif number == '7':
	os.system("pkg install wget openssl-tool proot tar -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/CentOS/centos.sh && bash centos.sh")
elif number == '8':
	os.system("pkg install wget openssl-tool proot tar -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/CentOS/centos.sh && bash centos.sh")
elif number == '9':
	os.system("pkg install wget openssl-tool proot tar -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/openSUSE/Tumbleweed/opensuse-tumbleweed.sh && bash opensuse-tumbleweed.sh")
elif number == '10':
	os.system("pacman-key --init && pacman-key --populate archlinuxarm && pacman -Sy --noconfirm curl && curl -O https://blackarch.org/strap.sh && chmod +x strap.sh && ./strap.sh")
else:
	print("Проблемка! ")
