# Generated from Orka.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .OrkaParser import OrkaParser
else:
    from OrkaParser import OrkaParser

# This class defines a complete listener for a parse tree produced by OrkaParser.
class OrkaListener(ParseTreeListener):

    # Enter a parse tree produced by OrkaParser#program.
    def enterProgram(self, ctx:OrkaParser.ProgramContext):
        pass

    # Exit a parse tree produced by OrkaParser#program.
    def exitProgram(self, ctx:OrkaParser.ProgramContext):
        pass


    # Enter a parse tree produced by OrkaParser#decl.
    def enterDecl(self, ctx:OrkaParser.DeclContext):
        pass

    # Exit a parse tree produced by OrkaParser#decl.
    def exitDecl(self, ctx:OrkaParser.DeclContext):
        pass


    # Enter a parse tree produced by OrkaParser#declarlist.
    def enterDeclarlist(self, ctx:OrkaParser.DeclarlistContext):
        pass

    # Exit a parse tree produced by OrkaParser#declarlist.
    def exitDeclarlist(self, ctx:OrkaParser.DeclarlistContext):
        pass


    # Enter a parse tree produced by OrkaParser#identlist.
    def enterIdentlist(self, ctx:OrkaParser.IdentlistContext):
        pass

    # Exit a parse tree produced by OrkaParser#identlist.
    def exitIdentlist(self, ctx:OrkaParser.IdentlistContext):
        pass


    # Enter a parse tree produced by OrkaParser#type.
    def enterType(self, ctx:OrkaParser.TypeContext):
        pass

    # Exit a parse tree produced by OrkaParser#type.
    def exitType(self, ctx:OrkaParser.TypeContext):
        pass


    # Enter a parse tree produced by OrkaParser#runsection.
    def enterRunsection(self, ctx:OrkaParser.RunsectionContext):
        pass

    # Exit a parse tree produced by OrkaParser#runsection.
    def exitRunsection(self, ctx:OrkaParser.RunsectionContext):
        pass


    # Enter a parse tree produced by OrkaParser#actionsequence.
    def enterActionsequence(self, ctx:OrkaParser.ActionsequenceContext):
        pass

    # Exit a parse tree produced by OrkaParser#actionsequence.
    def exitActionsequence(self, ctx:OrkaParser.ActionsequenceContext):
        pass


    # Enter a parse tree produced by OrkaParser#command.
    def enterCommand(self, ctx:OrkaParser.CommandContext):
        pass

    # Exit a parse tree produced by OrkaParser#command.
    def exitCommand(self, ctx:OrkaParser.CommandContext):
        pass


    # Enter a parse tree produced by OrkaParser#input.
    def enterInput(self, ctx:OrkaParser.InputContext):
        pass

    # Exit a parse tree produced by OrkaParser#input.
    def exitInput(self, ctx:OrkaParser.InputContext):
        pass


    # Enter a parse tree produced by OrkaParser#output.
    def enterOutput(self, ctx:OrkaParser.OutputContext):
        pass

    # Exit a parse tree produced by OrkaParser#output.
    def exitOutput(self, ctx:OrkaParser.OutputContext):
        pass


    # Enter a parse tree produced by OrkaParser#const.
    def enterConst(self, ctx:OrkaParser.ConstContext):
        pass

    # Exit a parse tree produced by OrkaParser#const.
    def exitConst(self, ctx:OrkaParser.ConstContext):
        pass


    # Enter a parse tree produced by OrkaParser#boolconst.
    def enterBoolconst(self, ctx:OrkaParser.BoolconstContext):
        pass

    # Exit a parse tree produced by OrkaParser#boolconst.
    def exitBoolconst(self, ctx:OrkaParser.BoolconstContext):
        pass


    # Enter a parse tree produced by OrkaParser#intnumb.
    def enterIntnumb(self, ctx:OrkaParser.IntnumbContext):
        pass

    # Exit a parse tree produced by OrkaParser#intnumb.
    def exitIntnumb(self, ctx:OrkaParser.IntnumbContext):
        pass


    # Enter a parse tree produced by OrkaParser#realnumb.
    def enterRealnumb(self, ctx:OrkaParser.RealnumbContext):
        pass

    # Exit a parse tree produced by OrkaParser#realnumb.
    def exitRealnumb(self, ctx:OrkaParser.RealnumbContext):
        pass


    # Enter a parse tree produced by OrkaParser#sign.
    def enterSign(self, ctx:OrkaParser.SignContext):
        pass

    # Exit a parse tree produced by OrkaParser#sign.
    def exitSign(self, ctx:OrkaParser.SignContext):
        pass


    # Enter a parse tree produced by OrkaParser#assign.
    def enterAssign(self, ctx:OrkaParser.AssignContext):
        pass

    # Exit a parse tree produced by OrkaParser#assign.
    def exitAssign(self, ctx:OrkaParser.AssignContext):
        pass


    # Enter a parse tree produced by OrkaParser#expression.
    def enterExpression(self, ctx:OrkaParser.ExpressionContext):
        pass

    # Exit a parse tree produced by OrkaParser#expression.
    def exitExpression(self, ctx:OrkaParser.ExpressionContext):
        pass


    # Enter a parse tree produced by OrkaParser#arithmexpr.
    def enterArithmexpr(self, ctx:OrkaParser.ArithmexprContext):
        pass

    # Exit a parse tree produced by OrkaParser#arithmexpr.
    def exitArithmexpr(self, ctx:OrkaParser.ArithmexprContext):
        pass


    # Enter a parse tree produced by OrkaParser#term.
    def enterTerm(self, ctx:OrkaParser.TermContext):
        pass

    # Exit a parse tree produced by OrkaParser#term.
    def exitTerm(self, ctx:OrkaParser.TermContext):
        pass


    # Enter a parse tree produced by OrkaParser#factor.
    def enterFactor(self, ctx:OrkaParser.FactorContext):
        pass

    # Exit a parse tree produced by OrkaParser#factor.
    def exitFactor(self, ctx:OrkaParser.FactorContext):
        pass


    # Enter a parse tree produced by OrkaParser#base.
    def enterBase(self, ctx:OrkaParser.BaseContext):
        pass

    # Exit a parse tree produced by OrkaParser#base.
    def exitBase(self, ctx:OrkaParser.BaseContext):
        pass


    # Enter a parse tree produced by OrkaParser#boolexpr.
    def enterBoolexpr(self, ctx:OrkaParser.BoolexprContext):
        pass

    # Exit a parse tree produced by OrkaParser#boolexpr.
    def exitBoolexpr(self, ctx:OrkaParser.BoolexprContext):
        pass


    # Enter a parse tree produced by OrkaParser#logicalexpr.
    def enterLogicalexpr(self, ctx:OrkaParser.LogicalexprContext):
        pass

    # Exit a parse tree produced by OrkaParser#logicalexpr.
    def exitLogicalexpr(self, ctx:OrkaParser.LogicalexprContext):
        pass


    # Enter a parse tree produced by OrkaParser#logicalterm.
    def enterLogicalterm(self, ctx:OrkaParser.LogicaltermContext):
        pass

    # Exit a parse tree produced by OrkaParser#logicalterm.
    def exitLogicalterm(self, ctx:OrkaParser.LogicaltermContext):
        pass


    # Enter a parse tree produced by OrkaParser#logicalmultiplier.
    def enterLogicalmultiplier(self, ctx:OrkaParser.LogicalmultiplierContext):
        pass

    # Exit a parse tree produced by OrkaParser#logicalmultiplier.
    def exitLogicalmultiplier(self, ctx:OrkaParser.LogicalmultiplierContext):
        pass


    # Enter a parse tree produced by OrkaParser#logicalrel.
    def enterLogicalrel(self, ctx:OrkaParser.LogicalrelContext):
        pass

    # Exit a parse tree produced by OrkaParser#logicalrel.
    def exitLogicalrel(self, ctx:OrkaParser.LogicalrelContext):
        pass


    # Enter a parse tree produced by OrkaParser#ifstatement.
    def enterIfstatement(self, ctx:OrkaParser.IfstatementContext):
        pass

    # Exit a parse tree produced by OrkaParser#ifstatement.
    def exitIfstatement(self, ctx:OrkaParser.IfstatementContext):
        pass


    # Enter a parse tree produced by OrkaParser#doblock.
    def enterDoblock(self, ctx:OrkaParser.DoblockContext):
        pass

    # Exit a parse tree produced by OrkaParser#doblock.
    def exitDoblock(self, ctx:OrkaParser.DoblockContext):
        pass


    # Enter a parse tree produced by OrkaParser#whilestatement.
    def enterWhilestatement(self, ctx:OrkaParser.WhilestatementContext):
        pass

    # Exit a parse tree produced by OrkaParser#whilestatement.
    def exitWhilestatement(self, ctx:OrkaParser.WhilestatementContext):
        pass


    # Enter a parse tree produced by OrkaParser#forstatement.
    def enterForstatement(self, ctx:OrkaParser.ForstatementContext):
        pass

    # Exit a parse tree produced by OrkaParser#forstatement.
    def exitForstatement(self, ctx:OrkaParser.ForstatementContext):
        pass


    # Enter a parse tree produced by OrkaParser#switchstatement.
    def enterSwitchstatement(self, ctx:OrkaParser.SwitchstatementContext):
        pass

    # Exit a parse tree produced by OrkaParser#switchstatement.
    def exitSwitchstatement(self, ctx:OrkaParser.SwitchstatementContext):
        pass


    # Enter a parse tree produced by OrkaParser#caselist.
    def enterCaselist(self, ctx:OrkaParser.CaselistContext):
        pass

    # Exit a parse tree produced by OrkaParser#caselist.
    def exitCaselist(self, ctx:OrkaParser.CaselistContext):
        pass


    # Enter a parse tree produced by OrkaParser#relop.
    def enterRelop(self, ctx:OrkaParser.RelopContext):
        pass

    # Exit a parse tree produced by OrkaParser#relop.
    def exitRelop(self, ctx:OrkaParser.RelopContext):
        pass



del OrkaParser