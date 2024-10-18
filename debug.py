import random
from parsers.pdfparser import PDFParser

def load_doc(file):
    """
    Test for error thrown by PDFParser
    :param file: .pdf file
    :return:
    """
    document = PDFParser(file)
    toc = document.toc.toc_dict
    sections = document.TextParser.Sectioning.sections_dict

    return document, toc, sections

def test_sectioning(file):
    """
    Test for sectioning error (len sections not corresponding to len toc)
    :param file: .pdf file
    :return:
    """
    document, toc, sections = load_doc(file)
    if len(toc) >= len(sections.keys()):
        raise Exception('Sectioning fails to catch all toc items.')

    return document,toc,sections

def test_preamble(file):
    """
    Test for preamble creation
    :param file: .pdf file
    :return:
    """
    document, toc, sections = load_doc(file)
    preamble = document.TextParser.get_toc_header(0).text()

    return preamble


if __name__ == "__main__":
    path = "/home/david/PycharmProjects/frq-nlp/Data/prospectus"
    files_parse_error = ["Candriam.pdf", "pictet_sicav.pdf", "pictet_multi.pdf"]
    

    ##1 Parsing error
    #document,toc,sections = load_doc(path + "/" + random.choice(files_parse_error))

    ##2 Sectioning error
    document,toc,sections = test_sectioning(path + "/" + random.choice(files_section_error))

    ##3 Preamble error
    preamble = test_preamble(path + "/" + random.choice(files_preamble_error))