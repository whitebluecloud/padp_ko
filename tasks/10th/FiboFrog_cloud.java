package codility;

import java.util.*;

public class FiboFrog {

    public int solution(int[] A) {

        if(A == null) return -1;
        int len = A.length;
        if(len == 0) return 1;

        List<Integer> jumpMap = getJumpMap(len);
        Collections.reverse(jumpMap);

        // bfs
        Queue<Node> queue = new LinkedList<>();
        queue.add(new Node(-1, 0));
        while(!queue.isEmpty()){

            Node currentNode = queue.poll();
            for(int i=0; i< jumpMap.size(); i++){
                int curPos = currentNode.pos + jumpMap.get(i);

                if(curPos == A.length){
                    return currentNode.jumpCnt + 1;
                }
                if(curPos < 0 || curPos > A.length || A[curPos] == 0){
                    continue;
                }

                int jumpCnt = currentNode.jumpCnt + 1;
                queue.add(new Node(curPos, jumpCnt));
                A[curPos] = 0;
            }
        }

        return -1;
    }

    public List<Integer> getJumpMap(int len){
        ArrayList<Integer> jumpMap = new ArrayList<>();
        jumpMap.add(0);
        jumpMap.add(1);

        while(true){
            int prev1 = jumpMap.get(jumpMap.size() - 1);
            int prev2 = jumpMap.get(jumpMap.size() - 2);
            int next = prev1 + prev2;
            jumpMap.add(next);

            if(prev1 + prev2 > len){
                break;
            }
        }
        return jumpMap;
    }

    public class Node {
        int pos;
        int jumpCnt;

        public Node(int pos, int jumpCnt){
            this.pos = pos;
            this.jumpCnt = jumpCnt;
        }
    }
}