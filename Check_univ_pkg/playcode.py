from openpyxl import Workbook
import pandas as pd

class Do_univ_check:

    @classmethod
    def kr_univ_read(cls, name):
        df_KR = pd.read_excel(name)
        df_KR_univ_name = df_KR['Eng']
        return df_KR_univ_name

    @classmethod
    def us_univ_read(cls, name):
        df_US = pd.read_excel(name)
        df_US_univ_name = df_US['Full University Name']
        return df_US_univ_name

    @classmethod
    def sum_univ(cls, *name):
        df_f = pd.concat(name)

        t_l = df_f.tolist()

        t_n = []
        for i in t_l:
            temp = i.replace(', ', ',')  
            temp = temp.lower()
            t_n.append(temp)
        return t_n
    
    @classmethod
    def error_check(cls, xlsxname, t_n):          

      workbook = Workbook()                            
      sheet = workbook.active                          
      sheet.title = '(첫번째 시트)'                   


      zzzz = pd.ExcelFile(xlsxname)                    
      sheet_count = len(zzzz.sheet_names)             


      for i in range(sheet_count):                    

          workbook.create_sheet(zzzz.sheet_names[i])      
          sheet = workbook[zzzz.sheet_names[i]]              

          print('\n')
          print('({}/{})'.format(i+1, sheet_count))            
          df =pd.read_excel(xlsxname, sheet_name = i)          

          loc_col=[]
          for i in df.keys():                                 
           if 'Institution' in i:                            
             loc_col.append(i)                               
           if 'Job' in i:                                    
             break


          for i in loc_col:                                  

            for k in range(0,len(df)):                                        
              if ',' in str(df[i][k]):                                         
                if str(df[i][k].lower().replace(', ', ',')) not in t_n:               
                  print('위치: {},{}'.format(i,k))                            
                  print('오류: {}'.format((str(df[i][k].lower().replace(', ', ',')))))
                  sheet.append([i,k,str(df[i][k].lower().replace(', ', ','))])    

      workbook.save('error_{}'.format(xlsxname))


    @classmethod
    def check_start(cls):

      print('작업을 시작합니다.')
      print('"국내대학 모음 파일", "외국대학 모음 파일", "에러를 확인하고 싶은 학과파일"이 저장소에 제대로 업로드 되었는지 확인해주세요.')

      kr_n = input('국내대학파일의 이름을 입력해주세요. : ')
      n_kr_n = input('외국대학파일의 이름을 입력해주세요. : ') 

      df_KR_univ_name = Do_univ_check.kr_univ_read('KR_Univ_2308.xlsx')
      df_US_univ_name = Do_univ_check.us_univ_read('US_Univ_2308.xlsx')

      t_n = Do_univ_check.sum_univ(df_KR_univ_name, df_US_univ_name)
     
      xlsxname = input('학과파일의 이름을 입력해주세요. : ')

      Do_univ_check.error_check(xlsxname, t_n)

      print('완료되었습니다. 오류 모음 파일이 생성되었는지 확인해주세요.')
