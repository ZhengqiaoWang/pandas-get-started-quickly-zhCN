import pandas as pd
import sqlite3

# 创建数据
conn = sqlite3.connect(':memory:')
query = """
CREATE TABLE TABLE1(
    CLASS_ID VARCHAR(20),
    CLASS_NAME VARCHAR(20),
    EXCHANGE_ID VARCHAR(10),
    VALUE1 INTEGER,
    VALUE2 FLOAT
);
"""
conn.execute(query)
conn.commit()

data = [
    ('AP', '苹果', 'ZCE', 1, 100.2),
    ('pb', '铅', 'SFE', 2, 32.12),
    ('rb', '螺纹钢', 'SFE', 3, 132),
    ('SM', '锰硅', 'ZCE', 4, -42.12),
]
statement = "INSERT INTO TABLE1 VALUES(?,?,?,?,?)"
conn.executemany(statement, data)
conn.commit()

cursor = conn.execute("SELECT * FROM TABLE1")
#返回结果集中的所有行
rows = cursor.fetchall()
print(rows)

df = pd.read_sql('SELECT * FROM TABLE1', conn)
print(df)
