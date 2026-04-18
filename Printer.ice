module Demo
{
    sequence<double> DoubleSeq;

    interface Printer
    {
        string printString(string s);
        int sum(int a, int b);
        double average(DoubleSeq values);
        string reverseString(string s);
    }
}
