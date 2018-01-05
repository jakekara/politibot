from Politibot.ConnAssembly.ConnAssembly import ConnAssembly
import json

ctass = ConnAssembly()

# print json.dumps(ctass.candidates(), indent=2)

print json.dumps(ctass.candidate("H",5), indent=2)

print json.dumps(ctass.bill_history()[:10])
