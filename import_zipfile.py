import zipfile
from lxml import etree

def get_word_xml(docx_filename):
   with open(docx_filename) as f:
      zip = zipfile.ZipFile(f)
      xml_content = zip.read('word/document.xml')
   return xml_content

# print get_word_xml('SAP.docx')



def get_xml_tree(xml_string):
   return etree.fromstring(xml_string)

get_xml_tree(xml_content)

etree.tostring(xmltree, pretty_print=True)
