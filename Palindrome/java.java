//-----------------------------------------		Method   ------------------------------------------------------
public class one {
		static boolean stri(String st)
		{
			int l=st.length();
				for(int i=0;i<l/2;i++){
					if(st.charAt(i)!= st.charAt(l-i-1))
						return false;
				}return true;
		}
	public static void main(String[] args)
	{
			String st = "ammfa";
			System.out.print(stri(st));
	}
}

//-----------------------------------------		Method   ------------------------------------------------------
public class one {
		static boolean stri(String st)
		{
			st=st.toLowerCase();
			int l=st.length();
			int j=l-1;
				for(int i=0;i<l-1;i++){
					if(st.charAt(i)!= st.charAt(j))
						return false;
					j--;
				}return true;
		}
	public static void main(String[] args)
	{
			String st = "MAdam";
			System.out.print(stri(st));
	}
}

