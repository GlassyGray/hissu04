# First
- Github first commit

## process 
1. ```git init``` 
- 해당 폴더를 깃 래퍼지토리로 만든다
2. ```git config --global user.email [email address]```
- 깃 유저 등록
3. ```git add READNE.md```
- 파일 변경 사항을 추적
4. ```git commit (-m "한 줄만 간단히 적을때")```
- 커밋
5. ```git remote add origin [url]```
- 리모트 레퍼지토리 주소 등록
6. ```git config credential.helper store```
- 자격증명 캐싱 활성화
7. ```git push -u origin master```
- 최초 푸쉬 후 다음 푸쉬부터 ```git push``` 

## 소감
- ``` 왜 써야하는지 모르겠다```
```cpp
std::vector<string>::iterator a = someStringVector;
for(auto& iString : a){ 
    std::cout<<iString<<std::endl;
}
```
- 아직 실감이 안남