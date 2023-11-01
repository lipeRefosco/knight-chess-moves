class knight:
    
    @staticmethod
    def move_up_right(x):
        return x - 8 * 2 + 1

    @staticmethod
    def move_up_left(x):
        return x - 8 * 2 - 1
    
    @staticmethod
    def move_right_up(x):
        return x - 8 * 1 + 2

    @staticmethod
    def move_left_up(x):
        return x - 8 * 1 - 2

    @staticmethod
    def move_down_right(x):
        return x + 8 * 2 + 1

    @staticmethod
    def move_down_left(x):
        return x + 8 * 2 - 1

    @staticmethod
    def move_right_down(x):
        return x + 8 * 1 + 2

    @staticmethod
    def move_left_down(x):
        return x + 8 * 1 - 2