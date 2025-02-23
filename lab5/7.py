
import re
t = "ghsjfh_hh_eqh_H_ejhrfkj_KJ"
result = re.sub(r"_([a-zA-Z])", lambda match: match.group(1).upper(), t)
print(result)