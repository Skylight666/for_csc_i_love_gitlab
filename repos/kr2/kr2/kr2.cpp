#include "pch.h"
#include <iostream>
#include "time.h"

using namespace std;

#define EXC(X,Y) { X+=Y;  Y = X - Y; X -= Y; }

int main()
{
    //1.1
	srand(time(NULL));
	int n, m;
	cin >> n >> m;
	int ** arr = new int *[n];
	for (int i = 0; i < n; i++)
	{
		arr[i] = new int[m];
	}
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
		{
			arr[i][j] = rand() % 3;
			cout << arr[i][j] << "\t";
		}

		cout << "\n";
	}

	cout << "______________________" << "\n";

	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m - 1; j++)
		{
			if (!arr[i][j])
			{
				for (int k = j; k < m - 1; k++)
				{
					EXC(arr[i][k], arr[i][k + 1])
				}
			}
		}
	}

	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
		{
			cout << arr[i][j] << "\t";
		}
		cout << "\n";
	}

		
	for (int i = 0; i < n; i++)
	{
		delete[] arr[i];
	}
	delete[] arr;

			


}

