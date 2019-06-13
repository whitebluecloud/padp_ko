import java.util.*;

class Solution {
    public int solution(int[] A, int[] B) {

        int alive = 0;
        Stack downFishes = new Stack();

        int aLen = A.length;
        int bLen = B.length;

        // 내려오는 물고기
        for(int i=0; i<aLen; i++){
            if(B[i] == 0){ // 올라오는 물고기
                alive++;

                if(downFishes.empty()){
                    continue;
                }

                while(true){
                    alive--;

                    if(A[i] < (int)downFishes.peek()){
                        break;
                    }else{
                        downFishes.pop();
                        if(downFishes.empty()){
                            break;
                        }
                    }
                }

            }else{ // 내려오는 물고기
                downFishes.push(A[i]);
                alive++;
            }
        }

        return alive;
    }
}