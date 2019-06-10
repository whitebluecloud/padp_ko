import java.util.Stack;
public class CountIPAddresses {

    public static long ipsBetween(String start, String end) {

        Stack<Integer> stack = new Stack();

        String[] startArr = start.split("\\.");
        for(String s: startArr){
            stack.push(Integer.valueOf(s));
        }
        long n = 1;
        long startSum = 0;
        for(int i=0; i<4; i++){
            startSum += Long.valueOf(stack.pop() * n);
            n = n * 256;
        }

        String[] endArr = end.split("\\.");
        for(String s: endArr){
            stack.push(Integer.valueOf(s));
        }
        n = 1;
        long endSum = 0;
        for(int i=0; i<4; i++){
            endSum += Long.valueOf(stack.pop() * n);
            n = n * 256;
        }
        long result = endSum - startSum;

        if(result < 0){
            throw new IllegalArgumentException();
        }

        return result;
    }
}

// test class
import static org.junit.Assert.assertEquals;

import codewars.CountIPAddresses;
import com.sun.org.apache.xpath.internal.functions.WrongNumberArgsException;
import org.junit.Test;

public class CountIPAddressesTest {

    @Test
    public void normalTest() throws Exception {
        assertEquals( 50, CountIPAddresses.ipsBetween( "10.0.0.0", "10.0.0.50" ) );
        assertEquals( 246, CountIPAddresses.ipsBetween( "20.0.0.10", "20.0.1.0" ) );
    }

    @Test(expected = NumberFormatException.class)
    public void paramIsNumber() throws Exception {
        CountIPAddresses.ipsBetween( "a", "b" );
    }

    @Test(expected = IllegalArgumentException.class)
    public void endIsBigger() throws Exception {
        CountIPAddresses.ipsBetween( "0.0.0.1", "0.0.0.0" );
    }
}