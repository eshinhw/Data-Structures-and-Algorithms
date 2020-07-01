
public class BubbleSort {
	
	public void bubbleSort (int[] arr) {
		
		int temp;		
		
		for (int i=0; i < arr.length; i++) {
			
			for (int j=0; j < arr.length -1 - i; j++) {				
				
				if (arr[j] > arr[j+1]) {
					temp = arr[j];
					arr[j] = arr[j+1];
					arr[j+1] = temp;
				}
			}
		}
		
		
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		BubbleSort bs = new BubbleSort();
		
		int[] nums = {1, 10, 5, 8, 7, 6, 4, 3, 2, 9};
		
		for (int i: nums)
			System.out.println(i);
		
		System.out.println("=====");
		
		bs.bubbleSort(nums);
		
		for (int i: nums)
			System.out.println(i);

	}

}
