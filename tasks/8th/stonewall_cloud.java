package codility;
import static org.junit.Assert.*;
import org.junit.Test;

import java.util.Stack;

public class stack_stone_wall {

    public int solution(int[] H) {

        if(H.length == 0) return 0;

        int cnt = 0;
        Stack<Integer> stack = new Stack<Integer>();

        for(int h: H){
            if(stack.empty() || stack.peek() < h){
                stack.push(h);
                cnt++;
                continue;
            }

            while(!stack.empty() && stack.peek() > h) {
                stack.pop();
            }
            if(stack.empty() || stack.peek() < h){
                stack.push(h);
                cnt++;
            }
        }

        return cnt;
    }

    @Test
    public void test() {
        System.out.println("stack_stone_wall_test start");

        assertEquals(solution(new int[]{8}), 1);
        assertEquals(solution(new int[]{8,8}), 1);
        assertEquals(solution(new int[]{8,8,5}), 2);
        assertEquals(solution(new int[]{8,8,5,7}), 3);
        assertEquals(solution(new int[]{8,8,5,7,9}), 4);
        assertEquals(solution(new int[]{8,8,5,7,9,8}), 5);
        assertEquals(solution(new int[]{8,8,5,7,9,8,7}), 5);
        assertEquals(solution(new int[]{8,8,5,7,9,8,7,4}), 6);
        assertEquals(solution(new int[]{8,8,5,7,9,8,7,4,8}), 7);

        System.out.println("stack_stone_wall_test end");
    }


}
