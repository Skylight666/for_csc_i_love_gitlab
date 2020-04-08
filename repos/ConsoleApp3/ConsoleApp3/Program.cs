using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp3
{
    class Glob
    {
        public static int k = 0;
    }
    class Program
    {
        private int k = 0;
        public static int Algo(int b)
            {
                
                if (b == 1)
                {
                    return Glob.k; 
                }
                else
                {
                Glob.k = ++Glob.k;
                    Algo (b % 2 == 0 ? b / 2 : (3 * b + 1) / 2);
                    return Glob.k;
                }
            }
        static void Main(string[] args)
        {
            int p = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine(Algo(p));
            Console.ReadKey();
        }
    }
}
