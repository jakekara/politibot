#
# Load all of the races in Connecticut from the ProPublica API
#

from Politibot.ProPublica.CampaignFinance import CampaignFinance 
import env
import json
import pandas as pd

conn = CampaignFinance(env.PROP_KEY)

races = conn.races("CT").results()

# Pretty-print json results
print json.dumps(races, indent=2)

# Now just list the candidates names
print "\n".join(map(lambda x: x["candidate"]["name"], races))
