
print('Annuity plan')
PMT=float(input('enter the regular payment amount:'))
R=float(input('enter the rate:'))
N=int(input('enter the number of times interest is compunded:'))
T=int(input('enter the number of years:'))
A = PMT * (((1 + (R / N)) ** (N * T) - 1) / (R / N))
print('The annuity is:', round(A,2))
input()
