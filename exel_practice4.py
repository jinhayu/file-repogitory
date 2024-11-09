"""""
실습문제 (4)
조건: "openpyxl_test.xlsx" 파일의 활성화된 Sheet에 있는 셀 A1에서 B1까지의 범위를 읽어 출력하시오.
"""
import openpyxl as op
wb=op.load_workbook("openpyxl_test.xlsx")
ws=wb.active
rng=ws["A1:B1"]
print(rng)