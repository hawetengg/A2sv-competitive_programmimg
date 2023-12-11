class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dictt = defaultdict(list)
        
        for path in paths:
            division = path.split(" ")
            currDir = division[0]
            
            for i in range(1,len(division)):
                fileName, fileContent = division[i].split("(")
                dictt[fileContent].append(f"{currDir}/{fileName}")
                
        return [val for val in dictt.values() if len(val) > 1]