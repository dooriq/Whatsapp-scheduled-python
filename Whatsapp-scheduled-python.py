#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1

@author: dooriq
"""

import pywhatkit
import sys

#for number
number = "+62" + input("enter the number : +62")
if len(number) > 16 or len(number) < 10:
    print("Error! Check your phone number")
    sys.exit()

#for time
try:
    hour,minute = input("enter the time (HH:MM) :").split(":")     
except:
    print("Error! Time format is HH:MM ")
    sys.exit()
    
#for message
message = input("input the message : ")


try:
    pywhatkit.sendwhatmsg(number,message,int(hour), int(minute))
except:
    print("Try again and Check your input!")

class Menu:    
    menu = {}
    menu['1'] = "Tambahkan Mahasiswa"
    menu['2'] = "Tambahkan Nilai"
    menu['3'] = "Cek IPK Mahasiswa"
    menu['4'] = "Ganti Nama Mahasiswa"
    menu['9'] = "Informasi Detail"
    menu['0'] = "Keluar"
    
    def menu_utama():    
        while True:
            options = Menu.menu.keys()
            print('''
                  ======= IPK CALCULATOR MAIN MENU =======
                  ''')
                  
            for pil in options:
                print(pil,"-", Menu.menu[pil])
            select = input("Pilih Menu :")
            Menu.clear_console()
            
            if select == '1':
                print('''
                      Menambahkan Mahasiswa
                      ''')
                      
                input_npm = input("Masukan NPM Mahasiswa :")
                input_nama = input("Masukan Nama Mahasiswa :").upper()
                Menu.clear_console()
                
                if len(input_npm) != 10:
                    print("NPM Berisikan Angka 10 Digit")
                    Menu.menu_utama()
                
                if input_npm not in Main.mahasiswa.keys():
                    Main.mahasiswa[input_npm] = {'nama': input_nama, 'ipk':0 ,
                                            'total_nilai':0, 'total_sks':0,
                                            'total_matkul':0, 'ipk' :0}
                else:
                    print("NPM Anda Telah Terdafar")
                    Menu.menu_utama()
                
        
            elif select == '2':
                print('''
                      Menambahkan Nilai Mahasiswa
                      ''')
                ask_npm = input("Masukan NPM mahasiswa :")
                
                Mahasiswa.cek_npm(ask_npm)
        
                while True:
                    ask_nilai = float(input("Masukan Nilai Mahasiswa :"))
                    ask_sks = int(input("Masukan SKS Mahasiswa :"))
                    
                    Mahasiswa.input_nilai(ask_npm, ask_nilai, ask_sks)
                    
                    lanjut = input("Apakah masih ingin masukan nilai lain? (Y/N) ").upper()
                    if lanjut == "N":
                        Menu.return_menu()
                        break
                
                    
            elif select == '3':
                print('''
                      Menambahkan Mahasiswa
                      ''')
                ask_npm = input("Masukan NPM mahasiswa :")
                Mahasiswa.cek_npm(ask_npm)
                Mahasiswa.cek_ipk(ask_npm)
                
            elif select == '9':
                print('''
                      Menambahkan Mahasiswa
                      ''')
                ask_npm = input("Masukan NPM mahasiswa :")
                Mahasiswa.cek_npm(ask_npm)
                Mahasiswa.informasi_mahasiswa(ask_npm)
                Menu.return_menu()
                   
            elif select == '0': 
                print('''
                              TERIMA KASIH ^.^
                      ''')
                time.sleep(4)
                Menu.clear_console()
                break
            
            
            else: 
                print("Menu Tidak Tersedia!")
                Menu.return_menu()
                
    def clear_console():
        os.system("clear")
        
    def count_down(t = 3):
        while t: 
            mins, secs = divmod(t, 60) 
            timer = '{:02d}:{:02d}'.format(mins, secs) 
            print(timer, end="\r") 
            Menu.clear_console()
            time.sleep(1) 
            t -= 1
            
    def return_menu():
        print("Kembali ke Menu Utama dalam 3 Detik")
        time.sleep(4)
        Menu.clear_console()
        Menu.menu_utama()