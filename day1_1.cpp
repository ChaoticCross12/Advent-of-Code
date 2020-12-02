#include <iostream>
#include <vector>

using namespace std;


int main()
{
    int number, i, j;
    long long int prod;
    vector<int> list;
    bool timeToGo = false;

    while (cin >> number)
    {
        list.push_back(number);
    }

    for (i = 0; i < list.size() - 1; i++)
    {
        for (j = i + 1; j < list.size(); j++)
        {
            if ((list[i] + list[j]) == 2020)
            {   prod = 1ULL * list[i] * list[j];
                timeToGo = true;
                cout << "reached 2nd break" << endl;
                break;
            }
        }

        if (timeToGo)
            break;
        
    }
    
    prod = 1ULL * list[i] * list[j];
    cout << prod << endl << list[i] << " " << list[j] << " " << i << " " << j;



    return 0;
}