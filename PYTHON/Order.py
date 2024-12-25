def order ():
	print("                                 Welcome to KFC")
	print("                                ----------------")
	print("     OUR MENU \n    ----------")
	a= "1. Chicken Chips: $1.5"
	b= "2. Chicken Burger: $2"
	c= "3. Fish Burger: $2"
	d= "4. Shuarma: $1"
	print(a)
	print(b)
	print(c)
	print(d)
	def l():
		N=int(input("How many items you want to order: ".title()))
		if N ==1 or N==2 or N==3 or N==4 :
			def m():
				total=0
				amount=0
				for i in range (1,N+1):
					x=int(input(f"Enter Item {i}: "))
					if x==1 or x==2 or x==3 or x==4:
						y=int(input(f"Enter the quantity of Item {i}: "))
						
						if x==1:
							price=1.5
							amount+=y*price
						elif x==2:
							price=2
							amount+=y*price
						elif x==3:
							price=2
							amount+=y*price
						elif x==4:
							price=1
							amount+=y*price
					else:
						print(f"Your order is {N} items".title())
						print(" ")
						m()
					total+=amount
				if total>=1:
					print(f"The total is ${total}")
					print("short payment method (*789*706981*$#)".title())
					exit()
		else:
			print(f"We Don't Have {N} Orders")
			l()	
		m()
	l()
order()

