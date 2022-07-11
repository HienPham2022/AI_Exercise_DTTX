#in giá tri của key"history" từ dict ở dạng lồng
from random import sample


sampleDict = {
    "class":{
        "student":{
            "name":"Mike","marks":{
                "physis":70,
                "history":80
            }
        }
    }
}
print(sampleDict["class"]["student"]['marks']['history'])