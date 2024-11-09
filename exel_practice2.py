"""""
실습문제 (2)
조건: "openpyxl_test.xlsx" 파일을 로드하고, 첫 번째 활성화된 Sheet에 접근하여 셀 A1의 값을 읽어 출력하시오.
"""
import openpyxl as op
wb=op.load_workbook("openpyxl_test.xlsx") # 원래 있던 엑셀파일을 가지고옴
ws=wb.active # 시트 활성화
print(ws["A1"].value) # 셀 A1의 값 출력


