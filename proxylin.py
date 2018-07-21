#! /usr/bin/python3

import os

def proxy_connect(proxy_addr,proxy_port):
    file = open(filename,"r")
    value = file.read()
    file.close()

    file = open(backup_environment,"w")
    file.write(value)
    file.close()


    file = open(filename,"r")
    clear_proxy = file.read()
    file.close()
    
    set_proxy=clear_proxy+'''\nhttp_proxy=http://'''	+	proxy_addr	+	''':'''	+	proxy_port	+	'''/
	\nhttps_proxy=http://'''	+	proxy_addr	+	''':'''	+	proxy_port	+	'''/
	\nftp_proxy=http://'''	+	proxy_addr	+	''':'''	+	proxy_port	+	'''/
	\nno_proxy="localhost,127.0.0.1,localaddress,.localdomain.com"
	\nHTTP_PROXY=http://'''	+	proxy_addr	+	''':'''	+	proxy_port	+	'''/
	\nHTTPS_PROXY='''	+	proxy_addr	+	''':'''	+	proxy_port	+	'''/
	\nFTP_PROXY='''	+	proxy_addr	+	''':'''	+	proxy_port	+	'''/
	\nNO_PROXY="localhost,127.0.0.1,localaddress,.localdomain.com"		''' + '''\nAcquire::http::proxy "''' + proxy_addr + ''':''' + proxy_port + '''";'''+'''\nAcquire::ftp::proxy "''' + proxy_addr + ''':''' + proxy_port + '''";'''+'''\nAcquire::https::proxy "''' + proxy_addr + ''':''' + proxy_port + '''";'''

    file = open(filename,"w")
    file.write(set_proxy)
    file.close()


def proxy_disconnect():
    print("Disconnecting Proxy")
    file = open(backup_environment,"r")
    value=file.read()
    file.close()

    file = open(filename , "w")
    file.write(value)
    file.close()
    


def custom_proxy():
    os.system("clear")
    logo()
    proxy_option = input(" Choose an Option \n\t 1) Connect Proxy \n \t 2) Disconnect Proxy\n Option :")
    if proxy_option == '1':
        print("Entered proxy connect\n")
        proxy_addr=input("\nEnter the proxy address     :")
        proxy_port=input("\nEnter the proxy port        :")
        proxy_connect(proxy_addr,proxy_port)
	
    elif proxy_option == '2':
        print("\nentered proxy disconnect\n")
        proxy_disconnect()
        
    else:
        print("\n\n\tinvalid option")
    
    reboot_option=input("\nA System Reboot is necessary to apply changes \n Do you Want to continue? \n 1) Reboot my Computer 2) Reboot later Manually")
    if reboot_option == '1':
        print("\nRebooting System")
        os.system("reboot")
    elif reboot_option == '2':
        print("\nCanceled Reboot. Reboot later for proper proxy setup")

    else:
        print("\n Invalid Option")



def logo():
    os.system("clear")
    print("\t\t\bProxyGuide\n")
    print("\t\bCreated By: Ivan Saji Abraham")


def main():
    
    os.system("clear")
    logo()
    home_option = input(" Choose an Option \n\t 1) Connect to Proxy \n \t 2) Exit\n")
    
    if home_option == '1':
        print("entered proxy\n")
        custom_proxy()


    elif home_option == '2':
	    print("exiting\n")
	    exit(0)


    else:
        print("\n\ninvalid option\n")


filename ='/etc/environment'
backup_environment='/etc/environment_backup.txt'
main()
