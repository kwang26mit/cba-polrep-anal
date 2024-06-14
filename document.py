# The following classes segment each policy report.

from info import SECTIONS, TOPIC_TAGS

class ID():
    ''' class to represent a report ID'''
    # fields: year: int, quarter: int
    def __init__(year: int, quarter: int):
        if quarter > 4 or quarter < 0:
            raise ValueError(f'improper quarter {quarter}')

class Report():
    ''' class to represent a quarter policy report '''
    # fields: id: ID, body: Dict[str, Section], topics: List[str]
    def __init__(id: ID, body: str):
        # parse results into sections 
        pass

class Section():
    ''' class to represent a section of a quarter policy report '''
    # fields: id: ID, section_name: str, paragraphs: List[Paragraph]
    def __init__(id: ID, body: str):
        # parse results into paragraphs
        pass

class Paragraph():
    ''' class to represent a paragraph of a section of a quarter policy report '''
    # fields: id: ID, section_name: str, body: str
    def __init__(id: ID, body: str):
        pass