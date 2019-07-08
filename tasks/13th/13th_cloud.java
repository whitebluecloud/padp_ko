import java.util.Arrays;
class Solution {
    public int solution(int distance, int[] rocks, int n) {
        int max = 0;
        int s = 1, e = distance, m = 0;
        Arrays.sort(rocks);
        while (s <= e) {
        	int cnt = 0, prev = 0, min = distance;
        	m =  (s + e) / 2;
        	for(int i = 0; i < rocks.length; i++) {
        		if(rocks[i] - prev <= m ) {
                    cnt++;
                } 
        		else {
        			min = Math.min(min, rocks[i] - prev);
        			prev = rocks[i];
        		}
        	}
        	if(distance - prev <= m) {
                cnt++;
            }else {
                min = Math.min(min, distance - prev);
            } 
        	if(cnt <= n) {
        		max = Math.max(max, min);
        	    s = m + 1;
        	}else{
                e = m - 1;
            }
        }
        return max;
    }
}