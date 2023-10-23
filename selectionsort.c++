// Online C++ compiler to run C++ program online
#include <iostream>

using namespace std;

void insertionsort(int arr[],int n) {
    // Write C++ code here
    
    bool a = true;
    int i = 0;
    
    
    while(a!=false){

        a = false;
        int index = arr[i];
        for (int j = i+1; j <n;j++){
            
            if(index>arr[j]){
               
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j]=temp;
                a = true;
                break;
            }
        }
        
        if(a==false){
            i = i+1;
            a = true;
            if(i==n){
                a = false;
            }
        }
       
    }
    

}
int main(){
    
    int arr[] = {6,5,4,2,24,3};
    int  n = sizeof(arr)/sizeof(arr[0]);
    for (int i = 0 ; i<n;i++){
        cout<<arr[i]<<" ";
    }
    
    cout<<endl;
    insertionsort(arr,n);
    for (int i = 0 ; i<n;i++){
        cout<<arr[i]<<" ";
    }
}
