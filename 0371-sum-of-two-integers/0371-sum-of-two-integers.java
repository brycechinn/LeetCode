class Solution {
    public int getSum(int a, int b) {
        // approach: (Java) (a XOR b) XOR ((a & b) << 1 )
        
        while (b != 0) {
            int tmp = (a & b) << 1;
            a = a ^ b;
            b = tmp;
        }
        
        return a;
    }
}