data = Mwaa_Redshift_Connect('아이디','비밀번호') # 자기아이디랑 비번 # class라서 변수명 선언이 필요함

sql = """ """ # 쿼리

df = data.redshift_sql_result(sql,'dataframe')
