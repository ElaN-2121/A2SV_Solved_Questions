class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_map=defaultdict(list)
        for path in paths:
            parts=path.split(" ")
            directory_path= parts[0]
            file_content=parts[1:]
            for i in file_content:
                file_name, content = i.split("(")
                content=content[:-1] #to remove the extra closing bracket
                content_map[content].append(directory_path + "/" + file_name)
        return [files for files in content_map.values() if len(files)>1]
