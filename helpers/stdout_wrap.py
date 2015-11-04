import sys
from io import StringIO


class CapturedOutput():

    def __init__(self):
        self.new_out, self.new_err = StringIO(), StringIO()
        self.old_out, self.old_err = sys.stdout, sys.stderr

        sys.stdout, sys.stderr = self.new_out, self.new_err

    def getvalue(self):
        output = self.new_out.getvalue().strip()
        return output

    def __del__(self):
        sys.stdout, sys.stderr = self.old_out, self.old_err