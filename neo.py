from py2neo import neo4j


class Neo():
    def __init__(self):
        self.db = neo4j.GraphDatabaseService("http://localhost:7474/db/data/")
        self.eden = []

    def populate(self):
        self.db.clear()
        self.eden = self.db.create(
            {"name": "Adam"},
            {"name": "Eve"},
            (0, "RIB", 1)
        )

    def eve(self):
        if self.eden:
            return list(self.db.match(end_node=self.eden[1]))

if __name__ == "__main__":
    neo = Neo()
    neo.populate()
