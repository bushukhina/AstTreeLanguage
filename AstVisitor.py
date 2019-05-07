import ast
import sys

#Attribute

class NodeVisitor(ast.NodeVisitor):
    def visit(self, node):
        method = 'visit_' + node.__class__.__name__
        try:
            visitor = getattr(self, method)
        except AttributeError as e:
            print(f"{node.__class__} is not implemented")
            import traceback
            print(traceback.print_exc())
            sys.exit()
        return visitor(node)

    def generic_visit(self, node):
        for value in ast.iter_child_nodes(node):
            self.visit(value)

    def visit_Num(self, node):
        self.generic_visit(node)
        return node

    def visit_Str(self, node):
        self.generic_visit(node)
        return node

    def visit_Name(self, node):
        self.generic_visit(node)
        return node

    def visit_Assign(self, node):
        self.generic_visit(node)
        return node

    def visit_Store(self, node):
        self.generic_visit(node)
        return node

    def visit_Load(self, node):
        self.generic_visit(node)
        return node

    def visit_Del(self, node):
        self.generic_visit(node)
        return node

    def visit_Module(self, node):
        self.generic_visit(node)
        return node

    def visit_Expr(self, node):
        self.generic_visit(node)
        return node

    def visit_Expression(self, node):
        self.generic_visit(node)
        return node

    def visit_BinOp(self, node):
        self.generic_visit(node)
        return node

    def visit_Add(self, node):
        self.generic_visit(node)
        return node

    def visit_Sub(self, node):
        self.generic_visit(node)
        return node

    def visit_Mult(self, node):
        self.generic_visit(node)
        return node

    def visit_Div(self, node):
        self.generic_visit(node)
        return node

    def visit_FloorDiv(self, node):
        self.generic_visit(node)
        return node

    def visit_Pow(self, node):
        self.generic_visit(node)
        return node

    def visit_Mod(self, node):
        self.generic_visit(node)
        return node

    def visit_BoolOp(self, node):
        self.generic_visit(node)
        return node

    def visit_And(self, node):
        self.generic_visit(node)
        return node

    def visit_Or(self, node):
        self.generic_visit(node)
        return node

    def visit_UnaryOp(self, node):
        self.generic_visit(node)
        return node

    def visit_Not(self, node):
        self.generic_visit(node)
        return node

    def visit_Compare(self, node):
        self.generic_visit(node)
        return node

    def visit_Eq(self, node):
        self.generic_visit(node)
        return node

    def visit_NotEq(self, node):
        self.generic_visit(node)
        return node

    def visit_Lt(self, node):
        self.generic_visit(node)
        return node

    def visit_Gt(self, node):
        self.generic_visit(node)
        return node

    def visit_LtE(self, node):
        self.generic_visit(node)
        return node

    def visit_GtE(self, node):
        self.generic_visit(node)
        return node

    def visit_In(self, node):
        self.generic_visit(node)
        return node

    def visit_Is(self, node):
        self.generic_visit(node)
        return node

    def visit_NotIn(self, node):
        self.generic_visit(node)
        return node

    def visit_IsNot(self, node):
        self.generic_visit(node)
        return node

    # True, False, None,
    def visit_NameConstant(self, node):
        self.generic_visit(node)
        return node

    def visit_Call(self, node):
        self.generic_visit(node)
        return node

    def visit_If(self, node):
        self.generic_visit(node)
        return node

    def visit_For(self, node):
        self.generic_visit(node)
        return node

    def visit_While(self, node):
        self.generic_visit(node)
        return node

    def visit_Break(self, node):
        self.generic_visit(node)
        return node

    def visit_Continue(self, node):
        self.generic_visit(node)
        return node

    # a += 1
    def visit_AugAssign(self, node):
        self.generic_visit(node)
        return node

    def visit_List(self, node):
        self.generic_visit(node)
        return node

    def visit_Set(self, node):
        self.generic_visit(node)
        return node

    def visit_Dict(self, node):
        self.generic_visit(node)
        return node

    def visit_Tuple(self, node):
        self.generic_visit(node)
        return node

    def visit_Subscript(self, node):
        self.generic_visit(node)
        return node

    def visit_Index(self, node):
        self.generic_visit(node)
        return node

    def visit_JoinedStr(self, node):
        self.generic_visit(node)
        return node
