from Politibot.ProPublica.CampaignFinance import CampaignFinance
import env
from sys import argv

conn = CampaignFinance(env.PROP_KEY)
matches = conn.candidate_search(" ".join(argv[1:])).results()
 
print "\n".join(map(lambda x: x["candidate"]["name"], matches))
