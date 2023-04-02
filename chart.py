from judge_line import JudgeLine

class Chart:
    version: int
    offset: float
    notes_count: int
    judge_lines: list[JudgeLine]

    def __init__(self, version: int, offset: float, notes_count: int, judge_lines: list[JudgeLine]):
        self.version = version
        self.offset = offset
        self.notes_count = notes_count
        self.judge_lines = judge_lines

    @classmethod
    def from_dict(cls, d: dict):
        #try:
        notesCounter = 0
        #if 'judgeLineList' in d:
        for judge_line in d['judgeLineList']:
            judge_line['numOfNotes'] = len(judge_line['notesAbove']) + len(judge_line['notesBelow'])
            notesCounter += judge_line['numOfNotes']
            judge_line['numOfNotesAbove'] = len(judge_line['notesAbove']) 
            judge_line['numOfNotesBelow'] = len(judge_line['notesBelow'])
            #print("Add|"+str(judge_line['numOfNotes'])+"|"+str(judge_line['numOfNotesAbove'])+":"+str(judge_line['numOfNotesBelow'])+"|["+str(notesCounter)+"]")
        #print("Notes:"+str(notesCounter))
        d['numOfNotes']=notesCounter
        #else:
        #    print("None")
        #except Exception as e:
        #    traceback.print_exc()
        version = d['formatVersion']
        if version == 1:
            return cls(version, d['offset'], d['numOfNotes'],
                       [*map(JudgeLine.from_dict_v1, d['judgeLineList'])])
        else:
            return cls(version, d['offset'], d['numOfNotes'],
                       [*map(JudgeLine.from_dict, d['judgeLineList'])])


__all__ = ['Chart']
