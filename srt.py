import os, re

class srt_file:
    def __init__(self, srt_path):
        self.full_path = srt_path
        self.contents = None
        self.modified_contents = []
        self.regex = {
            "hi_speaker_annotation"     : re.compile(r"^[A-Z]+\:\s"),
            "hi_parentheses_one_line"   : re.compile(r"^\([A-Z\s\-]+\)"),
            "hi_parentheses_start_line" : re.compile(r"^\([A-Z\s\-]+"),
            "hi_parentheses_end_line"   : re.compile(r"^[A-Z\s\-]+\)") }
        self.lines = {}
        self._load_file()

    def _load_file(self):
        try:
            with open(self.full_path) as f:
                self.contents = f.readlines()
            self.contents = [x.strip() for x in self.contents]
        except:
            print(f"could not open file: {self.full_path}")

    def save(self):
        if self.modified_contents:
            try:
                with open('test.srt', 'w') as f: # TODO: change file name dest.
                    for line in self.modified_contents:
                        f.write(f"{line}\n")
                print("save ok")
            except:
                print("save failed")
