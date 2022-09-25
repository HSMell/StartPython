from msilib import MSIMODIFY_INSERT_TEMPORARY


print('hello world'); 
print('Hi 성준 ㅋ'); 
print('ㅋ'); 

firstMoney = 10000;
secondMoney = 20000;

print(firstMoney);
print(secondMoney);

strFirstMoney = str(firstMoney);

print(strFirstMoney);


python = 'PYTHON';

# 문자열 자르기
pythonTest =  python[0];      # 0번째 인덱스 값만 가져옴
print(pythonTest);

# slicing : 원하는 인덱스순서대로 문자를 자를수있음
sliceTest = python[0:3];      # 0번째부터 3번째 직전까지
print(sliceTest);

# 문자열 길이 확인
lengthPython = len(python);
print(lengthPython);

# 대,소문자 변환
hiPython = 'how are You?';
print(hiPython.upper());        # 대문자
print(hiPython.lower());        # 소문자
print(hiPython.capitalize());   # 첫글자만 대문자
print(hiPython.title());        # 각 단어들의 첫글자만 대문자로
print(hiPython.swapcase());     # 각 단어들의 대,소문자들을 뒤바꾼다
print(hiPython.split());        # 문자열을 나눠 리스트형태로 반환
print(hiPython.count('how'));   # how의 개수 

s = '나는개발자';
print(s.startswith('나는'));
print(s.startswith('나도'));

_s = '...나는개발자아님...'
print(s.strip('.'));

print(s.replace('나는','나도'));

print(s + _s); 

# 값 추가
langs = ['파이썬','자바'];
langs.append("C#");
print(langs);

# list 와 tuple이 있는데 tuple은 한번 값을 넣고나면 수정이 불가능하다.
my_list = ['오예스','몽쉘'];
print(my_list);
my_list.append('초코파이');
print(my_list);

my_tuple = ('오예스','몽쉘');      # 읽기 전용의 리스트
print(my_tuple);

#언패킹
#언패킹시 튜플이아니라 리스트형태로 들어감
numbers = (1,2,3,4,5,6,7,8,9,10);
(one,two,*others) = numbers;
print(one);
print(two);
print(others);

# 세트  순서가 보장되지 않음(인덱스 없음)
A = {'돈까스','보쌈','제육덮밥'};
B = {'짬뽕','초밥','제육덮밥'};
print(A.intersection(B));       # 교집합 출력
print(A.union(B));              # 합집합 출력(순서보장하지 않음)
print(A.difference(B));         # 차집합 출력

B.add('닭갈비');
print(B);
B.remove('닭갈비');
print(B);
B.clear();
print(B);
#del B;
# print(B);

# dictinary
dicT = {'이름' : '김형석', '나이' : '29', '키' : '180 '};
_dicT = {'이름' : '김형석', '나이' : 29, '키' : 180 };
print(dicT);
print(dicT['이름']);
print(dicT['나이'] + dicT['키']);
print(int(dicT['나이']) + int(dicT['키']));
print(dicT['키']);

print(_dicT['나이'] + _dicT['키']);
print(str(_dicT['나이']) + str(_dicT['키']));

# dictionary get, add etc
print(dicT.get('이름'));
print(dicT.get('별명'));