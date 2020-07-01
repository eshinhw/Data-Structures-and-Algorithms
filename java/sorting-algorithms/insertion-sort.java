
public class InsertionSort {
	
	public void insertionSort (int[] arr) {
		
		int temp;
		
		for (int i=0; i < arr.length - 1; i++) {
			int j = i;
			
			while (arr[j] > arr[j+1]) {
				temp = arr[j];
				arr[j] = arr[j+1];
				arr[j+1] = temp;
				j--;
			}
		}
		
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		InsertionSort is = new InsertionSort();
		
		
		int[] nums = {1, 10, 5, 8, 7, 6, 4, 3, 2, 9};
		
		for (int i: nums)
			System.out.println(i);
		
		System.out.println("=====");
		
		is.insertionSort(nums);
		
		for (int i: nums)
			System.out.println(i);

	}

}
