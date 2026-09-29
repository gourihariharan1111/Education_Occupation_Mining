import requests
import pandas as pd


url = "https://statistikdatabasen.scb.se/api/v2/tables/TAB4446/data"




# Ages available: all ages = "*", 16-24, 25-29, 30-34, 35-39, 40-44, 45-49, 50-54, 55-59, 60-64, 065-69
AGES = "*"

# Gender: * = both, 1 = men, 2 = women
GENDER = "*" 

# Year of data: * = all years, 2020, 2021, 2022, 2023, 2024
YEAR = "2024"

# Education: all = "*",
# 0 General education
# 1 Education science and teacher training
# 2 Humanities and art
# 3 Social sciences, law and business administration
# 4 Natural sciences, mathematics and Information and Communication Technologies (ICTs)
# 5 Engineering,  manufacturing and construction
# 6 Agriculture and forestry; veterinary
# 7 Health and welfare
# 8 Services
# 9 Unknown
EDUCATION = "*"


params = {
    "lang": "en",
    "valueCodes[Yrke2012]": "*",
    # "valueCodes[Alder]": AGES,
    # "valueCodes[Kon]": GENDER,
    "valueCodes[Tid]": YEAR,
    # "valueCodes[UtbinriktnSUN2020]": EDUCATION,
    "valueCodes[ContentsCode]": "000006Y3"
}

response = requests.get(url, params=params)
data = response.json()

# print(data["id"])
# print(data["size"])

# rows = []
# occupations = data["dimension"]["Yrke2012"]["category"]["index"]
# educations = data["dimension"]["UtbinriktnSUN2020"]["category"]["index"]
# ages = data["dimension"]["Alder"]["category"]["index"]
# genders = data["dimension"]["Kon"]["category"]["index"]
# i = 0;
# for occupation in occupations:
#     for education in educations:
#         for age in ages:
#             for gender in genders:
#                 rows.append([
#                     occupation,
#                     education,
#                     age,
#                     gender,
#                     data["value"][i]
#                 ]) 
#                 i+=1


occupation_index = data["dimension"]["Yrke2012"]["category"]["index"]
occupation_labels = data["dimension"]["Yrke2012"]["category"]["label"]
values = data["value"]

for code, position in occupation_index.items():
    name = occupation_labels[code]
    employees = values[position]

    print(code, name, employees)


# print(data)