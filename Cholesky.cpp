#include<iostream>
#include<math.h>
using namespace std;
void input(int n,int a[100][100]){

 for(int i = 0; i < n; i++){
 for(int j = 0; j < n; j++){
 cout << "a[" <<i<<"][" <<j<<"] = ";
 cin >> a[i][j];
 }
 }
}
void output(int n, float a[100][100]){
 for(int i = 0; i < n; i++){
 for(int j = 0; j < n; j++){
 cout << a[i][j] << " ";
 }
 cout << endl;
 }
}
void cholesky(int n, int a[100][100],float f[100][100]){
 for(int i = 0; i < n; i++){
 for(int j = 0; j < n; j++){
 f[i][j] = 0;
 }
 }
 for(int i = 0; i < n; i++){
 for(int j = 0; j < n; j++){
 if(i == j){
 float s = 0;
 for(int k = 0; k < j - 1; k++){
 s += pow(f[i][k],2);
 }
 f[i][j] = sqrt(a[i][j]-s);
 }
 else{
 float s = 0;
 for(int k = 0; k < j -1; k++){
 s += f[i][k]*f[j][k];
 }
 f[i][j] = (1.0/f[j][j]) * (a[i][j] - s);
 }
 }
 }
}
int main(){
 int n;
 int a[100][100];
 float f[100][100];
 cout << "input n: "; cin >> n;
 input(n,a);
 cholesky(n,a,f);
 output(n,f);
 return 0;
}
