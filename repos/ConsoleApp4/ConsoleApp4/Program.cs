using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp4
{
    class Program
    {
        static void Main(string[] args)
        {

            using (FileStream fstream = File.OpenRead(@"C:\Users\SkyLighting\Desktop\C#\files\note.txt"))
            {

                // преобразуем строку в байты
                byte[] array = new byte[fstream.Length];
                // считываем данные
                fstream.Read(array, 0, array.Length);
                // декодируем байты в строку
                //string textFromFile = System.Text.Encoding.Default.GetString(array);
                for (int i = 0; i < fstream.Length; i++)
                {
                    Console.Write("{0} ", array[i]);
                }
                Console.ReadKey();
            }



        }
    }
}
