class Solution {
    public int carFleet(int target, int[] position, int[] speed) {
        int n = position.length;
        double[] arrivalTimes = new double[n];
        Stack<Double> stack = new Stack<>();
        
        for (int i = 0; i < n; i++) {
            // y = mx + b
            // x = (y - b) / m
            
            double y = target;
            double m = speed[i];
            double b = position[i];
            
            double x = (y - b) / m;
            
            arrivalTimes[i] = x;
        }
        
        for (double num : arrivalTimes) {
            System.out.println(num);
        }
        
        // array of arrays of size 2 position : arrivalTime
        double[][] cars = new double[n][2];
        
        for (int i = 0; i < n; i++) {
            cars[i][0] = position[i];
            cars[i][1] = arrivalTimes[i];
        }
        
        // sort cars by position
        Arrays.sort(cars, Comparator.comparingDouble(c -> c[0]));
        
        for (double[] car : cars) {
            System.out.println(car[0] + " " + car[1]);
        }
        
        // add arrivalTimes to stack from position closest to target
        for (int i = n - 1; i >= 0; i--) {
            double arrivalTime = cars[i][1];
            
            if (!stack.isEmpty() && arrivalTime <= stack.peek()) {
                continue;
            }
            
            stack.push(arrivalTime);
        }
        
        System.out.println(stack);
                
        return stack.size();
    }
}