package com.company;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
	// write your code here
        Scanner sc = new Scanner(System.in);
        System.out.println("  ENTER SCIENCE MARKS  :");
        float sub1 = sc.nextFloat();
        System.out.println("  ENTER MATHS MARKS  :");
        float sub2 = sc.nextFloat();
        System.out.println("  ENTER SST MARKS  :");
        float sub3 = sc.nextFloat();
        System.out.println("  ENTER ENGLISH MARKS  :");
        float sub4 = sc.nextFloat();
        System.out.println("  ENTER HINDI MARKS  :");
        float sub5 = sc.nextFloat();
        float result = (sub1+sub2+sub3+sub4+sub5)/500*100;
        System.out.println("  FINAL RESULT : PASS ");
        System.out.println(result);

    }
}
