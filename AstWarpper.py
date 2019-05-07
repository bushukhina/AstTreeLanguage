import ast
import traceback
import re
from AstVisitor import NodeVisitor


class AstWrapper:
    def __init__(self, file):
        with open(file, "r") as source:
            self.tree = ast.parse(source.read())
        # tree = ast.parse("print(2+2)")
        self.NV = NodeVisitor()
        self.NV.visit(self.tree)

    def dump(self):
        # вывод получившегося дерева
        print(ast.dump(self.tree))

    def execute(self, g_dict):
        d = {"__builtins__": None}
        glob_dict = {**g_dict, **d}
        try:
            exec(compile(source=self.tree, filename="<ast>", mode='exec'), glob_dict)
        except TypeError:
            print("Error on line", re.search('line (\d)', traceback.format_exc()).groups('0')[0])
            print("Unknown name or function")
