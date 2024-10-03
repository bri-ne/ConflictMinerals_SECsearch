from functions import *
from company_names import *
import datetime as dt

mineralKeyword = {
    "tableMineralsList" : [">Cobalt<",">Tin<", ">tantalum<", ">Tungsten<",">Lithium<", ">Gold<", ">Copper<", ">Gallium<", ">Aluminum<", ">Nickel<", ">Silicon<", ">Germanium<"],
    "mineralsList"      : ["Cobalt", "Lithium", "Gold", "Copper", "Gallium", "Aluminum", "Nickel", "Silicon", "Germanium"],
    "mineralsString"    : " \"Cobalt\" OR \"Lithium\" OR \"Gold\" OR \"Copper\" OR \"Gallium\" OR \"Aluminum\" OR \"Nickel\" OR \"Silicon\" OR \"Germanium\" ",
    "companies"         : c_names,
    "auditors"          : ["Responsible Minerals Initiative", "RMI", "Responsible Business Alliance", "RBA", "Fair Trade"],
    "formTypes"         : ["SD"]
}

params = {
  "query": mineralKeyword["companies"][0] ,
  "formTypes": mineralKeyword["formTypes"],
}


metalKeywords = mineralKeyword["tableMineralsList"]
auditKeywords = mineralKeyword["auditors"]

for i in range(len(mineralKeyword["companies"])):
 # print(i)
  params = {
  "query": mineralKeyword["companies"][i] ,
  "formTypes": mineralKeyword["formTypes"],
  }
  print(params)
  f = searchApiCall(params,csvData,metalKeywords,auditKeywords)
f.to_csv(f'output.csv_{dt.datetime.now()}', index=False)  
