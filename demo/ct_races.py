from Politibot.ProPublica.CampaignFinance import CampaignFinance
import env, json
from pandas.io.json import json_normalize

conn = CampaignFinance(env.PROP_KEY)

races = conn.races("CT")

json_normalize(ct_delegation.results()).to_csv("ct-races.csv")
