class Mark:
    def __init__(self):
        self._student_id = 0
        self._course_id = 0
        self._mark = 0.0 

    def setter(self,sid,cid,mark):
        self._student_id = sid
        self._course_id = cid
        self._mark = (float(mark))

    def list(self):
        print(f"Student ID: {self._student_id} | Course ID: {self._course_id} | Score: {self._mark}")
