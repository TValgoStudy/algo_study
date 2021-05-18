# 자료구조와 알고리즘을 통한 버전관리 연습

여러 자료구조와 알고리즘 파이썬 파일을 만들고 공동관리하면서 발전사항을 수정한 뒤에 git repository에 올린다.



## 방법

1. 최신 버전을 다운 받는다.

```bash
git pull origin 고동진
```

2. 변경할 파일의 branch를 생성한다.

```bash
git switch -c feature/file_or_function
// or
git branch // ??
git switch feature/file_or_function
```

3. 수정사항을 add commit 후에 git repository에 push한다.

   (pr 하면서 상세사항을 작성하거나 bash에서 작성 명령어 추가바람)

```bash
git add
git commit -m "create, first, fixed, modified, 더 기재 바람"
git push origin feature/file_or_function
```

4. PR을 한뒤 여러 merge 상황을 살펴보고 case 별로 정리를 한다.
5. merge가 끝나면 git pull을 받아 버전을 일치시켜준다.

```bash
git pull origin 고동진
```

6. feature/file_or_function branch가 고동진에 반영됬으므로 branch를 제거한다.

```bash
git branch -d feature/file_or_function
```



## 충돌사항(confilcts)과 해결 과정 정리(git merge)

### Case

1.  부모 branch를 pull 받지 않고 local에서 자식 branch를 삭제하려고 하면 경고를 보내준다.

   ```bash
   git branch -D feature/file_or_function
   ```

   `-d` 말고 `-D` 옵션을 주면 강제 삭제가 가능하다.

2.  

3. 