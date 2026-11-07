from torch.utils.data import Dataset, Subset
from torch import tensor
import numpy as np

from random import shuffle as randShuffle

class NumberDataset(Dataset):
    def __init__(self, start: int = 0, end: int = 9, shuffle: bool = True):
        super().__init__()
        self.operations = []
        self.results = []
        for i in range(start, end):
            for j in range(start, end):
                for op in ["+", "-", "*", "/"]:
                    if(op == "/" and j == 0):
                        continue

                    self.operations.append(str(i) + op + str(j))
                    if (op == "+"):
                        self.results.append(str(int(i+j)))
                    elif (op == "-"):
                        if(j > i):
                            self.results.append('0')
                        else:
                            self.results.append(str(int(i-j)))
                    elif (op == "*"):
                        self.results.append(str(int(i*j)))
                    else:
                        self.results.append(str(int(i/j)))

        
        if(shuffle):
            indices = []
            for i in range(len(self.operations)):
                indices.append(i)
            randShuffle(indices)

            shuffled_operations = []
            shuffled_results = []

            for i in indices:
                shuffled_operations.append(self.operations[i])
                shuffled_results.append(self.results[i])
            
            self.operations = shuffled_operations
            self.results = shuffled_results

    def __len__(self) -> int:
        return(len(self.operations))

    def __getitem__(self, index:int) -> Any:
        operation = list(self.operations[index])

        for idx in range(len(operation)):
            operation[idx] = float(ord(operation[idx]))
        operation = tensor(operation)
        
        result = self.results[index]

        if(len(result) == 1):
            result = '0' + result
        else:
            result = result[:2]
            
        result = list(result)
    
        for idx in range(len(result)):
            result[idx] = float(ord(result[idx]))
        result = tensor(result)

        sample = {}

        sample["operation"] = operation
        sample["result"] = result

        return sample