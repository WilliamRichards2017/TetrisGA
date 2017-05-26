import MultiNEAT as NEAT
import numpy as np
import math
import random
import csv
from Pieces import *
from Board import *

PRINT = False

popSize = 50
maxGeneration = 200
bestIndividuals = 2
width = 10
height = 22

params = NEAT.Parameters()
params.PopulationSize = popSize
params.RouletteWheelSelection = True


params.MutateRemLinkProb = 0.2
params.RecurrentProb = 0
params.OverallMutationRate = 0.50
params.MutateAddLinkProb = 0.2
params.MutateAddNeuronProb = 0.2
params.MutateWeightsProb = 0.90
params.MaxWeight = 8.0
params.WeightMutationMaxPower = 0.2
params.WeightReplacementMaxPower = 1.0

params.MutateActivationAProb = 0.0
params.ActivationAMutationMaxPower = 0.5
params.MinActivationA = 0.05
params.MaxActivationA = 6.0

params.MutateNeuronActivationTypeProb = 0.03

params.ActivationFunction_SignedSigmoid_Prob = 0.0
params.ActivationFunction_UnsignedSigmoid_Prob = 0.0
params.ActivationFunction_Tanh_Prob = 1.0
params.ActivationFunction_TanhCubic_Prob = 0.0
params.ActivationFunction_SignedStep_Prob = 1.0
params.ActivationFunction_UnsignedStep_Prob = 0.0
params.ActivationFunction_SignedGauss_Prob = 1.0
params.ActivationFunction_UnsignedGauss_Prob = 0.0
params.ActivationFunction_Abs_Prob = 0.0
params.ActivationFunction_SignedSine_Prob = 1.0
params.ActivationFunction_UnsignedSine_Prob = 0.0
params.ActivationFunction_Linear_Prob = 1.0

params.DivisionThreshold = 0.5
params.VarianceThreshold = 0.03
params.BandThreshold = 0.3
params.InitialDepth = 2
params.MaxDepth = 3
params.IterationLevel = 1
params.Leo = False
params.GeometrySeed = False
params.LeoSeed = False
params.LeoThreshold = 0.3
params.CPPN_Bias = -1.0
params.Qtree_X = 0.0
params.Qtree_Y = 0.0
params.Width = 1.
params.Height = 1.
params.Elitism = 0.1




'''
Create a genome with 310 inputs and 2 outputs
Inputs consist of
    - Board Configuration: 10 x 22= 220
    - Side Buffer: 88
    - Bias: 1
    - Piece: 1
Outputs are
    - Number of rotations
    - Horizontal displacement
'''
genome = NEAT.Genome(0, 310, 30, 2, False, NEAT.ActivationFunction.UNSIGNED_SIGMOID, NEAT.ActivationFunction.UNSIGNED_SIGMOID, 0, params)

params = NEAT.Parameters()
params.PopulationSize = 20
params.DynamicCompatibility = True






pop = NEAT.Population(genome, params, True, 1.0, 0)
substrate = [((i/width)/height , (i % width)/width, 0.0)  for i in range(width * height)]
piecearray = [(i/25, (i % 5)/5, 1.0)  for i in range(25)]
substrate.extend(piecearray * 4)
substrate = NEAT.Substrate( substrate, [], [((i-7)/7,) for i in range(14)])

def evaluate(genome):
    # create a neural network for the genome
    net = NEAT.NeuralNetwork()
    genome.BuildESHyperNEATPhenotype(net, substrate, params)
    
    # create a board
    board = Board(width, height)
    canAddPiece = 1
    current = 0
    line = 0
    maxPieces = 300
    
    # while the game is not over
    while(current < maxPieces):
        # get a piece
        pieceNum = random.randint(0, 6)
        piece = Piece(pieceNum)
        
        # pass board configuation & piece to the neural network
        conf = board.getBoard().ravel()
        c2, c3, c4, c5 = [piece.getPieceArray(i).ravel() for i in range(4)]
        conf = np.concatenate([conf, c2, c3, c4, c5])
        
        #conf = [tuple(row) for row in conf]
        np.append(conf, pieceNum)
        np.append(conf, 1.0)    # bias
        
        net.Input(conf)
        net.Activate()
        output = net.Output()
        
        if PRINT:
            print "output:", output[0], "outout", output[1]
        ## Found bug, output isnt always between 0 and 1
        col = int(sum(output[0:10]))
        rot = int(sum(output[10:14]))
        print col, rot
        ##print "output1:", output[0], "output2:", output[1]

        # update the board by the output we get
        ##print "rot: ", rot, "col: ", col
        canAddPiece = board.addPiece(piece, rot, col)
        line = line + board.clearRows()
        if canAddPiece == -1:
            #print board
            break
        current += 1
	
	
        
    # evaluate fitness
    #return line
    print "Rows Cleared:", line," Pieces: ", current
    return current
    
def main():
    # for as many as maxGeneration
    for generation in range(50):
        
        # retrieve a list of all genomes in the population
        genome_list = NEAT.GetGenomeList(pop)
        
        # apply the evaluation function to all genomes
        sum = 0
        for genome in genome_list:
            fitness = evaluate(genome)
            genome.SetFitness(fitness)
            sum += fitness
        avg = sum/float(len(genome_list))
        print avg
        # at this point we may output some information regarding the progress of evolution, best fitness, etc.
        # it's also the place to put any code that tracks the progress and saves the best genome or the entire
        # population. We skip all of this in the tutorial.
        
        # advance to the next generation
        pop.Epoch()
        
    # get how-many-ever best guys we want
        
        
if __name__ == "__main__":
    main()