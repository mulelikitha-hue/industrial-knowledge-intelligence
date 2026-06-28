import networkx as nx


class KnowledgeGraph:

    def __init__(self):

        self.graph = nx.Graph()

    def add_chunk(self, chunk):

    # -----------------------
    # Document Node
    # -----------------------

        document = chunk["document_name"]

        self.graph.add_node(
            document,
            type="document"
        )

        # -----------------------
        # Chunk Node
        # -----------------------

        chunk_node = f"Chunk_{chunk['chunk_id']}"

        self.graph.add_node(

            chunk_node,

            type="chunk",

             chunk=chunk

        )

        # -----------------------
        # Connect Document -> Chunk
        # -----------------------

        self.graph.add_edge(

            document,

            chunk_node,

            relation="contains"

        )

        # -----------------------
        # Connect Chunk -> Entities
        # -----------------------

        entities = chunk.get("entities", {})

        for entity_type, values in entities.items():

            for value in values:

                self.graph.add_node(

                    value,

                    type=entity_type

                )

                self.graph.add_edge(

                    chunk_node,

                    value,

                    relation="mentions"

                )

                    # -----------------------
                # Connect entities appearing
                # in the same chunk
                # -----------------------

                entity_list = []

                for values in entities.values():

                    entity_list.extend(values)

                for i in range(len(entity_list)):

                    for j in range(i + 1, len(entity_list)):

                        self.graph.add_edge(

                            entity_list[i],

                            entity_list[j],

                            relation="related"

                        )

    def get_neighbors(self, node):

        if node not in self.graph:

            return []

        return list(self.graph.neighbors(node))