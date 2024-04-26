class FileInfo:
    def __init__(self, summary: str, file_path: str, parent: "FileInfo"):
        """
        Initializes a new instance of FileInfo.

        Args:
        summary (str): A brief description of the file.
        file_path (str): The path to the file.
        parent (FileInfo, optional): A reference to another FileInfo object that acts as the parent.
                                    Default is None, indicating no parent.
        """
        self.summary:str = summary
        self.file_path:str = file_path
        self.parent:"FileInfo" = parent
        self.children: list["FileInfo"] = []
    
    def __add_children__(self, child: "FileInfo"):
        self.children.append(child)

    def __repr__(self):
        """
        Provides a string representation of the object, useful for debugging.
        """
        return f"FileInfo(summary={self.summary}, file_path={self.file_path}, parent={self.parent}, children={self.children})"
