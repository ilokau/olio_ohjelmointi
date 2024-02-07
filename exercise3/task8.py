class Recording:
    def __init__(self, length: int):
        self.length = length

    def get_length():
        return Recording.length

    def set_length(new_length: int):
        new_length = Recording.length


the_wall = Recording(43)
print(the_wall.length)
the_wall.length = 44
print(the_wall.length)
