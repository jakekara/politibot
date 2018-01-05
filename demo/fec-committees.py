from Politibot.Fec.Fec import Fec 
import env
from datetime import datetime

import pandas as pd
from pandas.io.json import json_normalize

conn = Fec(env.FEC_KEY)

print "Fetching CT committees"
results = conn.committees({"state":"CT"}).results()
norm_committees = json_normalize(results)
norm_committees.to_csv("ct-committees-2018.csv")

cand_id = "S6CT05090"
print "Fetching info on candidate" + str(cand_id)

candidate = conn.candidate(cand_id).results()
json_normalize(candidate).to_csv(cand_id + ".csv")

senate_filings = conn.filings({
    "state":"CT",
    "office":"S",
    "min_receipt_date":datetime(2017,1,1).strftime("%Y-%m-%d")
}).results()

json_normalize(senate_filings).to_csv("senate-filings.csv")


conn = Fec(env.FEC_KEY,cycle="2016")
print("Fetching house filings from 2016")
json_normalize(conn.filings({
    "state":"CT",
    "office":"H",
}).results()).to_csv("house-filings-2016.csv")

conn = Fec(env.FEC_KEY,cycle="2018")
print("Fetching house filings from 2018")
json_normalize(conn.filings({
    "state":"CT",
    "office":"H",
}).results()).to_csv("house-filings-2018.csv")
