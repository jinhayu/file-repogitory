import openpyxl as op # 엑셀을 하기위한 openpyxl 를 적는다
wb=op.load_workbook("openpyxl_test.xlsx")
ws=wb["new sheet1"] # 엑셀 시트 활성화 지정할수있음 수동으로 지정할려면 wb.active
data=1
for i in range(1,10): # row의 값을 1부터 9까지
    for j in range(1,5): # column 의 값을 1부터 4까지
        ws.cell(row=i,column=j).value=data 
        data+=1 # data에 있는값을 하나씩증가
wb.save("openpyxl_test.xlsx") # 저장함