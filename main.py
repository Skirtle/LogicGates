from dataclasses import dataclass
from abc import ABC, abstractmethod

class Gate(ABC):
    
    @abstractmethod
    def compute(self) -> bool | list[bool]: 
        pass