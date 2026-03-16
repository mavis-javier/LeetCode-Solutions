class Solution {
    public int[] twoSum(int[] nums, int target) {
                int index = 0;
        int firstIndex, secondIndex, subtrahend;
        firstIndex = secondIndex = subtrahend = 0;

        ArrayList<Integer> numsList = new ArrayList<>();
        for (int value : nums) {
            numsList.add(value);
        }

        while (index < nums.length) {
            firstIndex = index;
            subtrahend = target - nums[index];
            if (!numsList.contains(subtrahend) || numsList.indexOf(subtrahend) == firstIndex) {
                index++;
                continue;
            }
            secondIndex = numsList.indexOf(subtrahend);
            break;
        }
        int[] result = new int[2];
        result[0] = firstIndex;
        result[1] = secondIndex;
        return result;
    }
}