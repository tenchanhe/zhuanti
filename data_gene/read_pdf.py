import pdfplumber

book =  pdfplumber.open('109選課寶典.pdf')
tablesss = []
for i in range (3,39):
        # print(i)
        pdf = book.pages[i].extract_table()
        # for p in pdf:
            # print(p)
	# print(pdf)
	# print(page.extract_table())
        tablesss.append(pdf)
        # for p in pdf:
            # tablesss.append(p.extract_table())
        # print(tablesss)
	# print('====================')

# for i in tablesss:
    # for j in i:
        # print(j)
ans = []
for line in tablesss:
    table = []
    for i in range (len(line)):
        page = []
        # print(tablesss[i])
        if line[i][0] == '課程名稱' and (len(line)-i) > 2:
                # print(tablesss[i])
                page.append(line[i+1][2])
                page.append(line[i+1][3])
                page.append(line[i+2][0])
                page.append(line[i+1][4])
        table.append(page)
    ans.append(table)

for i in ans:
    for j in i:
        if len(j) != 0:
            print(j)

