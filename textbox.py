
class Textbox:
    def __init__(self, lines, width=None, padding=0):
        self.width = width or max([len(line) for line in lines]) + 2
        self.padding = padding
        self.inner_width = self.width - 2 + padding

        self.lines = lines        
        if type(lines[0]) == str:
            self.lines = [self.lines]

    def _render_top_line(self):
        return '/' + '-' * self.inner_width + '\\' + '\n'

    def _render_bottom_line(self):
        return '\\' + '-' * self.inner_width + '/' + '\n'

    def _render_line(self, line):
        return '|' + line.ljust(self.inner_width) + '|'

    def _render_lines(self):
        return '\n'.join([self._render_line(line) for line in self.lines]) + '\n'

    def render(self):
        res = ''
        res += self._render_top_line()
        res += self._render_lines()
        res += self._render_bottom_line()
        return res
        
if __name__ == '__main__':
    t = Textbox(['hello', 'this is dog', 'who are you'], width=50)
    print(t.render())