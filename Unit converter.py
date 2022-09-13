

print(" --------------------------------Unit converter-------------------------------- ")

while True:
    print()
    print("\nMain menu\n\n1:Angle\n2:Area\n3:Height\n4:Temperature\n0:Exit")
    try:
        op = int(input("\nPlease enter an option:\n>>> "))
        
        if op < 0 or op > 5:
                print("Invalid number, try again")
        
            
        elif op == 1:
                    x = int(input("\nNumber: "))
                    
                    print("\nConvert from:\n1:degree\n2:radian\n3:minutes\n4:seconds\n5:quadrant")
                    frm = int(input("\nPlease enter an option 1-5:\n>>> "))
                    print("\nConvert to:\n1:degree\n2:radian\n3:minutes\n4:seconds\n5:quadrant")
                    to = int(input("\nPlease enter an option 1-5:\n>>> "))
                    if to < 1:
                        print("Wrong choice, back to the main menu you go")
                    elif  to > 5:
                        print("Wrong choice, back to the main menu you go")
                    if frm == 1 and to == 1:
                        print(f"{x}°")
                    elif frm == 1 and to == 2:
                        value = x / 57.3
                        print("%.4f" % value , "rad")
                    elif frm == 1 and to == 3:
                        print(f"{x * 60}'")
                    elif frm == 1 and to == 4:
                        print(f'{x * 3600}"') 
                    elif frm == 1 and to == 5:
                        val = x / 90
                        print("%.4f" % val , "quadrant")
                    elif frm == 2 and to == 1:
                        res = x * 57.3
                        print("%.4f" %res, "°")
                    elif frm == 2 and to == 2:
                        print(f"{x} rad")
                    elif frm == 2 and to == 3:
                        prod = x * 3438
                        print("%4.f" % prod , "'" )
                    elif frm == 2 and to == 4:
                        print(f"{x * 206300}")
                    elif frm == 2 and to == 5:
                        quad = x / 1.571
                        print("%.4f" % quad , "quadrant")
                        
                    elif frm == 3 and to == 1:
                        min = x / 60
                        print("%.4f" % min, "°" )
                    elif frm == 3 and to == 2:
                        ans = x / 3438
                        print("%.4f" % ans , "rad")
                    elif frm == 3 and to == 3:
                        print(f"{x}'")
                    elif frm == 3 and to == 4:
                        print(f'{x * 60}"')  
                    elif frm == 3 and to == 5:
                        rta = x / 5400
                        print("%.4f" % rta , "quadrant")
                    elif frm == 4 and to == 1:
                        sec = x / 3600
                        print("%.4f" % sec , "º")
                    elif frm == 4 and to == 2:
                        print(f"{x / 206300} rad")
                    elif frm == 4 and to == 3:
                        sam = x / 60
                        print("%.4f" % sam , "'")
                    elif frm == 4 and to == 4:
                        print(f'{x}"')        
                    elif frm == 4 and to == 5:
                        print(f"{x / 324000} quadrant")
                    elif frm == 5 and to == 1:
                        print(f"{x * 90}º")
                    elif frm == 5 and to == 2:
                        radi = x * 1.5708
                        print("%.4f" % radi , "rad") 
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
                    print("\nConvert to:\n1-square inch (in²)\n2:square foot (ft²)\n3:square yard (yd²)\n4:square mile (mi²)\n5:square milimiter (mm²)\n6:square centimeter (cm²)\n7:square meter (m²)\n8:square kilometer (km²)")
                    to = int(input("\nSelect an option:\n>>> "))
                    if frm == 1 and to == 1:
                        print(f"{x} in²")
                    elif frm == 1 and to == 2:
                        ft = x / 144
                        print("%.4f" %ft ,"ft²" )
                    elif frm == 1 and to == 3:
                        yd = x / 1296
                        print("%.4f" %yd , "yd\xb2")
                    elif frm == 1 and to == 4:
                        print(f"{x /4014000000} mi\xb2")
                    elif frm == 1 and to == 5:
                        print(f"{x * 645.2} mm\xb2")
                    elif frm == 1 and to == 6:
                        print(f"{x * 6.452} cm\xb2")
                    elif frm == 1 and to == 7:
                        met = x / 1550
                        print("%.4f" % met , "m\xb2") 
                    elif frm == 1 and to == 8:
                        print(f"{x /1550000000} km\xb2 ")
                    elif frm == 2 and to == 1:
                        print(f"{x * 144} in\xb2")
                    elif frm == 2 and to == 2:
                        print(f"{x} in\xb2")
                    elif frm == 2 and to == 3:
                        yd = x / 9
                        print("%.4f" % yd , "yd\xb2")
                    elif frm == 2 and to == 4:
                        print(f"{x / 27880000} mi\xb2")
                    elif frm == 2 and to == 5:
                        print(f"{x * 92903.04} mm\xb2")
                    elif frm == 2 and to == 6:
                        print(f"{x * 929.0304} cm\xb2 ")
                    elif frm == 2 and to == 7:
                        m = x / 10.76
                        print("%.4f" %m , "m\xb2")
                    elif frm == 2 and to == 8:
                        print(f"{x / 10760000} km\xb2")
                    elif frm == 3 and to == 1:
                        print(f"{x * 1296} in\xb2")
                        
                        
                    
        elif op == 3:
            pass
        
        elif op == 4:
            pass
        
        elif op == 5:
            pass
        
        elif op == 6:
            pass            
                        
        elif op == 0:
            print("Goodbye")
            break
    except Exception:
            print("Please enter a number or 0 to exit")
        