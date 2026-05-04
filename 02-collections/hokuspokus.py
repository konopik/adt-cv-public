
from collections import defaultdict
listi = list(range(10))
print(listi[-1])
slovnik: defaultdict[str,list[list]]= defaultdict(lambda:["ahoj"])
slovnik["matematika"].append(object/"martin")
slovnik["matematika"].append(object/"peter")
slovnik["anglictina"].append(object/"martin")
print(slovnik)
print(slovnik["chemie"])
print("chemie" in slovnik)
