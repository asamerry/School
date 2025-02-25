from django.shortcuts import render
import ast

# Create your views here.


def textbooks(request):

    with open(__file__, 'r', encoding='utf8') as file:
        tree = ast.parse(file.read(), filename=__file__)
    function_count = sum(isinstance(node, ast.FunctionDef) for node in ast.walk(tree))

    return render(request, 'textbooks/textbooks.html', {
        'books': function_count - 1,
    })


def linearalgebradoneright(request):
    return render(request, 'textbooks/linearalgebradoneright.html')

def elementaryanalysis(request):
    return render(request, 'textbooks/elementaryanalysis.html')

def bookofproof(request):
    return render(request, 'textbooks/bookofproof.html')

def dynamicalsystemstheory(request):
    return render(request, 'textbooks/dynamicalsystemstheory.html')

def linearalgebradonewrong(request):
    return render(request, 'textbooks/linearalgebradonewrong.html')

def mathematicalstatisticsandapplications(request):
    return render(request, 'textbooks/mathematicalstatisticsandapplications.html')

def realanalysis(request):
    return render(request, 'textbooks/realanalysis.html')

def partialdifferentialequations(request):
    return render(request, 'textbooks/partialdifferentialequations.html')

def linearalgebraanditsapplications(request):
    return render(request, 'textbooks/linearalgebraanditsapplications.html')

def introductiontostatisticallearning(request):
    return render(request, 'textbooks/introductiontostatisticallearning.html')

def introductiontomathematicalstructuresandproofs(request):
    return render(request, 'textbooks/introductiontomathematicalstructuresandproofs.html')

def abookofabstractalgebra(request):
    return render(request, 'textbooks/abookofabstractalgebra.html')

def handsonmachinelearning(request):
    return render(request, 'textbooks/handsonmachinelearning.html')

def numericalanalysis(request):
    return render(request, 'textbooks/numericalanalysis.html')

def diffeqsdynsyslinalg(request):
    return render(request, 'textbooks/diffeqsdynsyslinalg.html')

def appliedlinearregression(request):
    return render(request, 'textbooks/appliedlinearregression.html')

def linearmodelswithr(request):
    return render(request, 'textbooks/linearmodelswithr.html')

def introductiontostochasticprocesseswithr(request):
    return render(request, 'textbooks/introductiontostochasticprocesseswithr.html')

def introductiontotimeseriesandforecasting(request):
    return render(request, 'textbooks/introductiontotimeseriesandforecasting.html')

def timeseriesanalysisanditsapplicationswithr(request):
    return render(request, 'textbooks/timeseriesanalysisanditsapplicationswithr.html')

def derivativesmarkets(request):
    return render(request, 'textbooks/derivativesmarkets.html')

def introductiontoprobabilitymodels(request):
    return render(request, 'textbooks/introductiontoprobabilitymodels.html')

def lossmodelsfromdatatodecisions(request):
    return render(request, 'textbooks/lossmodelsfromdatatodecisions.html')

def introductiontodatamining(request):
    return render(request, 'textbooks/introductiontodatamining.html')

def mathematicalinteresttheory(request):
    return render(request, 'textbooks/mathematicalinteresttheory.html')

def mathematicsofinvestmentandcredit(request):
    return render(request, 'textbooks/mathematicsofinvestmentandcredit.html')

def stigumsmoneymarket(request):
    return render(request, 'textbooks/stigumsmoneymarket.html')

def optionsmarkets(request):
    return render(request, 'textbooks/optionsmarkets.html')

def matrixanalysis(request):
    return render(request, 'textbooks/matrixanalysis.html')

def calculus(request):
    return render(request, 'textbooks/calculus.html')

def intermediatemicroeconomics(request):
    return render(request, 'textbooks/intermediatemicroeconomics.html')

def introductiontoprobability(request):
    return render(request, "textbooks/introductiontoprobability.html")

def introductoryeconometrics(request):
    return render(request, "textbooks/introductoryeconometrics.html")

def introtoeconometrics(request):
    return render(request, "textbooks/introtoeconometrics.html")

def masteringmetrics(request): 
    return render(request, "textbooks/masteringmetrics.html")

