
public class SelectionSort {
	
	public void selectionSort (int[] arr) {
				
		int index = 0, temp = 0;		
		
		for (int i=0; i < arr.length; i++) {
			
			int min = Integer.MAX_VALUE;
			
			for (int j=i; j < arr.length; j++) {
				
				if (arr[j] < min) {
					min = arr[j];
					index = j;
				}
				
			}
			
			// swap the elements
			
			temp = arr[i];
			arr[i] = arr[index];
			arr[index] = temp;
		}
		
		
		
		
		
	}

	public static void main(String[] args) {
		SelectionSort ss = new SelectionSort();
		
		int[] nums = {1, 10, 5, 8, 7, 6, 4, 3, 2, 9};
		
		for (int i: nums)
			System.out.println(i);
		
		System.out.println("=====");
		
		ss.selectionSort(nums);
		
		for (int i: nums)
			System.out.println(i);

	}

}
