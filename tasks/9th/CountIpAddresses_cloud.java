import java.util.Stack;
public class CountIPAddresses {
  public static long ipsBetween(String start, String end) {
    long result = convertLong(end) - convertLong(start);
    if(result < 0){
      throw new IllegalArgumentException();
    }
    return result;
  }
  public static long convertLong(String ip){
    Stack<Integer> stack = new Stack();
    String[] ipArr = ip.split("\\.");
    for(String s: ipArr){
        stack.push(Integer.valueOf(s));
    }
    long n = 1;
    long sum = 0;
    for(int i=0; i<4; i++){
        sum += Long.valueOf(stack.pop() * n);
        n = n * 256;
    }
    return sum;
  }
}
