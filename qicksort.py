#include <iostream>
using namespace std;


int subdivide(int arr[],int a, int b)  //array break
{
    int pivot = arr[b];//rightmost
    int i = (a-1);
    for (int j = a; j < b-1; j++)
    {
        if (arr[j] < pivot)
        {
            i++;
            int temp = arr[j];
            arr[j] = arr[i];
            arr[i] = temp;

        }
    }

    int temp2 = arr[i+1];
    arr[i+1] = arr[b];
    arr[b] = temp2;
    return i + 1;
}


void quickSort(int arr[],int a,int b)
{
    if (a < b) 
    {
        int pivot = subdivide(arr,a,b);

        quickSort(arr, a, b-1); //before
        quickSort(arr,a+1,b);//after
    }
}

int main()
{

    // Write C++ code here
    int a[] = { 34,1,22,12,26,23,4,2 };

    int n = (sizeof(a) / sizeof(a[0]));

    for (int i = 0; i < n; i++) {
        cout << a[i] << " ";
    }


    quickSort(a,0,n-1);

    cout <<endl;
    for (int i = 0; i < n; i++) {
        cout << a[i] << " ";
    }
 
    return 0;
}
