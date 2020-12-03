#include <iostream>
#include <vector>

using namespace std;


int main()
{
    int number, i, j, k;
    long long int prod;
    vector<int> list;
    bool timeToGo = false;

    while (cin >> number)
    {
        list.push_back(number);
    }

    for (i = 0; i < list.size() - 2; i++)
    {
        for (j = i + 1; j < list.size() - 1; j++)
        {
            for(k = j + 1; k < list.size(); k++)
            {
                if ((list[i] + list[j] + list[k]) == 2020)
                {   
                    prod = 1ULL * list[i] * list[j] * list[k];
                    timeToGo = true;
                    break;
                }
                
                
            }
            if (timeToGo)
                break;
        }

        if (timeToGo)
            break;
        
    }
    
    prod = 1ULL * list[i] * list[j] * list[k];
    cout << prod << endl << list[i] << " " << list[j] << " " << list[k] << " " << i << " " << j << " " << k;



    return 0;
}