package Java;
//Problem Description: given a signed int input, return the digits-reversed int, if the number overflows, return 0
//Int range = -214748364 to +2147483647

public class ReverseInteger {
    public int reverse(int x) {
        int result = 0;
        int temp = x;
        while(temp!=0){
            if (result > Integer.MAX_VALUE/10 || (result == Integer.MAX_VALUE && (temp%10) > 7) ) return 0; //check for overflow, if the current number is larger than the max value/10, then do not append the next value and return 0
            if (result < Integer.MIN_VALUE/10 || (result == Integer.MIN_VALUE && (temp%10) < -8) ) return 0; // if the current number equals to the max value/10, then check if the next value is larger than 7 or smaller than -8
            
            result = result*10 + temp%10; //push the current digit to the front by multiplying it by 10, and add the next digit by getting the %
            temp=temp/10; //save the current number without the last digit
        }
        return result;
    }
}
