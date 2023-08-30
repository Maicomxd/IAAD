import sqlite3
class Banco:
    def __init__(self):
        self._con = sqlite3.connect('hospital.db')
        self.banco = self._con.cursor()
        #print(self.get_all('''pacient', pacient_id, race'''))
        self.create_tables()
        
    def create_tables(self):
        self.create_table('illness', 'code INT PRIMARY KEY, description, severity_description TEXT, risk_mortality TEXT, medical_surgical TEXT')

        self.create_table('hospital', 'id INT PRIMARY KEY, hospital_name TEXT NOT NULL, service_area TEXT NOT NULL, county TEXT NOT NULL')

        self.create_table('pacient', '''
        pacient_id INT AUTO_INCREMENT PRIMARY KEY, age int NOT NULL, gender TEXT, race TEXT, 
        ethnicity TEXT, stay int NOT NULL, admission TEXT, disposition TEXT, 
        code INT, hospital_id INT NOT NULL, costs REAL NOT NULL,
        FOREIGN KEY(code) REFERENCES illeness(code),
        FOREIGN KEY(hospital_id) REFERENCES hospital(id)
        ''') 


    def create_table(self, table: str, fields: str):
        self.banco.execute(f'CREATE TABLE IF NOT EXISTS {table}({fields})')
    
    def insert(self, table: str, values):
        fields = ''
        if(table.lower() == 'pacient'): 
            fields = '''(pacient_id, age, gender, race, ethnicity, stay,
            admission, disposition, costs, code, hospital_id)'''
        elif(table.lower() == 'hospital'): 
            fields = '''(id, hospital_name, service_area, county)'''
        elif(table.lower() == 'illness'): 
            fields = '''(code, description, severity_description, risk_mortality, medical_surgical)'''
        
        self.banco.execute(f'''
        INSERT INTO {table}{fields} 
        Values{values}
        ''') 
    
    def delete(self, table: str, fields: str):
        self.banco.execute(f'DELETE FROM {table} WHERE ({fields})')
    
    
        
    def get_all(self, table: str, fields='*'):
        #return self.banco.execute(f'SELECT {fields} FROM {table}')
        for x in self.banco.execute(f'SELECT {fields} FROM {table}'):
            print(x)

        return ''

banco = Banco()

test = [
(0, 'descri;ao do primeiro', 'white', 'baixo', 'Mode'),
(1, 'oit', 'black', 'auto', 'extreme'),
]
for x in test:
    print(banco.insert('illness', x))

test = [
(0, 'alberto aistem', 'igarassu', 'pernambuco'),
(1, 'portugues', 'paulista', 'sao paulo'),
]
for x in test:
    print(banco.insert('hospital', x))

test = [
(0, 15, 'm', 'white', 'brazileiro', 15, 'extreme', 'dead', 1554.54, 0, 1),
(1, 15, 'm', 'white', 'brazileiro', 15, 'extreme', 'dead', 1554.54, 1, 0),
(2, 15, 'm', 'white', 'brazileiro', 15, 'extreme', 'dead', 1554.54, 0, 1), 
(3, 15, 'm', 'white', 'brazileiro', 15, 'extreme', 'dead', 1554.54, 0, 1), 
(4, 15, 'm', 'white', 'brazileiro', 15, 'extreme', 'dead', 1554.54, 1, 0),
]
for x in test:
    print(banco.insert('pacient', x))

print(banco.get_all('pacient', 'pacient_id, race'))