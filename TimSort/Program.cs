using System;
using System.Collections.Generic;

namespace TimSort
{
    class Program
    {

        const int INSERTION_RUN = 32;

        static void swap(int[] array, int position1, int position2)
        {
          
            int temp = array[position1]; 
            array[position1] = array[position2]; 
            array[position2] = temp; 
        }
        public void insertionSort(int[] array, int length)
        {
          //  int length = array.Length;
            for (int i = 0; i < length; i++)
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

        public void mergeArrays(int [] array, int left, int right, int mid)
        {
            int leftSize = mid - left + 1;
            int rightSize = right - mid;
            //two arrays for merging
            int[] leftMinArray = new int[leftSize];
            int[] rightMinArray = new int[rightSize];
            //add values to arrays
            for (int i = 0; i < leftSize; i++)
                leftMinArray[i] = array[left + i];
            for (int j = 0; j < rightSize; j++)
                rightMinArray[j] = array[mid + 1 + j];

            int p1 = 0;
            int p2 = 0;
            int p3 = 0;

            //start mergint two arrays to large one
            while(p1<leftSize&& p2<rightSize)
            {
                if(leftMinArray[p1]<=rightMinArray[p2])
                {
                    array[p3] = leftMinArray[p1];
                    p1++;
                }
                else
                {
                    array[p3] = rightMinArray[p2];
                    p2++;
                }
                p3++;
            }


            // if some elements remained in left aray
            //just insert them 
            while(p1<leftSize)
            {
                array[p3] = leftMinArray[p1];
                p1++;
                p3++;
            }

            //insert elments from right array
            while (p2 < rightSize)
            {
                array[p3] = rightMinArray[p2];
                p2++;
                p3++;
            }

        }


        public static int  getMinRunSize(int n)
        {
            int r = 0;//will be 1 if there at least one bit = 1
            while(n>=64)
            {
                r |= n & 1;
                n >>= 1;
            }
            return n + r;
        }

        public void timSort(int [] array, int n)
        {
            int size= array.Length;
            int MinSize = getMinRunSize(size);
            var minRunArray = new int[] { };
            Stack <int> minRunArray2 = new Stack<int>();
            int currentPosition = 0;
            while (currentPosition < size - 1)
            {
                int currentMinRunPosition = currentPosition;
                int nextPosition = currentMinRunPosition + 1;
                if (array[currentMinRunPosition] > array[nextPosition])
                    swap(array, currentMinRunPosition, nextPosition);
                bool goNext = true;
                while(goNext)
                {
                    if (array[currentMinRunPosition] > array[nextPosition - 1]
                        || currentMinRunPosition == size - 1)
                        goNext = false;
                    else if ((currentMinRunPosition - currentPosition) < MinSize)
                        goNext = true;
                    if(goNext)
                    {
                        ++currentMinRunPosition;
                        ++nextPosition;
                    }
                }
                int lengForSubArrays = (currentMinRunPosition + 1) - currentPosition;
                insertionSort(array, lengForSubArrays);
                for (int i = currentPosition; i < currentMinRunPosition - currentPosition; i++)
                {
                    minRunArray2.Push(i);
                    currentPosition = currentMinRunPosition;
                }
                while(minRunArray2.Count>1)
                {
                    int k = minRunArray2.Pop();
                    int y = minRunArray2.Pop();
                    if (k > y)
                    {
                        int temp = k;
                        k = y;
                        y = temp;
                    }
                

            
            }
        }
        sortInsertionPart(a, currentIndex, currentRunIndex+1);
        Range r = new Range();
        r.start = currentIndex;
            r.length = currentRunIndex - currentIndex;
 
            minrunStack.add(r);
 
            currentIndex = currentRunIndex;
        }
 
        while (minrunStack.size() > 1)
        {
            Range x = minrunStack.elementAt(0);
    minrunStack.remove(minrunStack.firstElement());
            Range y = minrunStack.elementAt(0);
    minrunStack.remove(minrunStack.firstElement());
            if (x.start > y.start) {
                int temp = x.start;
    x.start = y.start;
                y.start = temp;
 
                temp = x.length;
                x.length = y.length;
                y.length = temp;
            }
            if (y.start != x.start+x.length)
            {
                minrunStack.add(y);
                minrunStack.add(x);
                continue;
            }
            merge(a, x.start, x.length, y.start, y.length);
x.length = x.length + y.length;
            minrunStack.add(x);
        }
    }

          
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
        }
    }
}
