class Interval(object):
    def __init__(self, interval):
        self.interval = interval.copy()

    def __str__(self):
        return str(self.interval)

    def __repr__(self):
        return str(self.interval)

    def start(self):
        return self.interval[0]

    def end(self):
        return self.interval[1]

    def set_start(self, value):
        self.interval[0] = value

    def set_end(self, value):
        self.interval[1] = value


class Stack(object):
    def __init__(self):
        self.stack = []

    def __str__(self):
        return str(self.stack)

    def __repr__(self):
        return str(self.stack)

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def sort(self):
        self.stack.sort(key=lambda x: x.start())


def time_mon(intervals):
    intervals = [Interval(i) for i in sorted(intervals)]
    stack = Stack()
    stack.push(intervals[0])
    for interval in intervals[1:]:
        top = stack.peek()
        if top.end() < interval.start():
            stack.push(interval)
        elif top.end() < interval.end():
            top.set_end(interval.end())
            stack.pop()
            stack.push(top)
    total_time = 0
    for time in stack.stack:
        total_time += time.end() - time.start()
    return total_time
