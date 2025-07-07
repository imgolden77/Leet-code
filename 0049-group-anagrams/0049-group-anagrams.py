class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = []

        for str in strs:
            count={}
            words=[]
            s={}
            fit = bool()
            fit = False
            for i in str:
                count[i]=count.get(i, 0) + 1
            for j in dictionary:
                if count == j["count"]:
                    j["words"].append(str)
                    fit = True
            if fit == False:        
                s["count"]=count
                s["words"]=[str]
                dictionary.append(s)
            

        result =[]
        for j in dictionary:
            result.append(j["words"])

        return result