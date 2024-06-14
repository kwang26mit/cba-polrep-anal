import textract

# load document
file_path = '/Volumes/USB2/cba-polrep-anal/data/2013-2017/2013/Program Q2, 2013 Eng.doc'

def parse_doc(fname):
    # parse doc into text
    text_bytes = textract.process(file_path)
    text = text_bytes.decode('utf-8')

    # find quarter and year
    idx = text.index("Monetary Policy Program,")
    quart_year = text[idx + len("Monetary Policy Program, "):idx + len("Monetary Policy Program, Q#, 20##")]
    quarter = quart_year[1:2]
    year = quart_year[4:8]
    print(f'quarter {quarter}, year {year}')


parse_doc(file_path)
# # Extract text from the document
# full_text = []
# for para in document.paragraphs:
#     full_text.append(para.text)

# # Combine the text from all paragraphs
# document_text = '\n'.join(full_text)

# print(document_text)