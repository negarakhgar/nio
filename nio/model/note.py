from typing import Dict, List


class Note:
    def __init__(self, title: str, content: str, metadata: Dict[str, List[str]]):
        self.title = title
        self.content = content
        self.metadata = metadata 



        
