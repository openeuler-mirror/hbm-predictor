"""
Copyright (c) 2024 Ronglong Wu
Calchas is licensed under Mulan PSL v2.
You can use this software according to the terms and conditions of the Mulan PSL v2.
You may obtain a copy of Mulan PSL v2 at:
http://license.coscl.org.cn/MulanPSL2
THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND,
EITHER EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT,
MERCHANTABILITY OR FIT FOR A PARTICULAR PURPOSE.
See the Mulan PSL v2 for more details.
"""

# encoding: utf-8
import os
import pandas as pd

list_ue = []
list_ue_1d_max = []

cnt_ue = 0
list_ce = []
list_ce_1d_max = []
cnt_ce = 0

for i in range(0,8):
    list_ce_1d_max.append(0)

    list_ue_1d_max.append(0)


def ue_get_temp_ratio(file_path):
    csv_single_df = pd.read_csv(file_path)
    checked_df = csv_single_df[(csv_single_df["1h_max"] > 0) & (csv_single_df["7d_max"] <= 200)]
    global list_ue_1d_max
    global cnt_ue
    for i in range(0,8):
        if i == 0:
            list_ue_1d_max[i] =len(checked_df[(checked_df["1d_max"] < i + 25)])

        elif i == 7:
            list_ue_1d_max[i] =len(checked_df[(checked_df["1d_max"] >= 55)])
        else:
            list_ue_1d_max[i] =len(checked_df[(checked_df["1d_max"] >= 5*i + 20) & (checked_df["1d_max"] < 5*i + 25)])
    cnt_ue = len(checked_df)

def ce_get_temp_ratio(file_path):
    csv_single_df = pd.read_csv(file_path)
    checked_df = csv_single_df[(csv_single_df["1h_max"] > 0) & (csv_single_df["7d_max"] <= 200)]

    global list_ce_1d_max

    global cnt_ce
    for i in range(0,8):
        if i == 0:
            list_ce_1d_max[i] =len(checked_df[(checked_df["1d_max"] < i + 25)])
        elif i == 7:
            list_ce_1d_max[i] =len(checked_df[(checked_df["1d_max"] >= 55)])
        else:
            list_ce_1d_max[i] =len(checked_df[(checked_df["1d_max"] >= 5*i + 20) & (checked_df["1d_max"] < 5*i + 25)])
    cnt_ce = len(checked_df)

def print_file_contents(file_path):
    with open(file_path, 'r') as file:
        print(file.read())


in_path1 = "./data/uer_temp.csv"
in_path2 = "./data/ce_temp.csv"
out_file1 = "./result/max_ue_temp_distribution.txt"
out_file2 = "./result/max_ce_temp_distribution.txt"
# out_list1 = "./ue_list_max_8"
# out_list2 = "./ce_list_max_8"

ue_get_temp_ratio(in_path1)
ce_get_temp_ratio(in_path2)

r_f1 = open(out_file1,'w')
r_f2 = open(out_file2,'w')
# r_f1.write("UE总数:  "+str(cnt_ue))
# r_f2.write("CE总数:  "+str(cnt_ce))

for i in range(0,8):
    if i == 0:
        str_init = "<25 :"
        r_f1.write(str_init)
        r_f2.write(str_init)

        ue_1d_cnt = list_ue_1d_max[i]


        str_ue_list_1d = "    Ratio:" + str(round(float(ue_1d_cnt) / cnt_ue, 4))+"\n"

        ce_1d_cnt = list_ce_1d_max[i]


        str_ce_list_1d = "    Ratio:" + str(round(float(ce_1d_cnt) / cnt_ce, 4))+"\n"

        r_f1.write(str_ue_list_1d)
        r_f2.write(str_ce_list_1d)

    elif i == 7:
        str_init = ">55 :"
        r_f1.write(str_init)
        r_f2.write(str_init)

        ue_1d_cnt = list_ue_1d_max[i]

        str_ue_list_1d = "    Ratio:" + str(round(float(ue_1d_cnt) / cnt_ue, 4)) + "\n"

        ce_1d_cnt = list_ce_1d_max[i]

        str_ce_list_1d =  "    Ratio:" + str(round(float(ce_1d_cnt) / cnt_ce, 4)) + "\n"

        r_f1.write(str_ue_list_1d)

        r_f2.write(str_ce_list_1d)

    else:
        str_init = "["+str(5*i+20)+","+str(5*i+25)+") :"
        r_f1.write(str_init)
        r_f2.write(str_init)

        ue_1d_cnt = list_ue_1d_max[i]
        str_ue_list_1d ="   Ratio:" + str(round(float(ue_1d_cnt) / cnt_ue, 4)) + "\n"
        ce_1d_cnt = list_ce_1d_max[i]

        str_ce_list_1d = "    Ratio:" + str(round(float(ce_1d_cnt) / cnt_ce, 4)) + "\n"


        r_f1.write(str_ue_list_1d)

        r_f2.write(str_ce_list_1d)

r_f1.close()
r_f2.close()
# Print the contents of the output files
print("===================== Max Temperature Distribution =====================")
print("***************************************")
print("==========CE Max Temperature Distribution==========")
print_file_contents(out_file2)
print("***************************************")
print("==========UE Max Temperature Distribution==========")
print_file_contents(out_file1)

#
# li_1 = []
# li_2 = []
# for i in range(0,8):
#     x1 = round(float(list_ue_1d_max[i])/cnt_ue,4)
#     li_1.append(x1)
#     x2 = round(float(list_ce_1d_max[i])/cnt_ce,4)
#     li_2.append(x2)
#
# s1 ="["
# s2 ="["
# for i in range(0,8):
#     if i != 7:
#         s1 = s1 + str(li_1[i])+","
#         s2 = s2 + str(li_2[i])+","
#     else:
#         s1 = s1 +str(li_1[i])
#         s2 = s2 +str(li_2[i])
# s1 =s1 +"]"
# s2 = s2+"]"
#
# l_f1 = open(out_list1,'w')
# l_f2 = open(out_list2,'w')
# l_f1.write(s1)
# l_f2.write(s2)

