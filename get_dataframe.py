class Mwaa_Redshift_Connect:
    def __init__(self, REDSHIFT_ID, REDSHIFT_PW):
        self.REDSHIFT_ID = REDSHIFT_ID # 레드시프트 아이디
        self.REDSHIFT_PW = REDSHIFT_PW # 레드시프트 비밀번호
        
    def redshift_sql(self,sql):
        if sql == None or sql == '':
            return False
        import redshift_connector
        conn = redshift_connector.connect(
            host='레드시프트 주소',
            database='데이터베이스 명',
            user=self.REDSHIFT_ID,
            password=self.REDSHIFT_PW,
            auto_create=True
        )
        cursor: redshift_connector.Cursor = conn.cursor()
        cursor.execute(sql)
        return conn.commit()
    
    def redshift_sql_result(self,sql,type):
        if sql == None or sql == '':
            return False
        import redshift_connector
        import pandas as pd
        conn = redshift_connector.connect(
            host='레드시프트 주소',
            database='데이터베이스 명',
            user=self.REDSHIFT_ID,
            password=self.REDSHIFT_PW,
            auto_create=True
        )
        cursor: redshift_connector.Cursor = conn.cursor()
        cursor.execute( sql )
        if type == 'tuple' :
            result: tuple = cursor.fetchall()
        elif type == 'dict' :
            result: dict = cursor.fetchall()
        elif type == 'dataframe':
            result: pd.DataFrame = cursor.fetch_dataframe()
        else :
            result = None
        return result
    
