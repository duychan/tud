#include <iostream>
#include <math.h>
using namespace std;
float M[10][10];
float temp[10][10];
float l1,l2; 

void giaiPT(float a, float b, float c){
    float delta = b*b - 4*a*c;
    if(delta<0){
        l1=l1=0.0;
    }
    else if(delta==0){
        l1 = l2 = -b/(2*a);
    }
    else{
        delta = sqrt(delta);
        l1 = (-b + delta) / (2*a);
        l2 = (-b - delta) / (2*a);
    }
}
void nghichdao(float A[][10] , int n)
{
	float detA = A[0][0] * A[1][1] - A[0][1] * A[1][0];
	if (detA == 0)	cout << "Ma tran A k the nghich dao ! " << endl;
	else
	{
		temp[0][0] = A[1][1];
		temp[1][1] = A[0][0];
		temp[0][1] = -A[0][1];
		temp[1][0] = -A[1][0];
	}
	cout << "Ma tran V : " << endl;
	for ( int i = 0 ; i < n ; i++)
	{
		for (int j = 0; j < n ; j++)
		{
			cout << temp[i][j] << "   ";
		}
		cout << endl;
	}
	cout << "Nghich dao cua ma tran la : " << endl;
	for ( int i = 0 ; i < n ; i++)
	{
		for (int j = 0; j < n ; j++)
		{
			temp[i][j] = 1/detA * temp[i][j];
		}
	}
	for ( int i = 0 ; i < n ; i++)
	{
		for (int j = 0; j < n ; j++)
		{
			cout << temp[i][j] << "   ";
		}
		cout << endl;
	}
}

void NhanMaTran(float A[][10] , float B[][10],float C[][10],int n)
{
	float kq[n][n];
	int i , j , k;
	for( i = 0; i < n; ++i)
        for( j = 0; j < n; ++j)
            for( k = 0; k < n; ++k)
            {
                M[i][j] += A[i][k] * B[k][j];
            }
    for( i = 0; i < n; ++i)
        for( j = 0; j < n; ++j)
            for( k = 0; k < n; ++k)
            {
                kq[i][j] += M[i][k] * C[k][j];
            }
    cout << "Ma tran A phan ra : " << endl;
    for(i = 0 ; i < n ; i++)
	{
		for (j = 0 ; j < n ; j++)
		{
			cout << kq[i][j] << " ";
		}
		cout << endl;
	}
}

int main()
{
	int i,j,n=2;
	float det;
	float A[10][10];
	float V[10][10];
	float T[10][10];
	cout << "Nhap vao mang 2 chieu : " << endl;
	for ( i = 0 ; i < n ; i++ )
	{
		for ( j = 0 ; j < n ; j++)
		{
			cout << "Nhap A[" << i << "][" << j << "] = ";
			cin >> A[i][j];
		}
	}
	det = A[0][0] * A[1][1] - A[1][0] * A[0][1];
	float b = A[0][0] + A[1][1];
	giaiPT(1,-b,det);
	cout << "Chi so rieng 1 : " << l1 << endl;
	cout << "Chi so rieng 2 : " << l2 << endl;
	float x = (A[0][0] - l1);
	float y = (-A[0][1]);
	float z = (A[0][0] - l2);
	cout << "Vector rieng  1 : \n [" << y << "\n" << x << "]" << endl;
	cout << "Vector rieng  2 : \n [" << y << "\n" << z << "]" << endl;
	float lamda[2] = {l1,l2};
	V[0][0] = y ; V[1][0] = x ; V[0][1] = x ; V[1][1] = z;
	for ( i = 0 ; i < n ; i++)
	{
		for (j = 0 ; j < n ; j++)
		{
			if(i==j) T[i][j] = lamda[i];
			else T[i][j] = 0;
		}
	}
	cout << "Diag(lamda) la : " << endl;
	for ( i = 0 ; i < n ; i++)
	{
		for (j = 0 ; j < n ; j++)
		{
			cout << T[i][j] << " ";
		}
		cout << endl;
	}
	nghichdao(V,n);
	for(i = 0 ; i < n ; i++)
	{
		for (j = 0 ; j < n ; j++)
		{
			M[i][j] = 0;
		}
	}
	NhanMaTran(V,T,temp,n);
	return 0;
}
