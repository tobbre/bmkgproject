class Graph:
	def __init__(self,
				 iri_to_index = {},
				 index_to_iri=[],
				 neighbors=[],
				 triples=[],
				 iri_to_index_predicates={},
				 index_to_iri_predicates=[],
				 n = 0):
		self.iri_to_index = iri_to_index
		self.index_to_iri = index_to_iri
		self.neighbors = neighbors
		self.triples = triples
		self.iri_to_index_predicates = iri_to_index_predicates
		self.index_to_iri_predicates = index_to_iri_predicates
		self.n = len(neighbors)

def read_graph(filepath):
	f = open(filepath, "r")
	lines_temp = f.readlines()
	lines = [line.split("\t")[:3] for line in lines_temp if "\"" not in line]

	iri_to_index = {}
	index_to_iri = []
	neighbors = []
	triples = []
	iri_to_index_predicates = {}
	index_to_iri_predicates = []

	current_index_nodes = 0
	current_index_predicates = 0
	for i in range(len(lines)):
		if lines[i][0] in iri_to_index:
			s_index = iri_to_index[lines[i][0]]
		else:
			iri_to_index[lines[i][0]] = current_index_nodes
			s_index = current_index_nodes
			index_to_iri.append(lines[i][0])
			neighbors.append([])
			current_index_nodes += 1

		if lines[i][2] in iri_to_index:
			o_index = iri_to_index[lines[i][2]]
		else:
			iri_to_index[lines[i][2]] = current_index_nodes
			o_index = current_index_nodes
			index_to_iri.append(lines[i][2])
			neighbors.append([])
			current_index_nodes += 1

		if lines[i][1] in iri_to_index_predicates:
			p_index = iri_to_index_predicates[lines[i][1]]
		else:
			iri_to_index_predicates[lines[i][1]] = current_index_predicates
			p_index = current_index_predicates
			index_to_iri_predicates.append(lines[i][1])
			current_index_predicates += 1

		triples.append([s_index, p_index, o_index])

		neighbors[s_index].append(o_index)
		neighbors[o_index].append(s_index)

	return Graph(iri_to_index, index_to_iri, neighbors, sorted(triples), iri_to_index_predicates, index_to_iri_predicates)

