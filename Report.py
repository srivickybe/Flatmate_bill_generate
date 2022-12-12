from fpdf import FPDF
import webbrowser
import os


class ReportPdf:
    """
    pdf for flatmates for the bill amount 
    """
    def __init__(self, filename):
        self.filename = filename
        
    def generate(self, flatamate1, flatmate2, bill):
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()
        
        flatmate1_pay = str(round(flatamate1.pays(bill, flatmate2),2))
        flatmate2_pay = str(round(flatmate2.pays(bill, flatamate1),2))
        #Insert title 
        pdf.set_font(family="Times", size=24, style='B')
        pdf.cell(w=0, h=80, txt="Flatmates Bill ", border=1,align='C', ln=1)
        
        #Insert Period lable & value
        pdf.set_font(family="Times", size=14, style='B')
        pdf.cell(w=100, h=40, txt="Period :", border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln =1)

        #Insert Name & Due Amount of the First flatname 
        pdf.set_font(family="Times", size=12)
        pdf.cell(w=100, h=40, txt=flatamate1.name, border=0)
        pdf.cell(w=150, h=40, txt=flatmate1_pay, border=0,align='L', ln=1)
        
        #Insert Name & Due Amount of the First flatname2
        pdf.cell(w=100, h=40, txt=flatmate2.name, border=0)
        pdf.cell(w=150, h=40, txt=flatmate2_pay, border=0,align='L', ln=1)
        
        #change the directory and open pdf created 
        os.chdir("files")
        pdf.output(self.filename)
        webbrowser.open(self.filename)