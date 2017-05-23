import MultiNEAT as NEAT
import numpy as np
import math
import random
from Pieces import *
from Board import *

popSize = 50
maxGeneration = 200
bestIndividuals = 2
width = 10
height = 22

params = NEAT.Parameters()
params.PopulationSize = popSize
params.RouletteWheelSelection = True

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
genome = NEAT.Genome(0, 223, 30, 2, False, NEAT.ActivationFunction.UNSIGNED_SIGMOID, NEAT.ActivationFunction.UNSIGNED_SIGMOID, 0, params)

params.DynamicCompatibility = True
params.CompatTreshold = 2.0
params.YoungAgeTreshold = 15
params.SpeciesMaxStagnation = 100
params.OldAgeTreshold = 35
params.MinSpecies = 5
params.MaxSpecies = 10
params.RouletteWheelSelection = False

params.MutateRemLinkProb = 0.02
params.RecurrentProb = 0
params.OverallMutationRate = 0.15
params.MutateAddLinkProb = 0.08
params.MutateAddNeuronProb = 0.01
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


pop = NEAT.Population(genome, params, True, 1.0, 0)

def evaluate(genome):
    # create a neural network for the genome
    net = NEAT.NeuralNetwork()
    genome.BuildPhenotype(net)
    
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
        np.append(conf, pieceNum)
        np.append(conf, 1.0)    # bias
        
        net.Input(conf)
        net.Activate()
        output = net.Output()
        
        col = int(math.ceil(output[0] * 9 + 2))
        rot = int(math.ceil(output[1] * 3))

        # update the board by the output we get
        print "rot: ", rot, "col: ", col
        canAddPiece = board.addPiece(piece, rot, col)
        line = line + board.clearRows()
        if canAddPiece == -1:
            break
        current += 1
        
    print "Rows Cleard:", line," Pieces: ", current
        
    # evaluate fitness
    #return line
    return current
    
def main():
    # for as many as maxGeneration
    for generation in range(1):
        
        # retrieve a list of all genomes in the population
        genome_list = NEAT.GetGenomeList(pop)
        
        # apply the evaluation function to all genomes
        sum = 0.0
        for genome in genome_list:
            fitness = evaluate(genome)
            genome.SetFitness(fitness)
            sum += fitness
        avg = sum/popSize
        print avg
        # at this point we may output some information regarding the progress of evolution, best fitness, etc.
        # it's also the place to put any code that tracks the progress and saves the best genome or the entire
        # population. We skip all of this in the tutorial.
        
        # advance to the next generation
        pop.Epoch()
        
    # get how-many-ever best guys we want
        
        
if __name__ == "__main__":
    main()