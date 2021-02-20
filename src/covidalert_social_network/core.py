import EoN

class CovidAlertSocialNetwork:
    def __init__(self, graph, tau, gamma):
        self.G = graph
        self.tau = tau
        self.gamma = gamma
        self.R0 = tau / gamma
    
    def calculate_infected_nodes(self):
        infected_nodes = EoN.get_infected_nodes(self.G, 
            self.tau, self.gamma, initial_infecteds=self.initial_infected_nodes)

        return infected_nodes
    
    def calculate_infection_probability(self, node, n_iter=1000):
        cont = 0
        available_nodes_for_infection = list(self.G.nodes)
        available_nodes_for_infection.pop(available_nodes_for_infection.index(node))

        for _ in range(n_iter):
            infected_nodes = self.calculate_infected_nodes()

            if node in infected_nodes:
                cont += 1
        
        infection_probability = cont / n_iter

        return infection_probability
