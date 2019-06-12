using IntroSortName;
using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Text;

namespace SortMethod
{
    class Test
    {
        public void test()
        {
            Stopwatch timePerParse;
            var numbers = 16;
            long ticksThisTime = 0;

            int[] datata = new int[numbers];
            for (int i = 0; i < numbers; i++)
            {
                Random random = new Random();
                var number = random.Next(0, 10000);
                datata[i] = number;

            }
            var data2 = new int[datata.Length];
            var data3 = new int[datata.Length];
            var data4 = new int[datata.Length];
            var data5 = new int[datata.Length];
            datata.CopyTo(data2, 0);
            datata.CopyTo(data3, 0);
            datata.CopyTo(data4, 0);
            datata.CopyTo(data5, 0);

            timePerParse = Stopwatch.StartNew();
            SortClass.Sort(ref datata);
            timePerParse.Stop();
            ticksThisTime = timePerParse.ElapsedTicks;
            Console.WriteLine("MainSort     " + ticksThisTime);


            timePerParse = Stopwatch.StartNew();
            SortClass.QuickSort(ref data2, data2[0], data2.Length - 1);
            timePerParse.Stop();
            ticksThisTime = timePerParse.ElapsedTicks;
            Console.WriteLine("QuickSort     " + ticksThisTime);


            timePerParse = Stopwatch.StartNew();
            SortClass.InsertionSort(ref data4);
            timePerParse.Stop();
            ticksThisTime = timePerParse.ElapsedTicks;
            Console.WriteLine("InsertionSort     " + ticksThisTime);

            timePerParse = Stopwatch.StartNew();
            SortClass.HeapSort(ref data5);
            timePerParse.Stop();
            ticksThisTime = timePerParse.ElapsedTicks;
            Console.WriteLine("HeapSort      " + ticksThisTime);
        }
    }
}
