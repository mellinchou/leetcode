class TwoSum {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        
        for (int i=0; i<nums.length;i++){ //loop once through the input array
            int complement = target - nums[i]; //find the complement number for the current array element
            if (map.containsKey(complement)){ //if the map contains the complement, meaning that the current i and complement sums up to target
                return new int[] {map.get(complement),i}; //return current i and the complement's index
            }
            map.put(nums[i],i);//put the current i and its value into the hash table
        }
        throw new IllegalArgumentException("No two sum solution");
    }
    
}