#include <iostream>
#include <stdio.h>
#include <bits/stdc++.h> 
using namespace std;

int main() {
	int i,j,t,n,p,sum=0;
	cin>>t;
	for(i=0;i<t;i++)
	{
	    sum=0;
	    cin>>n;
	    int arr[n];
	    for(j=0;j<n;j++)
	    {
	        cin>>arr[j];
	    }
	    sort(arr,arr+n);
	    sum=arr[0];
	    for(j=1;j<n;j++)
	    {
	        sum=sum%arr[j];
	    }
	    cout<<sum<<endl;
	}
	return 0;
}
