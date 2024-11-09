"""""
실습문제 (1)
조건: openpyxl을 이용하여 새로운 Workbook을 생성하고 파일 이름을 "new_workbook.xlsx"로 저장하시오.
"""
import openpyxl as op
wb=op.Workbook()
wb.save("new_workbook.xlsx")