def bill ():
	Number_of_devices=int(input("How many devices you use: ".title()))
	total=0
	Rate=float(input("Enter the rate of the company(/Kwh): $".title()))
	for i in range(1,Number_of_devices+1):
		Name=input(f"Enter the Name of device {i}: ".title())
		Watt =float(input(f"Enter the watt of device {i}: ".title()))
		Hour =float(input(f"Enter the used hour of device {i}: ".title()))
		Rate=0.46
		Kw=Watt/1000
		Kwh=Kw*Hour*720
		Money=Kwh*Rate
		total+=Money
	print("---------------------------------")
	print(f"The bill of this month is: ${total:.2f}".title())	
	print("---------------------------------")
	payment=input("Do you want to pay the bill (y/n): ")
	if payment=="y":
		print("--------------------------------------")
		print(f"Short Payment Method *789*345678*{total}# ")
		print("--------------------------------------")
		
	elif payment=="n":
		print("-----------------------------")
		print("Pay the bill 1-5 of the month")
		print("-----------------------------")
bill()