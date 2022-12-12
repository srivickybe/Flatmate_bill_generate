
from Report import ReportPdf
from flat import Bill, Flatmate
        
amount = float(input("Please enter bill the Amount: ")) 
period = (input("Please enter Bill period? e.g december 2021 :  ")) 

name1 = input("what is your name? ")
days_in_house1 = int(input(f"how many days {name1} stayed in the flat : "))

name2 = input("what is your other flat person name? ")
days_in_house2 = int(input(f"how many days {name2} stayed in the flat : "))
  
the_bill = Bill(amount, period)
Flatmate1 = Flatmate(name1, days_in_house1)
Flatmate2 = Flatmate(name2, days_in_house2)

print(f"{Flatmate1.name} Pays", Flatmate1.pays(the_bill, Flatmate2))
print(f"{Flatmate2.name} Pays", Flatmate2.pays(the_bill, Flatmate1))

pdf_report = ReportPdf(f"{the_bill.period}.pdf")

pdf_report.generate(Flatmate1, Flatmate2, the_bill)