def anintroductiontomeasuretheory(request):
    return render(request, "textbooks/anintroductiontomeasuretheory.html")

def designandanalysisofexperiments(request):
    return render(request, "textbooks/designandanalysisofexperiments.html")

def advancedcalculus(request):
    return render(request, "textbooks/advancedcalculus.html")

def advancedcalculusofseveralvariables(request):
        return render(request, "textbooks/advancedcalculusofseveralvariables.html")

def divgradcurlandallthat(request):
        return render(request, "textbooks/divgradcurlandallthat.html")

def functionsofmanycomplexvariables(request):
    return render(request, "textbooks/functionsofmanycomplexvariables.html")

def vectorcalculuslinearalgebraanddifferentialforms(request):
    return render(request, "textbooks/vectorcalculuslinearalgebraanddifferentialforms.html")

def introductoryrealanalysis(request):
    return render(request, "textbooks/introductoryrealanalysis.html")

def contempabstractalgebra(request):
    return render(request, "textbooks/contempabstractalgebra.html")\

def anintrotoprobandstats(request):
    return render(request, "textbooks/anintrotoprobandstats.html")

def extendingthelinearmodel(request):
    return render(request, "textbooks/extendingthelinearmodel.html")

def problemsolvingwithalgorithmsanddatastructures(request):
    return render(request, "textbooks/problemsolvingwithalgorithmsanddatastructures.html")

def hyperbolicgeometry(request):
    return render(request, "textbooks/hyperbolicgeometry.html")

def principlesofmathematicalanalysis(request):
    return render(request, "textbooks/principlesofmathematicalanalysis.html")

def introductoryphysics1(request):
    return render(request, "textbooks/introductoryphysics1.html")

def introductoryphysics2(request):
    return render(request, "textbooks/introductoryphysics2.html")

def fundamentalsofphysics(request):
    return render(request, "textbooks/fundamentalsofphysics.html")

def intrototopology(request):
    return render(request, "textbooks/intrototopology.html")

def measureintegrationandrealanalysis(request):
    return render(request, "textbooks/measureintegrationandrealanalysis.html")

def realandcomplexanalysis(request):
    return render(request, "textbooks/realandcomplexanalysis.html")

def largescaleconvexoptimization(request):
    return render(request, "textbooks/largescaleconvexoptimization.html")

def problemsolvingwithcpp(request):
    return render(request, "textbooks/problemsolvingwithcpp.html")

def roydenanalysis(request):
    return render(request, "textbooks/roydenanalysis.html")

def datastructuresandotherobjects(request):
    return render(request, "textbooks/datastructuresandotherobjects.html")

def operatingsystems(request):
    return render(request, "textbooks/operatingsystems.html")

def effectivemoderncpp(request):
    return render(request, "textbooks/effectivemoderncpp.html")

def datastructuresandalgorithmanalysis(request):
    return render(request, "textbooks/datastructuresandalgorithmanalysis.html")

def algorithms(request):
    return render(request, "textbooks/algorithms.html")

def artificialintelligenceamodernapproach(request):
    return render(request, "textbooks/artificialintelligenceamodernapproach.html")

def machinelearningtheartandscienceofalgorithms(request):
    return render(request, "textbooks/machinelearningtheartandscienceofalgorithms.html")

def proofsandrefutations(request):
    return render(request, "textbooks/proofsandrefutations.html")

def theartandcraftofproblemsolving(request):
    return render(request, "textbooks/theartandcraftofproblemsolving.html")

def anintroductiontooptimization(request):
    return render(request, "textbooks/anintroductiontooptimization.html")

def numbertheoryrevealed(request):
    return render(request, "textbooks/numbertheoryrevealed.html")

def anintroductiontothetheoryofnumbers(request):
    return render(request, "textbooks/anintroductiontothetheoryofnumbers.html")

def progit(request):
    return render(request, "textbooks/progit.html")

def theoryofneuralcomputation(request):
    return render(request, "textbooks/theoryofneuralcomputation.html")

def complexanalysis(request): 
    return render(request, "textbooks/complexanalysis.html")