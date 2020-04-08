using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Vvedi chislo");
            string a = Console.ReadLine();
            int x = Convert.ToInt16(a);
            Console.WriteLine(x*x*x);
            Console.ReadKey();
            
        }
    }
}
