# Final_Project

## 일정

* 월 
  	* 프론트: ~~파비콘~~,~~계정연동~~ 
    	  	* 백:~~영화정보 50개 이상 받아서 데이터베이스 만들기~~	
* 화 
  * 댓글 수정
  * ~~이미지 깨끗하게~~
  * ~~폰트 바꾸기~~
  * ~~영화 관객수 순위로 정렬~~
  * ~~평점 등록할때 무한대로 입력되는거 바꾸기~~
  * 
* 수
  * ~~데이터가 계속 들어옴 루트 경로로 갈때마다 start함수가 딱 한번만 실행되게, 어차피 11.16기준으로 오니까  json파일로 만들어도 상관없을듯....~~
  * ~~댓글 수정~~
  * ~~추천 영화? 어떻게 띄울까 - 좋아요 상위 3개 순으로~~
  * 꾸미기
    * 유저정보
    * 상세페이지
    * 전체 테마
* 목
  * 프론트:
  * 백:
  * 최종합쳐서 완성본 만들기/ 서비스 배포
* 금

## 막히는점

* ~~영화50개의 정보를 json파일로 만들어야하는지 그냥 데이터베이스에 두어도 상관 없는지??~~
  * ~~json파일로 만들기로 결정~~
* ~~왜 이미지가 흐릴까??~~

## 구현할것

* 전체적인 테마 꾸미기

* 추천 영화 띄우기

* ~~파비콘~~
* ~~네이버, 카카오 계정 연동~~
* 페이지네이션

json파일 만들기, 로드시키기



```
python manage.py dumpdata app.Post --indent 4 > post.json
python manage.py loaddata post.json
```