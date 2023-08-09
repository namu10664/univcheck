# univcheck
## 이 모듈은 정식 명칭이 적힌 대학파일들 기준으로, 조사한 학과 파일에서 명칭이 정확한지 확인하는 것을 도와줍니다.

 준비: "국내대학 모음 파일", "외국대학 모음 파일", "에러를 확인하고 싶은 학과파일"이 필요합니다. 
 
 (위치가 /content/univcheck/ 일 것!)
 
 (모든 파일은 엑셀 파일 입니다.)
 
 ( "국내대학 모음 파일"은 'Eng'열에 이름들이 저장돼있어야 합니다. )
 
 ( "외국대학 모음 파일"은 'Full University Name'열에 이름들이 저장돼있어야 합니다. )
 
 ( "에러를 확인하고 싶은 학과파일"은 'Institution'열에 이름들이 저장돼있어야 합니다.)
 
 ( 설치 방법: !git clone https://github.com/namu10664/univcheck.git )
 
 ( 위치 이동: %cd /content/univcheck/ )

 사용방법: 
 
 모듈을 설치하고 univcheck파일로 이동 한 후,

 ( openpyxl모듈이 없다면, 입력창에서 !pip install openpyxl 를 실행해주세요. )
 
 입력창에 !python main.py 을 입력하세요.


>아래 코드를 실행하면 됨
>
>>!git clone https://github.com/namu10664/univcheck.git
>>
>>%cd /content/univcheck/
>>
>>!pip install openpyxl 
>>
>>!python main.py

변경사항1. job 이전까지를 보려했지만 이제는 job과 상관없이 모든 'Institution'을 확인함

변경사항2. if문에서 이름을 걸러낼 때, ','가 없는지를 묻고, 아닐 때 넘어갔지만 이제는 ',' 개수가 2개 이상일 때 넘어가도록 변경함
