# API 구성

1. localhost:8000/comment/
2. localhost:8000/product/

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

    localhost:8000/product/search=비타민&search_fields=name&search_fields=company&ordering-price
