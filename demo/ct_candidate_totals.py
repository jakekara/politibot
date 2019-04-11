from Politibot.ProPublica.CampaignFinance import CampaignFinance
import env, json
from pandas.io.json import json_normalize
import pandas as pd

conn = CampaignFinance(env.PROP_KEY, cycle="2018")

races = conn.races("CT")

json_normalize(races.results()).to_csv("ct-races.csv")

# Get the latest details on a candidate
def get_deets(cand):

    cand_data = conn.candidate(cand["candidate"]["id"])

    fname = str(cand["candidate"]["id"]) + ".csv"

    json_normalize(cand_data.results()).to_csv(fname)

    return json_normalize(cand_data.results())

pd.concat(map(get_deets, races.results())).to_csv("total.csv")
