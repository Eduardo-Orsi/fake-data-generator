from faker import Faker
import xlsxwriter
from validate_docbr import CPF

file_name = input("Nome do arquivo a ser gerado: ")
number_of_data_holders = int(input("Quantas pessoas devem ser geradas: "))

workbook = xlsxwriter.Workbook(f'{file_name}.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write(0, 0, "numero_documento")
worksheet.write(0, 1, "nome")
worksheet.write(0, 2, "telefone")
worksheet.write(0, 3, "email")
worksheet.write(0, 4, "data_ultima_alteracao")

fake = Faker('pt_BR')
Faker.seed(10)

for row in range(number_of_data_holders):

    document_number = CPF()
    document_number = document_number.generate()
    name = fake.name_nonbinary()
    email = f'{name.lower()}@{fake.free_email_domain()}'
    email = email.replace(' ', '')
    phone = fake.msisdn()

    worksheet.write(row+1, 0, document_number)
    worksheet.write(row+1, 1, name)
    worksheet.write(row+1, 2, phone)
    worksheet.write(row+1, 3, email)

workbook.close()
