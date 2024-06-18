import textract
import subprocess
import os

START_YEAR = 2013
END_YEAR = 2023

# load document
def parse_doc(fname, quarter, year):
    # parse doc into text
    if '.docx' in fname:
      try:
        text_bytes = textract.process(fname)
        text = text_bytes.decode('utf-8')
      except Exception as e:
        print(f"Error {e} occurred while trying to load file")

    elif '.doc' in fname:
      try:
        result = subprocess.run(['antiword', fname], stdout=subprocess.PIPE)
        text = result.stdout.decode('utf-8')
      except Exception as e:
          print(f"Error {e} occurred while trying to load file")

    print(f"Text loaded for Q{quarter}, {year}.")

path = '/Volumes/USB2/cba-polrep-anal/data'
def parse_docs():
    for year in range(START_YEAR, END_YEAR + 1):
        for quarter in range(1, 5):
            paths = [path + f'/{year}/Program Q{quarter}, {year} eng.doc',
                     path + f'/{year}/Program Q{quarter}, {year} Eng.doc',
                     path + f'/{year}/Program Q{quarter}, {year} eng.docx',
                     path + f'/{year}/Program Q{quarter}, {year} Eng.docx']
            # obtain file path
            file_path = ''
            for p in paths:
              if os.path.exists(p):
                file_path = p
                break
            if file_path == '':
              raise FileNotFoundError(f"Q{quarter}, {year} file does not exist")
            parse_doc(file_path, quarter, year)

parse_docs()