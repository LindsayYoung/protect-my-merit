"""" Testing out parsing of a SF-50"""

from pypdf import PdfReader

reader = PdfReader("data/sf50s/SF50_NO_COMMIT.pdf")
number_of_pages = len(reader.pages)
p = 0

info_array = []

while p <= number_of_pages:
    page = reader.pages[0]
    text = page.extract_text()
    fields = text.split("\n")
    """ it would probably be better to append so that if one 
    page gets messed up the next pages are extracted correctly, 
    but this is just a test run """
    info_array.extend(fields)
    p+=1

print("Print contents so I can figure out the mapping key")
x = 0
while x < len(info_array):
    print (x, info_array[x])
    x+=1

def data_mapper(info_array):
    data_map = {}
    data_map['name'] = info_array[216]
    data_map['gs_level'] = [9]
    data_map['locality_pay'] = [10]
    data_map['salary'] = [16]
    data_map['clearance'] = [19]
    data_map['title'] = [25]

    return(data_map)

data_map = data_mapper(info_array)
