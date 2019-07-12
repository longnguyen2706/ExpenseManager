from FileManipulation.read_util import filter_by_cols, get_file_in_resource
import tabula
PDF_FILE = "../resources/DBS_Mar19.pdf"
# PDF_FILE = "../resources/FRANK ACCOUNT-0001-Apr-19.pdf"
import pdftotext

def read_pdf(file_path):
    columns =['Date', 'Date', 'Description', 'Cheque', 'Withdrawal', 'Deposit', 'Balance']
    # Read pdf into DataFrame
    df_list = tabula.read_pdf(file_path, pages='all', multiple_tables=True)

    idx = 0
    for df in df_list:
        idx+=1
        df = filter_by_cols(df, columns)
        df.to_excel("output.xlsx",sheet_name='Sheet_name'+str(idx))

def pdf_to_excel(file_path):
    tabula.convert_into(file_path, "output.xlsx", output_format="xlsx", pages='all')

def pdf_to_text(file_path):


    # Load your PDF
    with open(file_path, "rb") as f:
        pdf = pdftotext.PDF(f)

    # If it's password-protected
    # with open("secure.pdf", "rb") as f:
    #     pdf = pdftotext.PDF(f, "secret")

    # How many pages?
    print(len(pdf))

    # Iterate over all the pages
    for page in pdf:
        print(page)


    # # Read some individual pages
    # print(pdf[0])
    # print(pdf[1])

    # Read all the text into one string
    print("\n\n".join(pdf))
def main():
    pdf_path = get_file_in_resource(PDF_FILE)
    # df_list = tabula.read_pdf(pdf_path, pages='all', multiple_tables=True, encoding='ISO-8859-1')
    # print(df_list)
    # read_pdf(pdf_path)
    # pdf_to_excel(pdf_path)
    pdf_to_text(pdf_path)

if __name__ == "__main__":
    main()