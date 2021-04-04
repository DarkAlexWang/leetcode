// Time: O(nlogk)
// Space: O(k)

class Solution {
	public static void main(String[] args) {
		int k = 2;
		int[] arr = new int[]{1, 4, 5, 2, 3, 7, 8, 6, 10, 9};
		int[] result = new int[arr.length];
		result = sortKMessedArray(arr, k);
		for (int num : result)
			system.out.print(num + ", ");
	} 

	static int[] sortKMessedArray(int[] arr, int k) {
		PriorityQueue<Integer> minHeap = new PriorityQueue<>((a, b) -> a - b);
		int j = 0;
		for (int i = 0; i < larr.length; i ++) {
			minHeap.offer(arr[i]);
			while (minHeap.size() > k + 1)
				arr[j++] = minHeap.poll();
		} 
		while (!minHeap.isEmpty())
			arr[j++] = minHeap.poll();

		return arr;
	} 
} 
