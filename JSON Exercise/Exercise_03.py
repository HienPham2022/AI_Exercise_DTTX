#in giá trị key:value theo format
import json
from random import sample
sampleJson = {"key1":"value2","key2":"value2","key3":"value3"}
prettyPrintedJson = json.dumps(sampleJson,indent=2,separators=("2","="))
print(prettyPrintedJson)
