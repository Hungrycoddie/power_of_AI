Read the memory area off the PLCs in the the current network.
       
        Parameters
        ----------
        start : int
            The starting memory address to read from.
        count : int
            The number of memory areas to read from.
        type : str
            The data type of the memory areas to read.
            Must be one of:
                'bit'
                'int'
                'real'
                'float'
                'double'
                'dword'
                'word'
                'long'
                'short'
                
        Returns
        -------
        data : list
            A list of the data read from the memory areas.
        """
        return self._read_memory(start, count, type)
        
    def write_memory(self, address, value, type='bit'):
        """Write the memory area to the PLCs in the current network.
       
        Parameters
        ----------
        address : int
            The memory address to write to.
        value : list
            The value to write to the memory address.
        type : str
            The data type of the memory area to write.
            Must be one of:
                'bit'
                'int'
                'real'
                'float'
                'double'
                'dword'
                'word'
                'long'
                'short'
        """
        self._write_memory(address, value, type)
        
    def read_memory_area(self, area, start, count):
        """Read the memory area off the PLCs in the the current network.
       
        Parameters
        ----------
        area : str
            The memory area to read from.
            Must be one of:
                'input'
                'output'
                'memory'
                'db'
                'vmemory'
                'vdb'
        start : int
            The starting memory address to read from.
        count : int
            The number of memory areas to read from.
        
        Returns
        -------
        data : list
            A list of the data read from the memory areas.
        """
        return self._read_memory_area(area, start, count)
        
    def write_memory_area(self, area, address, value):
        """Write the memory area to the PLCs in the current network.
       
        Parameters
        ----------
        area : str
            The memory area to write to.
            Must be one of:
                'input'
                'output'
                'memory'
                'db'
                'vmemory'
                'vdb'
        address : int
            The memory address to write to.
        value : list
            The value to write to the memory address.
        """
        self._write_memory_area(area, address, value)
    
    def read_memory_area_bit(self, area, start, count):
        """Read the memory area off the PLCs in the the current network.
       
        Parameters
        ----------
        area : str
            The memory area to read from.
            Must be one of:
                'input'
                'output'
                'memory'
                'db'
                'vmemory'
                'vdb'
        start : int
            The starting memory address to read from.
        count : int
            The number of memory areas to read from.
        
        Returns
        -------
        data : list
            A list of the data read from the memory areas.
        """
        return self._read_memory_area_bit(area, start, count)
        
    def write_memory_area_bit(self, area, address, value):
        """Write the memory area to the PLCs in the current network.
       
        Parameters
        ----------
        area : str
            The memory area to write to.
            Must be one of:
                'input'
                'output'
                'memory'
                'db'
                'vmemory'
                'vdb'
        address : int
            The memory address to write to.
        value : list
            The value to write to the memory address.
        """
        self._write_memory_area(area, address, value)
        
    def read_memory_area_int(self, area, start, count):
        """Read the memory area off the PLCs in the the current network.
       
        Parameters
        ----------
        area : str
            The memory area to read from.
            Must be one of:
                'input'
                'output'
                'memory'
                'db'
                'vmemory'
                'vdb'
        start : int
            The starting memory address to read from.
        count : int
            The number of memory areas to read from.
        
        Returns
        -------
        data : list
            A list of the data read from the memory areas.
        """
        return self._read_memory_area_int(area, start, count)
        
    def write_memory_area_int(self, area, address, value):
        """Write the memory area to the PLCs in the current network.
       
        Parameters
        ----------
        area : str
            The memory area to write to.
            Must be one of:
                'input'
                'output'
                'memory'
                'db'
                'vmemory'
                'vdb'
        address : int
            The memory address to write to.
        value : list
            The value to write to the memory address.
        """
        self._write_memory_area(area, address, value)
        
    def read_memory_area_word(self, area, start, count):
        """Read the memory area off the PLCs in the the current network.
       
        Parameters
        ----------
        area : str
            The memory area to read from.
            Must be one of:
                'input'
                'output'
                'memory'
                'db'
                'vmemory'
                'vdb'
        start : int
            The starting memory address to read from.
        count : int
            The number of memory areas to read from.
        
        Returns
        -------
        data : list
            A list of the data read from the memory areas.
        """
        return self._read_memory_area_word(area, start, count)
        
    def write_memory_area_word(self, area, address, value):
        """Write the memory area to the PLCs in the current network.
       
        Parameters
        ----------
        area : str
            The memory area to write to.
            Must be one of:
                'input'
                'output'
                'memory'
                'db'
                'vmemory'
                'vdb'
        address : int
            The memory address to write to.
        value : list
            The value to write to the memory address.
        """
        self._write_memory_area(area, address, value)
        
    def read_memory_area_short(self, area, start, count):
        """Read the memory area off the PLCs in the the current network.
       
        Parameters
        ----------
        area : str
            The memory area to read from.
            Must be one of:
                'input'
                'output'
                'memory'
                'db'
                'vmemory'
                'vdb'
        start : int
            The starting memory address to read from.
        count : int
            The number of memory areas to read from.
        
        Returns
        -------
        data : list
            A list of the data read from the memory areas.
        """
        return self._read_memory_area_short(area, start, count)
        
    def write_memory_area_short(self, area, address, value):
        """Write the memory area to the PLCs in the current network.
       
        Parameters
        ----------
        area : str
            The memory area to write to.
            Must be one of:
                'input'
                'output'
                'memory'
                'db'
                'vmemory'
                'vdb'
        address : int
            The memory address to write to.
        value : list
            The value to write to the memory address.
        """
        self._write_memory_area(area, address, value)
        
    def read_memory_area_long(self, area, start, count):
        """Read the memory area off the PLCs in the the current network.
       
        Parameters
        ----------
        area : str
            The memory area to read from.
            Must be one of:
                'input'
                'output'
                'memory'
                'db'
               