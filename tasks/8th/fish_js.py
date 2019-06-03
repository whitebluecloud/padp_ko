def countFish(fish, maxNum_of_fish) :
    return list(filter(lambda x : x > maxNum_of_fish, fish)).count


def solution(A, B):
    upstream_fish = [A[i] for i in range(len(A)) if B[i] == 0]
    downstream_fish = [A[i] for i in range(len(A)) if B[i] == 1]

    return (countFish(upstream_fish, max(downstream_fish))) if max(upstream_fish) > max(downstream_fish) else (
        countFish(downstream_fish, max(upstream_fish)))


print(solution([4, 3, 2, 1, 5], [0, 1, 0, 0, 0]))