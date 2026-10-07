import json
from src.qa import ask

print(json.dumps(ask("What caused past database outages related to capacity issues?"), indent=2))
print(json.dumps(ask("What's the best pizza topping?"), indent=2))  # should be rejected by scope check