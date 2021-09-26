from docxtpl import DocxTemplate
import datetime


def gen_cv():

    company_name = input("Enter name of the Company : ")
    position_name = input("Enter name of the Position: ")

    today_date = datetime.datetime.today().strftime('%d/%m/%Y')

    elements = {'today_date': today_date,
                'company_name': company_name,
                'position_name': position_name
                }

# This open our master template
    doc = DocxTemplate("my_cover_letter.docx")

# This get and load them up
    doc.render(elements)

# This save the file with personalized filename
    doc.save('Cover_letter_'+company_name+'_'+position_name+'.docx')

# success message
    print('Resume generated successfully')


gen_cv()
