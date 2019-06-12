using System;
using System.Diagnostics;

namespace IntroSortName
{
    public class SortClass
    {
        static void swap(ref int[] array, int position1, int position2)
        {
            int temp = array[position1];
            array[position1] = array[position2];
            array[position2] = temp;
        }
        public static void Sort(ref int[] array)
        {
            int lengthOfPartition = Partition(ref array, 0, array.Length-1);
            if (lengthOfPartition < 16)
            {
                InsertionSort(ref array);
                Console.WriteLine("InsertionSort used ");
            }
            else if (lengthOfPartition > (2 * Math.Log(array.Length)))
            {
                HeapSort(ref array);
                Console.WriteLine("HeapSort used ");
            }
            else
            {
                QuickSort(ref array, 0, array.Length);
                Console.WriteLine("QuickSort used ");
            }

            }
        public static void InsertionSort(ref int[] array)
        {

            int length = array.Length;
            for (int i = 1; i < length; i++)
            {
                int current = array[i];
                int index = i;

                while (index > 0 && array[index - 1] > current)
                {
                    array[index] = array[index - 1];
                    index--;
                }
                array[index] = current;
            }

        }
        public static void HeapSort(ref int[] array)
        {
            BuildHeap(ref array);
            int heapSize = array.Length - 1;
            for (int i = heapSize; i > 0; --i)
            {
                swap(ref array, i, 0);
                --heapSize;
                Heapify(ref array, heapSize, 0);
            }

        }

        public static void BuildHeap(ref int[] array)
        {
            int heapSize = array.Length;
            int middle = (heapSize - 1) / 2;
            for (int i = middle; i >= 0; --i)
                Heapify(ref array, heapSize, middle);
        }
        public static void Heapify(ref int[] array, int size, int position)
        {
            int left = 2 * (position + 1) - 1;
            int right = 2 * (position + 1);
            int maximum = 0;
            if (left <= size && array[left] > array[position])
                maximum = left;
            else
                maximum = position;
            if (right < size && array[right] > array[maximum])
                maximum = right;
            if (maximum != position)
            {
                swap(ref array, position, maximum);
                Heapify(ref array, size, maximum);
            }

        }
        public static void QuickSort(ref int[] array, int start, int end)
        {
            if (start < end)
            {
                int pivot = Partition(ref array, start, end);
                QuickSort(ref array, start, pivot - 1);
                QuickSort(ref array, pivot + 1, end);
            }
        }

        public static int Partition(ref int[] array, int left, int right)
        {
            int pivot = array[right];
            int i = left;
            for (int j = left; j < right; ++j)
            {
                if (array[j] <= pivot)
                {
                    swap(ref array, j, i);
                    i++;
                }
            }
            array[right] = array[i];
            array[i] = pivot;
            return i;

        }


        public void test(ref int[] array)
        {
            Sort(ref array);
        }

    }
    class Program
    {


        static void Main(string[] args)
        {
            var numbers = 10;
            int[] data = new int[numbers];
            for (int i = 0; i < numbers; i++)
            {
                Random random = new Random();
                var number = random.Next(0, 10000);
                data[i] = number;
             

            }
            SortClass.Sort(ref data);
            foreach (int num in data)
            {
                 Console.WriteLine(num);
             }
             Console.Read();
        }



    }
}
