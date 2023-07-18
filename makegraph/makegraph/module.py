from colorama import init, Fore

init()

def _color(text, color):
    return f'{color}{text}{Fore.WHITE}'

class Graph:
    def __init__(self, data):
        self.data = data

    def show(self):
        graph_data = [round(num) for num in self.data]
        data_length = len(graph_data)
        last_value = graph_data[0]

        x = len(graph_data)
        y = max(graph_data)
        graph_structure = [[0 for _ in range(x)] for _ in range(y)]

        for i in range(data_length):
            if last_value > graph_data[i]:
                for j in range(graph_data[i], last_value):
                    graph_structure[y - (1 + j)][i] = 3
            elif last_value < graph_data[i]:
                for j in range(last_value, graph_data[i]):
                    graph_structure[y - (1 + j)][i] = 2
            else:
                graph_structure[y - (1 + graph_data[i])][i] = 1

            last_value = graph_data[i]

        for ln in graph_structure:
            newln = ''
            for chr in ln:
                if chr == 0:
                    newln += ' '
                elif chr == 1:
                    newln += _color('.', Fore.YELLOW)
                elif chr == 2:
                    newln += _color('.', Fore.GREEN)
                elif chr == 3:
                    newln += _color('.', Fore.RED)
            print(newln)