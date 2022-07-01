//-----------------------------------------		Method --strings input   ------------------------------------------------------
public class one {
	static int getSum(String str)
	{
			int sum = 0;
			// Traversing through the string
			for (int i = 0; i < str.length(); i++) {
					// Since ascii value of  numbers starts from 48  so we subtract it from sum
					sum = sum + str.charAt(i) - 48;
			}
			return sum;
	}
	public static void main(String[] args)
	{
			String st = "125";
			System.out.print(getSum(st));
	}
}

//-----------------------------------------		Method   ------------------------------------------------------
public class one {
	static int getSum(int n)
	{
			int sum = 0;a
			while (n != 0) 
			{
					sum = sum + n % 10;
					n = n / 10;
			}
			return sum;
	}
		public static void main(String[] args)
	{
			int n = 125;
			System.out.println(getSum(n));
	}
}

//-----------------------------------------		Method   ------------------------------------------------------
public class one {
	static int getSum(int n)
    {
        int sum;
        for (sum = 0; n > 0; sum += n % 10, n /= 10) ;
        return sum;
    }
		public static void main(String[] args)
	{
			int n = 125;
			System.out.println(getSum(n));
	}
}
//-----------------------------------------		Method   ------------------------------------------------------
public class one {
	static int sumDigits(int no)
    {
        if(no == 0){
          return 0 ;
        }
        return (no % 10) + sumDigits(no / 10) ;
     }
 
    // Driver code
    public static void main(String[] args)
    {
        System.out.println(sumDigits(680));
    }
}
