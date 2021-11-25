# API 구성

1. localhost:8000/comment/
2. localhost:8000/product/

# API Model

## Product Response Message

| Name        | Type   | Description        |
| ----------- | ------ | ------------------ |
| id          | Number | 제품의 Primary Key |
| comments    | Array  | 제품에 달린 댓글   |
| image       | String | 제품의 대표 사진   |
| avg_rate    | Number | 제품의 별점        |
| name        | String | 제품의 이름        |
| company     | String | 제품의 제조회사    |
| price       | Number | 제품의 가격        |
| category    | String | 제품의 카테고리    |
| description | String | 제품의 상세설명    |
| created_at  | Date   | 데이터 추가 날짜   |
| updated_at  | Date   | 데이터 변경 날짜   |

## Comment Response Message

Comment는 Product와 1:N Foriegn Key 관계를 가집니다.
|Name|Type|Description|
|-|-|-|
|id|Number|댓글의 Primary Key|
|user|String|댓글을 작성한 유저 닉네임|
|comment|String|댓글 내용|
|rate|Number|별점|
|created_at|Date|댓글 추가 날짜|
|product|Number|댓글을 작성한 제품|

# API 필터링

필터링은 product에서만 제공합니다.

## 검색 필터링

    search=[SEARCH VALUE]

검색 필터링은 **필드 필터링**과 동시에 사용해야 합니다.

## 필드 필터링

    search_fields=[FIELD VALUE]

## 정렬

    ordering=[FIELD VALUE]

## API 활용

1. 검색하고자 하는 필드는 2개 이상 선택할 수 있습니다.
2. 다중 검색을 할 때는 **&** 문자를 사용해야 합니다.
3. **-[FIELD VALUE]** 를 사용하여 desc로 정렬할 수 있습니다.

## 예제

    localhost:8000/product/?search=비타민&search_fields=name&search_fields=company&ordering=-price
