from datetime import datetime
import pandas as pd 
pin=int(input("Sameyso pin cusub: ".title()))
if len(str(pin))==4:
	h=float(input("Lacag soo gasho: ".title()))
	def EVC():
		global h
		print(" ")
		x=input("Fadlan gali form-ka lacag dirista: ".title())
		print(" ")
		if x =="*770#":
			print(" ")
			print("-EVCPlus-")
			y=int(input("Fadlan gali pin-kaaga: ".title()))
			if y==pin:
				print(" ")
				A="EVCPlus"
				a="1. Itus haraagaaga".title()
				b="2. Kaarka hadalka".title()
				c= "3. Bixi biiil".title()
				d= "4. uwareeji EVCplus ".title()
				print(A)
				print(a)
				print(b)
				print(c)
				print(d)
				print(" ")
				z=int(input("Dooro adeega: ".title()))
				if z==1:
					print(f"Haraagaaga waa ${h}")
				elif z==2:
					print("Madiiwan gashno".title())
				elif z==3:
					print("Madiiwan gashno".title())
				elif z==4:
					n= input("Fadlan gali mobile-ka: ".title())
					if n.isdigit() and n.startswith('61')and len(str(n))==9:
						p=float(input("Fadlan gali lacagta: ".title()))
						print(" ")
						if p<=h:
							d="1. Haa"
							f= "2. Maya"
							print(d)
							print(f)
							w=int(input(f"mahubta inaad ${p} uwareejisid {n}: ".title()))
							print(" ")
							if w==1:
								h-=p
								

								fi  = datetime.now().hour
								min = datetime.now().minute
								sec = datetime.now().second
								t = f'{fi}: {min} : {sec}'
								date = datetime.now().strftime('%d/%m/%Y')

								file = 'New Microsoft Excel Worksheet.xlsx'
								q = pd.read_excel(file)
								u = {'Numker ka loo direy':n,'Waqtiga la direy':t,'Tariikhda la direy':date,'Xadiga la direy':f'${p}'}
								q = q._append(u,ignore_index = True)
								q.to_excel(file,index = False)

								print(f"[-EVCPlus-] ${p} ayaad uwareejisay 0{n}, Haraagaagu waa ${h}.")
							else:
								print("Mahadsanid")
						else:
							print("Haraagaaga kuguma filno".title())
					else:
						print("Number-kaan madiiwan gashna".title())
			else:
					print("<-EVCPlus-> Numberka sirta ah waa qalad".title())
		else:
				print("shortcut-ka aad garaacday ma han mid jira.".title())
				print(" ")
		repeat = input("Marabta inaad dib ulabatid (y/n): ").lower()
		if repeat == "y":
				print("-----------------------------------------------------------------------------------")
				EVC()
	EVC()
else:
	print("Pin-ku waa inuu ka koobnaadaa 4 god".title())