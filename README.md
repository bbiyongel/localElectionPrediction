# 지방선거 결과 예측 프로젝트 (2018.03-2018.06)

## 제안

* 프로젝트 진행 시기가 지방선거 기간이라 관련 뉴스 데이터를 모아 자주 언급된 단어로 선거 결과를 예측할 수 있다면 재밌을 것 같아서 진행
* Naver Search Open API, Python Beautiful Soup4 웹크롤러로 데이터 수집
* 수업시간에 배웠던 기초 스파크 프로그래밍으로 단어 빈도수 체크하는 워드 카운팅 프로그램으로 결과 출력

---

## 설계

![01](https://github.com/younggeun0/localElectionPrediction/blob/master/result/01.png?raw=true)

1. Web Crawler
2. Word Count
3. Render Graph 

* 세 개의 코드가 결과물
* Naver API 이용, '선거'에 관련된 데이터를 요청해서 받아 BS4로 파싱, 텍스트 파일로 저장. (5월 31일부터 6월 13일까지 수집)
* 스파크를 사용 텍스트 데이터를 토큰으로 분할, 키/값 페어 RDD로 매핑, reduceByKey로 동일 키값 데이터들의 합을 구하고, 내림차순으로 정렬, 결과를 텍스트 파일로 출력
* 스파크 결과로 matplotlib이용 바그래프 출력

---

## 최종결과

![renderGraph](https://github.com/younggeun0/localElectionPrediction/blob/master/result/render_graph_result.png?raw=true)

![onRaspberryPi](https://github.com/younggeun0/localElectionPrediction/blob/master/result/result_on_raspberryPi.png?raw=true)

![result01](https://github.com/younggeun0/localElectionPrediction/blob/master/result/result01.png?raw=true)

* 먼저 요약하면 많이 언급됐다고 항상 좋은 결과가 나타나지 않았음
    * 안좋은 사건들로 이슈가 될 수 있다는 점들을 간과
    * 바미당은 당명 언급순위 3위, 안철수 후보는 김문수 후보보다 많이 언급됐음에도 결과에 영향을 미치지 못했음
* 순서대로 1,2위인 더민주, 자한당은 시도지사, 구시군의장 분포에서 각각 1,2위의 결과를 보임

![result02](https://github.com/younggeun0/localElectionPrediction/blob/master/result/result02.png?raw=true)

![result03](https://github.com/younggeun0/localElectionPrediction/blob/master/result/result03.JPG?raw=true)

