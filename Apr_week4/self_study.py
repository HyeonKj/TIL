''' 2022. 04. 26. 
# 크롤링

# 셀레니움을 활용해 크롤링 할 때 클릭이 되지 않는 문제점. 

<a href = 'http://test.test'> 테스트입니다 </a>
- a 태그의 href 속성값에 링크가 바로 나와있는 경우는 
 '''

# browser = webdriver.Chrome()
# sample = browser.find_element_by_css_select('a')
# sample.click()
'''
"위와 같은  click() 명령에 바로 링크로 접속할 수 있습니다. 

하지만 아래 처럼, 링크가 아닌 자바스크립트가 들어가있는 경우에는
'''
# <a href = '#', onclick = 기타명령어> 테스트2 </a>
'''
제대로 선택하여 click() 명령을 하더라도  href 속성 값에 url 주소가 제대로 들어가있지 않기 때문에 

해당 주소로 들어갈 수가 없어요. 

이럴때에는, onlclick 내부의 명령어가 실행되도록 해야 합니다. 

'''
# # 첫번째 방법
# sample = browser.find_element_by_css_select('a')
# sample.send_keys('\n')    # 해당 링크/명령어 에  엔터 를 실행하도록

# # 두 번째 방법
# sample = browser.find_element_by_css_select('a')
# browser.execute_script("arguments[0].click();", sample)  #자바 명령어 실행
'''
첫 번째 방법은  해당 링크/명령어 위치에서  '\n' 을 입력하여  엔터를 입력하는 것과 동일한 효과를 가지게 하는 것이며, 

두 번째 방법은 자바스크립트 명령어를 이용하여,  스크립트를 실행하라는 것이에요. 

※ arguments 는 두 개의 파라미터를 가지게 되며  arguments[0] 가 해당 스크립트를 지정한다. 
'''

list1 = [[1, 10], [2, 22], [3, 19], [4, 7]]
list2 = [data for inner_list in list1 for data in inner_list]
print(list2)

'''[output] [1, 10, 2, 22, 3, 19, 4, 7]'''

