####################################################################################
### Author : Rokas Stanislovas
###
### GSoC 2016 project: Cortical Networks
####################################################################################

###########  Main settings  ########################################################

ref =                   "Figure2_cNoESS"

simConfig=              "TempSimConfig"

simDuration =           1000 # ms                                ##
simDt =                 0.025 # ms
neuroConstructSeed =    133243                                      ##

simulator =             None   ### "jNeuroML_NEURON"

defaultSynapticDelay =  0.05 

scaleCortex =             0.5                             ##
scaleThalamus =           0                              ##

gabaScaling =             1.25                           ##

l4ssAmpaScaling =         1                           ##

inNrtTcrNmdaScaling =    0.2
pyrSsNmdaScaling =       2.5

deepBiasCurrent =         -1 

from RunColumn import *

RunColumnSimulation(net_id=ref,
                    nml2_source_dir="../../../neuroConstruct/generatedNeuroML2/",
                    sim_config=simConfig,
                    scale_cortex=scaleCortex,
                    scale_thalamus=scaleThalamus,
                    default_synaptic_delay=defaultSynapticDelay,
                    gaba_scaling=gabaScaling,
                    l4ss_ampa_scaling=l4ssAmpaScaling,
	            in_nrt_tcr_nmda_scaling=inNrtTcrNmdaScaling,
	            pyr_ss_nmda_scaling=pyrSsNmdaScaling,
	            deep_bias_current=deepBiasCurrent,
                    which_models='all',
                    dir_nml2="../../",
                    duration=simDuration,
                    dt=simDt,
                    max_memory='1000M',
                    seed=neuroConstructSeed,
                    simulator=simulator)
