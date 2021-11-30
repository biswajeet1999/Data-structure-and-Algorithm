/*
 * Shell Sort(or n-gape insertion sort or diminishing counting sort)
 * Author:- Biswajeet padhi
 * Date:- 1/12/2019
 * 3rd sem
**/

main()
{
    int n;
    printf("Enter no of elements: ");
    scanf("%d",&n);
    int arr[n];
    int index; /* contains the index of element which is sorting */
    printf("Enter elements:\n");
    for(int i=0;i<n;i++){
        scanf("%d",&arr[i]);
    }
    /* decide gape for each pass */
    for(int gape=n/2; gape>0; gape/=2){
        /* iterate through elements in a gape */
        for(int j=0; j<gape; j++){
            /* compare elements in gape */
            for(int k = j; k < n; k+=gape){
                index = k;
                while(index-gape >= 0){
                    if(arr[index] < arr[index-gape]){
                        int temp = arr[index];
                        arr[index] = arr[index-gape];
                        arr[index-gape] = temp;
                    }
                    index = index-gape;
                }
            }
        }
    }
    for(int i=0;i<n;i++){
        printf("%d ",arr[i]);
    }
    printf("\n");
}
