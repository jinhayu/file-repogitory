import openpyxl as op
wb=op.load_workbook("openpyxl_test.xlsx") # 기존에 있던 엑셀 파일 불러옴
ws=wb["new sheet1"] # 시트 활성화
rng=ws["A1:D9"] # 셀 A1부터 D9까지 
for rng_data in rng: 
    for cell_data in rng_data:
        if cell_data.value%2==0: # 셀 A1 부터 D9까지 하나씩돌면서 짝수이면
            cell_data.value="" # 빈칸으로 만든다
wb.save("openpyxl_test.xlsx") # 저장함