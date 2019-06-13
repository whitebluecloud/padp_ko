import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class fish_js {
    public int solution(int[] A, int[] B) {
        List<Integer> upstream_fish = new ArrayList<>();
        List<Integer> downstream_fish = new ArrayList<>();

        // 먼저 상류와 하류를 분류 (방향)
        for(int i=0; i<A.length; i++){
            if(B[i] == 0) upstream_fish.add(A[i]);
            if(B[i] == 1) downstream_fish.add(A[i]);
        }

        return Collections.max(upstream_fish) > Collections.max(downstream_fish) ? countFish(upstream_fish, Collections.max(downstream_fish))
                : countFish(downstream_fish, Collections.max(upstream_fish));
    }
    // 상류와 하류의 max값을 추출하여, 더 적은 쪽의 물고기와 필터를 걸어서 살아남은 물고기 수를 출력함
    public int countFish(List<Integer> fish, int maxNum_of_fish) {
        return (int) fish.stream()
                .filter(num -> num > maxNum_of_fish).count();
    }
}
