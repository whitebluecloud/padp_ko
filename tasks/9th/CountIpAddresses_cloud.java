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
