using System;

namespace ConsoleApp2
{
    class Program
    {
        static void Main(string[] args)
        {
            byte m, n;
            m = Convert.ToByte(Console.ReadLine());
            n = Convert.ToByte(Console.ReadLine());
            Console.WriteLine((m*n) % 2 == 0 ? "First" : "Second");
            Console.ReadKey();
        }
    }
}
