import argparse
import sys
import os
import time
import numpy as np
import mmap


class ShuffleCSV:

    def __init__(self, input_file, header = True, batch_size = 1000):
        self.input_file = input_file
        self.header = header
        self.batch_size = batch_size


    def shuffle_csv(self):    

        with open(self.input_file, mode="r", encoding = "ISO-8859-1") as file_obj:
            with mmap.mmap(file_obj.fileno(), length=0, access=mmap.ACCESS_READ) as file_map:

                lines = file_map.read().decode("ISO-8859-1").splitlines()
                
                if self.header:
                    header = lines[0]
                                
                                
                lines = lines[1:]

                
                if self.batch_size <= len(lines):
                    self.batch_size = len(lines)

                np.random.shuffle(lines)

        with open(self.input_file, 'w') as f:
            
            f.write(header + '\n')

            for batch in range(0, len(lines), self.batch_size):                
                f.write('\n'.join([line for line in lines[batch: batch + self.batch_size]]))

        return len(lines)      