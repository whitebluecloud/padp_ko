package codility;

import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.*;

public class FiboFrogTest {

    private FiboFrog frog;

    @Before
    public void frogCreate(){
        frog = new FiboFrog();
    }

    @Test
    public void noJump() {
        assertEquals(-1, frog.solution(null));
    }

    @Test
    public void sampleTest(){
        // f(5) = 5, f(3) = 2, f(5) = 5 return 3
        int[] a = {0,0,0,1,1,0,1,0,0,0,0};
        assertEquals(3, frog.solution(a));
    }

    @Test
    public void oneJump(){
        assertEquals(1, frog.solution(new int[]{}));
        assertEquals(1, frog.solution(new int[]{0})); // 2
        assertEquals(1, frog.solution(new int[]{0,0})); // 3
        assertEquals(1, frog.solution(new int[]{0,0,0,0})); // 5
        assertEquals(1, frog.solution(new int[]{1,1,1,1})); // 5
        assertEquals(1, frog.solution(new int[]{1})); // 1 , 1
        assertEquals(1, frog.solution(new int[]{0,1})); // 2, 1
    }

    @Test
    public void twoJump(){
        assertEquals(2, frog.solution(new int[]{0,0,1})); // 3, 1
        assertEquals(2, frog.solution(new int[]{0,0,1,1,1})); // 3, 3
        assertEquals(2, frog.solution(new int[]{0,0,1,0,1})); // 3, 3
    }

    @Test
    public void threeJump(){
        assertEquals(3, frog.solution(new int[]{0,0,1,0,0,1})); // 3, 3, 1
    }
}