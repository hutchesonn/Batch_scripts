__author__ = 'Nathaniel'

import re
from xml.etree import ElementTree as et

infile = 'F:\\Extraction_Output\\06-19-2017_Container_Pilot\c03_pilot.xml'
outfile = 'F:\\Extraction_Output\\06-19-2017_Container_Pilot\c03_pilot_processed.xml'

output = open(outfile, 'w', encoding='utf8')
header = '<?xml version="1.0" encoding="UTF-8" standalone="no" ?>'
output.write(header)

xmlstring = open(infile, 'r', encoding='utf8').read()
pattern1 = re.compile(r'[^\S\r\n]+')
pattern2 = re.compile(r'\n ')
pattern3 = re.compile(r'\n\W<')
pattern4 = re.compile(r'(\n)([^<])')
pattern5 = re.compile(r'[^\S\r\n]+')
pattern6 = re.compile(r'\n?\s?<[!|?][^>]+>')
pattern7 = re.compile(r'<eadid [^>]+>')
pattern8 = re.compile(r'(</[^>]+>)([[a-zA-Z]|\(|\[|[\d]|<]|[[\"|‘“][a-zA-Z]])')
pattern9 = re.compile(r'(\S)(<[^/][^>]+>)')
pattern10 = re.compile(r'(\s[\"|“]) (<[^/>]+>)')

xmlstring1 = re.sub(pattern1, ' ', xmlstring)
xmlstring2 = re.sub(pattern2, r'\n', xmlstring1)
xmlstring3 = re.sub(pattern3, r'\n<', xmlstring2)
xmlstring4 = re.sub(pattern4, ' \\2', xmlstring3)
xmlstring5 = re.sub(pattern5, ' ', xmlstring4)
xmlstring6 = re.sub(pattern6, '', xmlstring5)
xmlstring7 = re.sub(pattern7, '<eadid>', xmlstring6)
xmlstring8 = re.sub(pattern8, '\\1 \\2', xmlstring7)
xmlstring9 = re.sub(pattern9, '\\1 \\2', xmlstring8)
xmlstring10 = re.sub(pattern10, '\\1\\2', xmlstring9)

output.write(xmlstring10)

output.close()
