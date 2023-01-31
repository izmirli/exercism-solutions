"""Circular Buffer.

About circular buffer:
https://en.wikipedia.org/wiki/Circular_buffer
"""


class BufferFullException(BufferError):
    """Exception raised when CircularBuffer is full.

    message: explanation of the error.
    """
    def __init__(self, message):
        self.message = message


class BufferEmptyException(BufferError):
    """Exception raised when CircularBuffer is empty.

    message: explanation of the error.
    """
    def __init__(self, message):
        self.message = message


class CircularBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = [None] * self.capacity
        self.read_pointer = 0
        self.write_pointer = 0

    def read(self):
        if self.buffer[self.read_pointer] is None:
            raise BufferEmptyException('Circular buffer is empty')
        data, self.buffer[self.read_pointer] = self.buffer[self.read_pointer], None
        self.read_pointer = (self.read_pointer + 1) % self.capacity
        return data

    def write(self, data, overwrite=False):
        if self.buffer[self.write_pointer] is not None:
            if overwrite:
                self.read_pointer = (self.read_pointer + 1) % self.capacity
            else:
                raise BufferFullException('Circular buffer is full')
        self.buffer[self.write_pointer] = data
        self.write_pointer = (self.write_pointer + 1) % self.capacity

    def overwrite(self, data):
        self.write(data, True)

    def clear(self):
        self.buffer = [None] * self.capacity
        self.read_pointer = 0
        self.write_pointer = 0
