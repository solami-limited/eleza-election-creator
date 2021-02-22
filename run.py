import os
from csv import DictReader
contestant_template = 'insert into contestants set name="{contname}" ,electionID=5 ,categoryID={catid} ,code="{code}", createdAt=now();\n'
category_template = 'INSERT INTO categories SET name="{catname}" ,electionID=5 ,categoryID={catid} ,code="{code}", createdAt=now();\n'

os.remove("create.sql")
def read_data():
    with open('Elections.csv') as csvfile, open("create.sql","a") as sqlfile:
        reader = DictReader(csvfile, quotechar='"')
        for row in reader:
            info = {
                'catname': row['CATEGORY '].strip(),
                'contname': row['CONTESTANT NAME'].strip(),
                'catid': row['CATEGORYID'].strip(),
                'code': row['CODE'].strip()
            }
            print(info)
            catsql = category_template.format(**info)
            contsql = contestant_template.format(**info)
            sqlfile.write(catsql)
            sqlfile.write(contsql)



if __name__ == "__main__":
    read_data()
