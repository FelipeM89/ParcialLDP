from FiboVisitor import FiboVisitor
from FiboParser import FiboParser

class EvalVisitor(FiboVisitor):

    def visitProg(self, ctx: FiboParser.ProgContext):
        n = int(ctx.INT().getText())
        return self.fibonacci(n)

    def fibonacci(self, n):
        seq = []
        a, b = 0, 1
        while a <= n:
            seq.append(a)
            a, b = b, a + b
        return seq
