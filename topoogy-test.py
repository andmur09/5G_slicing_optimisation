# -*- coding: utf-8 -*-
from topology_class import location, link, makeLink, topology
import optimisation

def main():
    # Makes the locations in the datacenter
    locations = []
    locations.append(location("Gateway", "gateway"))
    locations.append(location("Spine1", "switch"))
    locations.append(location("Leaf1", "switch"))
    locations.append(location("Leaf2", "switch"))
    locations.append(location("Node1", "node", resources={"cpu": float(4), "ram": float(8)}))
    locations.append(location("Node2", "node", resources={"cpu": float(2), "ram": float(16)}))

    # Makes the links between locations in the datacenter
    links = []
    links += makeLink(locations[0], locations[1], {"bandwidth": float(10), "latency": float(1)})
    links += makeLink(locations[1], locations[2], {"bandwidth": float(5), "latency": float(1)})
    links += makeLink(locations[1], locations[3], {"bandwidth": float(5), "latency": float(1)})
    links += makeLink(locations[2], locations[3], {"bandwidth": float(5), "latency": float(1)})
    links += makeLink(locations[2], locations[4], {"bandwidth": float(5), "latency": float(1)})
    links += makeLink(locations[2], locations[5], {"bandwidth": float(5), "latency": float(1)})
    links += makeLink(locations[3], locations[4], {"bandwidth": float(5), "latency": float(1)})
    links += makeLink(locations[3], locations[5], {"bandwidth": float(5), "latency": float(1)})
    
    # Creates then plots topology and saves to file
    problem = topology("trial1", locations, links)
    # gateway = problem.getGateway()
    # problem.addArtificialSource(gateway)
    # problem.addArtificialSink(gateway)
    
    #problem.print()

    # Define source and sink for optimisation
    # _from = problem.getLocationByDescription("Gateway")
    # _to = problem.getLocationByDescription("Node1")
    # result = optimisation.minCostFlow(problem, stops)
    
    # # Defines source/sink pairs for each flow
    gateway = problem.getLocationByDescription("Gateway")
    node = problem.getLocationByDescription("Node1")
    segments = [(gateway, node), (node, gateway)]

    result = optimisation.minCostFlowWithStops(problem, segments, plot=True)
    
if __name__ == "__main__":
    main()


