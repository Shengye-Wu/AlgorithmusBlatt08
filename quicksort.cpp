#include <stdlib.h>
#include <stdio.h>
#include<iostream>
#include <cassert>
using namespace std;
#include <time.h>
#include <unistd.h>
#include <stdbool.h>

/*
The functionality in C is too primal, therefore this quicksort
is completed through switching the elements in the already existing
array recursively.
We'll need two pointers  for recursive call to traverse correctly 
without doing append or concatenation.
Notice that the "A=" part always has one element in this variant 
to make it simpler.
Correctness is similar to the variante in lecture, tested in other document.
*/ 
void quicksort(int array[], int left, int right){
/*
Divide elements in array[left:right] into A<= and A>=,
with pointer i standing at the edge at last.
Then switch the pivot with the element at the edge, sothat
the array is splitted into A<=, A= and A>=.
The algorithm always terminates because one element in A= will always
be fixed and no more taken care in further recursive calls.
*/
    int pivot = array[left];
    int i = left;
    int j = right; // two pointers to traverse in two directions
    int t; // switch mediate
    if (i > j)
    {
        return; // Start of recursion
    }
    
    while (i != j)
    {
        /*
        Use two while loops to search for single pair of element to switch
        if they both meet inappropriate element, the two loops break, (1)
        if they meet each other, the two loops also break. (2)
        */
        while (array[j] >= pivot && i<j)
        {
            j--;
        }
        while (array[i] <= pivot && i<j)
        {
            i++;
        }
        if (i < j) // Check if the loops stopped for case (1)
        { // in case (1) switch the two pointed elements
            t = array[i];
            array[i] = array[j];
            array[j] = t;
        }
    }
        // set the pivot in the middle
        array[left] = array[i];
        array[i] = pivot;

        //recursive call, position i is A=
        quicksort(array, left, i-1);
        quicksort(array, i+1, right);
        return;
}

int main(){
//-------------------------Test Correctness------------------------
int arr1[] = {1,2,5,4,3};
int arr1_exp[] = {1,2,3,4,5};
quicksort(arr1, 0, 4);
assert(equal(arr1, arr1+5, arr1_exp));

int arr2[] = {};
int arr2_exp[] = {};
quicksort(arr2, 0, 0);
assert(equal(arr2, arr1+0, arr2_exp));

int arr3[] = {1};
int arr3_exp[] = {1};
quicksort(arr3, 0, 0);
assert(equal(arr3, arr3+1, arr3_exp));

int arr4[] = {25, 42, 26, 42, 1, 41, 42, 40, 43};
int arr4_exp[] = {1, 25, 26, 40, 41, 42, 42, 42, 43};
quicksort(arr4, 0, 8);
assert(equal(arr4, arr4+9, arr4_exp));
//------------------------Time Analysis---------------------------
int array_sizes[11] = {10, 100, 500, 1000, 1500, 2000, 2500, 3000, 5000, 7500, 10000};
double q_times[11] = {};
double time_spent;
int arrs[11][10000];
struct timespec start, end;
for (int i = 0; i < 11; i++)
{   // generate arrays
    for (int j = 0; j < array_sizes[i]; j++)
    {
        arrs[i][j] = rand() % 100000;
    }
}
for (int i = 0; i < 11; i++)
{  // record running times
    clock_gettime(CLOCK_REALTIME, &start);
    quicksort(arrs[i], 0, array_sizes[i]-1);
    clock_gettime(CLOCK_REALTIME, &end);
    time_spent = (end.tv_nsec - start.tv_nsec);
    cout << time_spent/ 1000000  << " ";
    q_times[i] = time_spent;
}

    }