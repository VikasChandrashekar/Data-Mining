#!/usr/bin/env python
import sys

totalSales = 0
oldCombo=None

for line in sys.stdin:
        #strip each line
        line = line.strip()
        #split the line after each tab
        data = line.split("\t")
         
        dep,year,sales = data
        thisCombo = dep + "\t" + year
         
        if oldCombo and oldCombo != thisCombo:
            if totalSales > 25000000:
                print('%s\t%s' % (oldCombo, totalSales))
            totalSales=0
                 
        oldCombo=thisCombo
        totalSales += float(sales)
        
if oldCombo != None:
    if totalSales > 25000000:
        print('%s\t%s' % (oldCombo, totalSales))

# this_dept = None
# this_sales = 0
# this_year = None
# this_dept_year_combo = None
# word = None
# combo = None
# 
# # input comes from STDIN
# for line in sys.stdin:
#     # remove leading and trailing whitespace
#     line = line.strip()
# 
#     # parse the input we got from mapper.py
#     dept, year, sales = line.split('\t', 2)
#     
#     # convert count (currently a string) to int
#     try:
#         sales = int(sales)
#     except ValueError:
#         # count was not a number, so silently
#         # ignore/discard this line
#         continue
# 
#     # this IF-switch only works because Hadoop sorts map output
#     # by key (here: word) before it is passed to the reducer
#     combo = dept + "\t" + year
#     # if current_word == word:
#     if this_dept_year_combo == combo:
#         this_sales += sales
#     else:
#         if this_dept_year_combo:
#         # if current_word:
#             # write result to STDOUT
#             if this_sales > 25000:
#                 print('%s\t%s' % (this_dept_year_combo, this_sales))
#         this_sales = sales
#         # current_word = word
#         this_dept_year_combo = combo
# 
# # do not forget to output the last word if needed!
# if this_dept_year_combo == combo:
#     if this_sales > 25000:
# # if current_word == word:
#     # print('%s\t%s' % (current_word, current_count))
#         print('%s\t%s' % (this_dept_year_combo, this_sales))
