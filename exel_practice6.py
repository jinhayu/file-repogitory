"""""
실습문제 (6)
조건: 새로운 Workbook을 생성하고 첫 번째 시트에 리스트 [2, 4, 8, 16, 32]의 각 값을 1행에 순서대로 저장하시오.
"""
import openpyxl as op
wb=op.Workbook()
ws=wb.active
list=list(map(int,input().split()))
for i in range(len(list)):
    ws.cell(row=1,column=i+1).value=list[i]
wb.save("one_test.xlsx")
