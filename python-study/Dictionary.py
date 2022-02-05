##<Dictionary란..?>

{Key1:Value1, Key2:Value2, Key3:Value3, ..}
# Key와 Value의 쌍 여러 개가 { }로 둘러싸여 있다. 
# 각각의 요소는 Key : Value 형태로 이루어져 있고 쉼표(,)로 구분되어 있다.


dic = {'이름':'수연', '나이':'22', '키': '157'} #기본형


a = {1: 'hi'}
# Key로 정수 값 1, Value로 문자열도 넣을 수 있다


a = { 'a': [1,2,3]}
# Value에 리스트도 넣을 수 있다






##<Key-Value 쌍 추가>

a = {1: 'a'}
a[2] = 'b'

#{1: 'a'} 딕셔너리에 a[Key2] = 'Value2'와 같이 입력하면

a = {1: 'a', 2: 'b'}

# a에 Key와 Value가 각각 2와 'b'인 2 : 'b'라는 딕셔너리 쌍이 추가된다.





##<Key-Value 쌍 삭제>

family = {'모찌':'수연', '정아':'수경', '아빠':'엄마'}

del family['모찌']

family = {'정아':'수경', '아빠':'엄마'}

#del함수를 사용해서 del a[key]처럼 입력하면, 해당 Key에 해당하는 {key : value} 쌍이 삭제된다.





##<Key를 사용해 Value 얻기>

family = {'모찌':'수연', '정아':'수경', '아빠':'엄마'}

family['모찌']
>> '수연'

family['정아']
>> '수경'

#Dic[Key]로 Value값을 얻을 수 있다


#주의 : Key에는 불특정 값의 집합, 리스트는 사용할 수 없다. Value에는 불특정,특정 값 모두 넣을 수 있다. 



###<DIC함수에 대하여>


#예제) 
fmy = {'모찌':'수연', '정아':'수경', '아빠':'엄마'}



##<DIC함수 1) Key만 모아서 리스트 만들기>


fmy.keys() 


##<DIC함수 2) Value만 모아서 리스트 만들기>


fmy.values() 


##<DIC함수 3) ('Key', 'Value') : 쌍(a:b)을 튜플('a','b')로 묶어 쌍을 얻을 수 있다.>


fmy.items() 


##<DIC함수 4) ( Key : Value ) 쌍 모두 지우기 >


fmy.clear() 


##<DIC함수 5) Key로 Value 얻기 >


fmy.get(Key) 
fmy.get(Key, Default) #찾으려는 Key 값이 없을 경우 미리 정해 둔 디폴트 값을 대신 가져오게 하고 싶을 때


##<DIC함수 5) 해당 Key가 딕셔너리 안에 있는지 조사하기 >

'Key' in fmy

'모찌' in fmy == True!
'곰돌' in fmy == False!
