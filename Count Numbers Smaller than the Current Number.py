import java.util.Scanner;
public class Current
{
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        int cnt=0;
        int n=sc.nextInt();
        int a []=new int [n];
        for(int i=0;i<n;i++)
        {
            a[i] =sc.nextInt();
        }
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<n;j++)
            {
                if(a[i]>a[j])
                {
                    cnt++;
                }
            }
            System.out.printf(cnt+" ");
            cnt=0;
        }
    }
}