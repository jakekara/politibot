from Politibot.ProPublica.Congress import Congress
import env, json
from pandas.io.json import json_normalize

conn = Congress(env.PROP_KEY)

ct_delegation = conn.delegation("CT")

print json.dumps(ct_delegation.results(), indent=2)

json_normalize(ct_delegation.results()).to_csv("ct-delegation.csv")

def bill_report(member):

    cosponsored = conn.cosponsored(member["id"])

    print (member["name"] + " cosponsored the following " +\
           str(cosponsored.results()[0]["num_results"]) +\
           " bills: ")

    bills = cosponsored.results()[0]["bills"]

    for i in range(len( bills )):
        bill = bills[i]
        print "\t" + str(i) + "\t" + bill["short_title"][:50] + "..."

    print ""

map(bill_report, ct_delegation.results())
    
