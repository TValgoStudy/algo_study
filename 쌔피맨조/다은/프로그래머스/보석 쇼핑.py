def solution(gems):
    n = len(gems)
    gems_cnt = len(set(gems))
    result = 9999999999
    s, e = 0, 0

    # gem 종류 하나 선택해서 index 리스트
    gem_index = []
    for i in range(n):
        if gems[i] == gems[0]:
            gem_index.append(i)

    # 특정 gem index만 검사
    for i in gem_index:
        # 빈 dict 만들고
        gems_dict = {}
        for j in range(i, n):
            gem = gems[j]
            gems_dict[gem] = gems_dict.get(gem, 0) + 1
            # dict 길이 세서어서 gems 종류 수이면 조건 만족
            if len(gems_dict) == gems_cnt:
                # 맨 뒤는 괜찮고
                # 맨 앞 검사하면서 해당 gem 개수가 1 이상이면 
                # 안 쪽에 포함되어 있다는 거니까 맨 앞을 제외 
                while True:
                    gem_check = gems[i]
                    if gems_dict[gem_check] > 1:
                        gems_dict[gem_check] -= 1
                        i += 1
                    else:
                        break
                # result 길이, start, end 갱신
                if result > j - i + 1:
                    result = j - i + 1
                    s, e = i, j
                break

    return [s + 1, e + 1]


gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
print(solution(gems))

# 오답
# ["DIA", "EM", "EM", "RUB", "DIA"] => 답 [3, 5]