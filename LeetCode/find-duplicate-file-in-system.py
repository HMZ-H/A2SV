class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dic = {}

        for path in paths:
            parts = path.split(" ")
            d = parts[0]
            f = parts[1:]

            for file in f:
                f_part = file.split('(')
                f_name = f_part[0]
                f_cont = f_part[1][:-1]
                f_path = d + '/'+ f_name
                if f_cont not in dic:
                    dic[f_cont] = [f_path]
                else:
                    dic[f_cont].append(f_path)
        dupl = [g for g in dic.values() if len(g)>1]
        return dupl

        

        