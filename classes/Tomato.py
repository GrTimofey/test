class Tomato:
    status = {0: 'nothing', 1: 'flower', 2: 'green_tomato', 3: 'red_tomato'}

    def __init__(self, index):
        self._index = index
        self._tomato_stat = 0

    def grow(self):
        self._change_state()

    def is_ripe(self):
        if self.status == 3:
            return True
        return False

    def _change_state(self):
        if self._tomato_stat < 3:
            self._tomato_stat += 1
        self._print_state()

    def _print_state(self):
        print(f'Tomato: {self._index}, Status: {Tomato.status[self._tomato_stat]}')
