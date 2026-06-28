def graph_search(question_entities, kg):

    related_chunks = []

    visited = set()

    for entity_list in question_entities.values():

        for entity in entity_list:

            if entity not in kg.graph:
                continue

            neighbors = kg.graph.neighbors(entity)

            for node in neighbors:

                if not str(node).startswith("Chunk_"):
                    continue

                if node in visited:
                    continue

                visited.add(node)

                chunk = kg.graph.nodes[node]["chunk"]

                related_chunks.append(chunk)

    return related_chunks