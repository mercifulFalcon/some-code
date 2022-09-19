print(" --------------------------------Unit converter-------------------------------- ")

while True:
    print()
    print("\nMain menu\n\n1:Angle\n2:Area\n3:Height\n4:Temperature\n0:Exit")
    try:
        op = int(input("\nPlease enter an option:\n>>> "))
        
        if op < 0 or op > 5:
                print("Invalid number, try again")
        
            
        elif op == 1:
                    x = float(input("\nNumber: "))
                    
                    print("\nConvert from:\n1:degree\n2:radian\n3:minutes\n4:seconds\n5:quadrant")
                    frm = int(input("\nPlease enter an option 1-5:\n>>> "))
                    if frm < 1 or frm > 5:
                        print("Wrong choice, back to the main menu you go")
                        continue
                    print("\nConvert to:\n1:degree\n2:radian\n3:minutes\n4:seconds\n5:quadrant")
                    to = int(input("\nPlease enter an option 1-5:\n>>> "))
                    if to < 1 or to > 5:
                        print("Wrong choice, back to the main menu you go")
                        continue
                    if to < 1:
                        print("Wrong choice, back to the main menu you go")
                    elif  to > 5:
                        print("Wrong choice, back to the main menu you go")
                    if frm == 1 and to == 1:
                        print(f"{x}°")
                    elif frm == 1 and to == 2:
                        print(f"{round(x / 57.3, 2)} rad")
                    elif frm == 1 and to == 3:
                        print(f"{x * 60}'")
                    elif frm == 1 and to == 4:
                        print(f'{x * 3600}"') 
                    elif frm == 1 and to == 5:
                        print(f"{round(x / 90, 2)} quadrant")
                    elif frm == 2 and to == 1:
                        print(f"{round(x * 57.3, 2)}°")
                    elif frm == 2 and to == 2:
                        print(f"{x} rad")
                    elif frm == 2 and to == 3:
                        print(f"{x * 3438}'")
                    elif frm == 2 and to == 4:
                        print(f"{x * 206300}")
                    elif frm == 2 and to == 5:
                        quad = x / 1.571
                        print(f"{round(x / 1.571 , 2)} quadrant")
                    elif frm == 3 and to == 1:
                        print(f"{round(x / 60, 2)}°" )
                    elif frm == 3 and to == 2:
                        print(f"{round(x / 3438, 2)} rad")
                    elif frm == 3 and to == 3:
                        print(f"{x}'")
                    elif frm == 3 and to == 4:
                        print(f'{x * 60}"')  
                    elif frm == 3 and to == 5:
                        print(f"{round(x / 5400, 2)} quadrant")
                    elif frm == 4 and to == 1:
                        print(f"{round(x / 3600, 2)}º")
                    elif frm == 4 and to == 2:
                        print(f"{x / 206300} rad")
                    elif frm == 4 and to == 3:
                        print(f"{round(x / 60, 2)}'")
                    elif frm == 4 and to == 4:
                        print(f'{x}"')        
                    elif frm == 4 and to == 5:
                        print(f"{x / 324000} quadrant")
                    elif frm == 5 and to == 1:
                        print(f"{x * 90}º")
                    elif frm == 5 and to == 2:
                        print(f"{round(x * 1.5708, 2)} rad") 
                    elif frm == 5 and to == 3:
                        print(f"{x * 5400}'")
                    elif frm == 5 and to == 4:
                        print(f'{x * 324000}"')
                    elif frm == 5 and to == 5:
                        print(f"{x} quadrant")
                        
        elif op == 2:
                    x = int(input("\nNumber: "))
                    
                    print("\nConvert from:\n1:square inch (in²)\n2:square foot (ft²)\n3:square yard (yd²)\n4:square mile (mi²)\n5:square milimiter (mm²)\n6:square centimeter (cm²)\n7:square meter (m²)\n8:square kilometer (km²)")
                    
                    frm = int(input("\nSelect an option:\n>>> ")) 
                    if frm < 1 or frm > 8:
                        print("Wrong choice, back to the main menu you go")
                        continue 
                    
                    print("\nConvert to:\n1-square inch (in²)\n2:square foot (ft²)\n3:square yard (yd²)\n4:square mile (mi²)\n5:square milimiter (mm²)\n6:square centimeter (cm²)\n7:square meter (m²)\n8:square kilometer (km²)")
                    to = int(input("\nSelect an option:\n>>> "))
                    
                    if to < 1 or to > 8:
                        print("Wrong choice, back to the main menu you go")
                        continue
                    if frm == 1 and to == 1:
                        print(f"{x} in²")
                    elif frm == 1 and to == 2:
                        print(f"{round(x / 144, 2)} ft\xb2" )
                    elif frm == 1 and to == 3:
                        print(f"{round(x /1296, 2)} yd\xb2")
                    elif frm == 1 and to == 4:
                        print(f"{x /4014000000} mi\xb2")
                    elif frm == 1 and to == 5:
                        print(f"{x * 645.2} mm\xb2")
                    elif frm == 1 and to == 6:
                        print(f"{x * 6.452} cm\xb2")
                    elif frm == 1 and to == 7:
                        met = x / 1550
                        print(f"{round(x /1550, 2)} m\xb2") 
                    elif frm == 1 and to == 8:
                        print(f"{x /1550000000} km\xb2 ")
                    elif frm == 2 and to == 1:
                        print(f"{x * 144} in\xb2")
                    elif frm == 2 and to == 2:
                        print(f"{x} in\xb2")
                    elif frm == 2 and to == 3:
                        print(f"{round(x / 9, 2)} yd\xb2")
                    elif frm == 2 and to == 4:
                        print(f"{x / 27880000} mi\xb2")
                    elif frm == 2 and to == 5:
                        print(f"{x * 92903.04} mm\xb2")
                    elif frm == 2 and to == 6:
                        print(f"{x * 929.0304} cm\xb2 ")
                    elif frm == 2 and to == 7:
                        print(f"{round(x / 10.76, 2)} m\xb2")
                    elif frm == 2 and to == 8:
                        print(f"{x / 10760000} km\xb2")
                    elif frm == 3 and to == 1:
                        print(f"{x * 1296} in\xb2")
                    elif frm == 3 and to == 2:
                        print(f"{x * 9} ft\xb2")
                    elif frm == 3 and to == 3:
                        print(f"{x} yd\xb2")
                    elif frm == 3 and to == 4:
                        print(f"{x / 3098000} mi\xb2 ")
                    elif frm == 3 and to == 5:
                        print(f"{x * 836100} mm\xb2")    
                    elif frm == 3 and to == 6:
                        print(f"{x * 8361} cm\xb2")
                    elif frm == 3 and to == 7:
                        print(f"{round(x / 1.196, 2)} m\xb2")
                    elif frm == 3 and to == 8:
                        print(f"{x / 1196000} km\xb2")
                    elif frm == 4 and to == 1:
                        print(f"{x * 4014000000} in\xb2")
                    elif frm == 4 and to == 2:
                        print(f"{x * 278800000} ft\xb2")
                    elif frm == 4 and to == 3:
                        print(f"{x * 3098000} yd\xb2")
                    elif frm == 4 and to == 4:
                        print(f"{x} mi\xb2")
                    elif frm == 4 and to == 5:
                        print(f"{x * 2590000000000} mm\xb2")
                    elif frm == 4 and to == 6:
                        print(f"{x * 25900000000} cm\xb2")
                    elif frm == 4 and to == 7:
                        print(f"{x * 2590000} m\xb2")
                    elif frm == 4 and to == 8:
                        print(f"{x * 2.59} km\xb2")
                    elif frm == 5 and to == 1:
                        print(f"{round(x / 645.2, 4)} in\xb2")
                    elif frm == 5 and to == 2:
                        print(f"{x / 92900} ft\xb2")
                    elif frm == 5 and to == 3:
                        print(f"{x /836100} yd\xb2")
                    elif frm == 5 and to == 4:
                        print(f"{x / 2590000000000} mi\xb2")
                    elif frm == 5 and to == 5:
                        print(f"{x} mm\xb2")
                    elif frm == 5 and to == 6:
                        print(f"{round(x / 100, 2)} cm\xb2")
                    elif frm == 5 and to == 7:
                        print(f"{x / 1000000} m\xb2")
                    elif frm == 5 and to == 8:
                        print(f"{x /1000000000000} km\xb2")
                    elif frm == 6 and to == 1:
                        print(f"{round(x / 6.452, 2)} in\xb2")
                    elif frm == 6 and to == 2:
                        print(f"{round(x / 929, 2)} ft\xb2")
                    elif frm == 6 and to == 3:
                        print(f"{round(x / 8361, 4)} yd\xb2")
                    elif frm == 6 and to == 4:
                        print(f"{x / 25900000000} mi\xb2 ")
                    elif frm == 6 and to == 5:
                        print(f"{x * 100} mm\xb2")
                    elif frm == 6 and to == 6:
                        print(f"{x} cm\xb2")
                    elif frm == 6 and to == 7:
                        print(f"{round(x / 10000, 4)} m\xb2")
                    elif frm == 6 and to == 8:
                        print(f"{x / 10000000000} km\xb2")
                    elif frm == 7 and to == 1:
                        print(f"{round(x * 1550, 3)} in\xb2")
                    elif frm == 7 and to == 2:
                        print(f"{round(x * 10.76, 2)} ft\xb2")
                    elif frm == 7 and to == 3:
                        print(f"{round(x * 1.196, 2)} yd\xb2")
                    elif frm == 7 and to == 4:
                        print(f"{x / 2590000} mi\xb2")
                    elif frm == 7 and to == 5:
                        print(f"{x * 1000000} mm\xb2")
                    elif frm == 7 and to == 6:
                        print(f"{x * 100000} cm\xb2") 
                    elif frm == 7 and to == 7:
                        print(f"{x} m\xb2")
                    elif frm == 7 and to == 8:
                        print(f"{x / 1000000} km\xb2")
                    elif frm == 8 and to == 1:
                        print(f"{x / 1550000000} in\xb2")
                    elif frm == 8 and to == 2:
                        print(f"{x * 10760000} ft\xb2")
                    elif frm == 8 and to == 3:
                        print(f"{x * 1196000} yd\xb2")
                    elif frm == 8 and to == 4:
                        print(f"{round(x / 2.59, 2)} mi\xb2")
                    elif frm == 8 and to == 5:
                        print(f"{x * 1000000000000} mm\xb2")
                    elif frm == 8 and to == 6:
                        print(f"{x * 10000000000} cm\xb2")
                    elif frm == 8 and to == 7:
                        print(f"{x * 1000000} m\xb2")
                    elif frm == 8 and to == 8:
                        print(f"{x} km\xb2")
                        
        elif op == 3:
            x = float(input("\nNumber: "))
            
            print("\nConvert from:\n1:feet (ft)\n2:centimeter (cm)")
            
            frm = int(input("\nSelect an option:\n>>> ")) 
            
            if frm < 1 or frm > 2:
                print("Wrong choice, back to the main menu you go")
                continue 
            
            print("\nConvert to:\n1:feet (ft))\n2:centimeter (cm)")
            to = int(input("\nSelect an option:\n>>> "))
            
            if to < 1 or to > 2:
                
                print("Wrong choice, back to the main menu you go")
                continue
            
            elif frm == 1 and to == 1:
                print(f"{x} ft")
            elif frm == 1 and to == 2:
                print(f"{x * 30.48} cm")
            elif frm == 2 and to == 1:
                print(f"{x /  30.48} ft")
            elif frm == 2 and to == 2:
                print(f"{x} cm")
                
        elif op == 4:
            x = float(input("\nTemperature: "))
            print("\nConvert from:\n1:celcius (\xb0c)\n2:fahrenheit (\xb0f)\n3:kelvin (k)")
            frm = int(input("\nSelect an option:\n>>> ")) 
            if frm < 1 or frm > 3:
                print("Wrong choice, back to the main menu you go")
                continue 
            print("\nConvert to\n1:celcius (\xb0c)\n2:fahrenheit (\xb0f)\n3:kelvin (k)")
            to = int(input("\nSelect an option:\n>>> "))
            if to < 1 or to > 3:
                print("Wrong choice, back to the main menu you go")
                continue
            elif frm == 1 and to == 1:
                print(f"{x} \xb0C")
            elif frm == 1 and to == 2:
                print(f"{round(x * 9/5+32, 2)} \xb0F")
            elif frm == 1 and to == 3:
                print(f"{round(x + 273.15, 2)} K")
            elif frm == 2 and to == 1:
                print(f"{round((x - 32) * (5/9), 2)} \xb0C")
            elif frm == 2 and to  == 2:
                print(f"{x} \xb0F")
            elif frm == 2 and to == 3:
                print(f"{round((x + 459.67) * (5/9), 2)} K")
            elif frm == 3 and to == 1:
                print(f"{x - 273.15} \xb0C")
            elif frm == 3 and to == 2:
                print(f"{round((9/5) * (x - 273.15) + 32, 2)} \xb0F")
            elif frm == 3 and to == 3:
                print(f"{x} K")
                
        elif op == 0:
            print("Goodbye")
            break
        
    except Exception:
            print("Please enter a number or 0 to exit")
        