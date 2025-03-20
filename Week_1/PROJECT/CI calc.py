Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print('CI calculator')
... P=float(input('enter the principal value'))
... R=float(input('enter the rate'))
... N=int(input('enter the number of times interest is compunded'))
... T=int(input('enter the number of years'))
... A=P*(1+(R/N))**(N*T)
