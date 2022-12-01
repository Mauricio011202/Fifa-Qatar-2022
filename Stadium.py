class Stadium:
    def __init__(self,name,rows,columns,location):
        self.name=name
        self.rows=rows
        self.columns=columns
        self.location=location
    
    
    def register_stadium(self):
        register= self.name+','+str(self.rows)+','+str(self.columns)+','+self.location+'\n'
        return register
    
    