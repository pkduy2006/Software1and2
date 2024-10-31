class Publication:
    total_publications = 0

    def __init__(self, name):
        self.name = name
        Publication.total_publications += 1
        self.publication_number = Publication.total_publications

    def print_information(self):
        print(f"{self.publication_number}. Name: {self.name}")

class Book(Publication):
    def __init__(self, name, author_name, page_count):
        self.author_name = author_name
        self.page_count = page_count
        super().__init__(name)

    def print_information(self):
        super().print_information()
        print(f"""Type: Book
Author: {self.author_name}
Page Count: {self.page_count} pages""")

class Magazine(Publication):
    def __init__(self, name, chief_editor):
        self.chief_editor = chief_editor
        super().__init__(name)

    def print_information(self):
        super().print_information()
        print(f"""Type: Magazine
Chief Editor: {self.chief_editor}""")

publications = []
publications.append(Book("Compartment No. 6", "Rosa Liksom", 192))
publications.append(Magazine("Donald Duck", "Aki Hyyppä"))
for p in publications:
    p.print_information()