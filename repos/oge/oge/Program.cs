using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace oge
{
    class Program
    {
        static void Main(string[] args)
        {
            int n;
            int summ = 0;
            string c;
            string s;
            c = Console.ReadLine();
            n = Convert.ToUInt16(c);
            for (int i = 0; i < n; i++ )
            {
                c = Console.ReadLine();
                n = Convert.ToUInt16(c);
                if (n % 6 == 0)
                {
                    summ = summ++;
                }
            }
            Console.WriteLine(summ);
            Console.ReadKey();
        }
    }
}
