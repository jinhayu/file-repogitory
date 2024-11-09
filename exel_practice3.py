"""""
실습문제 (3)
조건: 새로운 Workbook을 생성하고, 시트 "new_sheet1"을 추가한 후, 파일을 "test_result.xlsx"로 저장하시오.
"""
import openpyxl as op
wb=op.Workbook()
wb.create_sheet("new_sheet1")
wb.save("test_result.xlsx")