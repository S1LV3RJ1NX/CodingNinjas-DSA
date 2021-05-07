vector<int> majorityElementII(vector<int> &arr)
{
    //    Write your code here
    int ct1=0, ct2=0, candidate1=0, candidate2=0;
    int length = arr.size();
    for(int i=0; i<length; i++)
    {
        if(arr[i]==candidate1)
            ct1++;
        else if(arr[i]==candidate2)
            ct2++;
        else if(ct1==0)
        {
            candidate1 = arr[i];
            ct1 = 1;
        }
        else if(ct2==0)
        {
            candidate2 = arr[i];
            ct2 = 1;
        }
        else
        {
            ct1--;
            ct2--;
        }
    }
    
    
    int count_c1=0, count_c2=0;
    for(auto& it: arr)
    {
        if(it==candidate1)
            count_c1++;
        else if(it==candidate2)
            count_c2++;
    }
    vector <int> ans;
    if(count_c1 > length/3)
        ans.push_back(candidate1);
    if(count_c2 > length/3)
        ans.push_back(candidate2);
    return ans; 
}