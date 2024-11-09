import openpyxl as op
wb=op.load_workbook("openpyxl_test.xlsx") # 이미 있던 엑셀 파일을 불러옴
ws=wb["new sheet1"] # 활성화 시트
ws.delete_cols(2,1) # 두번째 열의 첫번째 만 삭제 2,2 면 2개 삭제 2,3이면 2열 3 삭제
wb.save("openpyxl_test.xlsx") # 저장함