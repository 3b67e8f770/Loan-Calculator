import math
import argparse


parser  = argparse.ArgumentParser()
parser.add_argument('--type', type = str)
parser.add_argument('--payment', type = int)    # m_p     monthly_payment   kwota miesiecznie   annuity_payment
parser.add_argument('--principal', type = int)  # p     loan_principal    kwota pozyczki  
parser.add_argument('--periods', type = int)    # n     number_of_periods ile miesiecy
parser.add_argument('--interest', type = float) # l     loan_interest     %
args = parser.parse_args()

if args.principal != None:
    p = args.principal
if args.payment != None:
    m_p = args.payment
if args.periods != None:
    n = args.periods
if args.interest != None:
    l = args.interest
    i = args.interest / 1200

if args.type == "diff" and args.payment == None:
    z=0
    for j in range(0,n):
        m = j + 1
        Dm = (p / n) + i * (p - ((p * (m-1))/ n))
        Dm=math.ceil(Dm)
        print(f'Month {m}: payment is {Dm}')
        z += Dm       
    print(f'Overpayment = {math.ceil(z - p)}')
    
 #--type=annuity --principal=1000000 --periods=60 --interest=10
elif args.type == "annuity" and args.payment == None:

        a = p * (i * ((1 + i) ** n) / ((1 + i) ** n -1))
        a=math.ceil(a)
        print(f'Your annuity payment = {a}!')
        print(f'Overpayment = {math.ceil(a *n) - p}')

elif args.type == "annuity" and args.principal == None:
        p = m_p / (i * ((1 + i) ** n) / ((1 + i) ** n -1))
        p=math.floor(p)
        print(f'Your loan principal = {p}!')
        print(f'Overpayment = {math.ceil(m_p *n) - p}')

elif args.type == "annuity" and args.periods == None and args.interest != None:
            
        n=math.log(m_p / (m_p - i * p), 1 + i)
        n=math.ceil(n)
        yy = int(n / 12)
        if yy == 1:
            years = "year"
        else:
            years = "years"
        mm = n % 12
        if mm == 1:
            months = "month"
        else:
            months = "months"
        if yy > 0 and mm > 0:
            print(f'It will take {yy} {years} and {mm} {months} to repay this loan!')
        elif yy > 0:
            print(f'It will take {yy} {years} to repay this loan!')
        else:
            print(f'It will take {mm} {months} to repay this loan!')
            
        print(f'Overpayment = {math.ceil(m_p *n) - p}')

else:  # (args.type == "diff" and args.payment != None) or args.type not in ["diff", "annuity"] or args.interest == None:
    print("Incorrect parameters")
    
