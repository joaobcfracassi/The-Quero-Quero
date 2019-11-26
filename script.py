#!/usr/bin/python
#-*-coding:utf-8-*-

print('******************************************************')
print('* QUERO-QUERO WEBMAIL AND WEB FILTER                 *')
print('*                                                    *')
print('*                                                    *')
print('* Front-End Interface for The Harvester              *')
print('* Ver. 1.0                                           *')
print('* Coded by João Fracassi                             *')
print('* joaobcfracassi@gmail.com                           *')
print('******************************************************')
print('')

import os
import commands
import time

domain_target = None
result_number = None
data_source = None
file_result = None

#Function scan target:
def scan_target():
    op = raw_input("Save result in output file?[S/N]. Enter any key to exit. ")
    
    if op == 'N' or op == 'n':
        domain_target = raw_input("Enter target domain: ")
        result_number = raw_input("Enter limit the number of results: ")
        data_source = raw_input("Enter data source search: ")
        exec_comandos = commands.getoutput('theharvester -d '+domain_target+' -l '+result_number+' -b '+data_source)
        print(exec_comandos)
    elif op == 'S' or op == 's':
        domain_target = raw_input("Enter target domain: ")
        result_number = raw_input("Enter limit the number of results: ")
        data_source = raw_input("Enter data source search: Others data source:[bing|baidu|linkedin|hunter|twitter|virustotal|yahoo|all]")
        file_result = raw_input("File Name: ")
        exec_comandos = commands.getoutput('theharvester -d '+domain_target+' -l '+result_number+' -b '+data_source+' -f '+file_result)
    else:
        print('Error! Invalid Option.')
        op = raw_input('Continue?[S]. Or any key to exit?')
        if op != 'S' or op != 's':
            os.system('clear')
            print('Leaving the program.')
            time.sleep(10)
            exit()
        else:
            scan_target()

#Call function:
if __name__ == '__main__':
    scan_target()   






