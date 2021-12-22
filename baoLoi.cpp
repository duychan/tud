#include<iostream>
#define N 1000
using namespace std;
struct point
{
    int x;
    int y;
};
double derminant(point &p, point &q, point &r){
    double d1 , d2 ;
    d1 = q.x * r.y + p.x * q.y + p.y * r.x;
    d2 = q.x * p.y + p.x * r.y + r.x * q.y;
    return d1 - d2;
}
void convexhull(point *a,const int &n){
    point tempPoint, Lup[N], Llow[N];
    cout << "So diem da cho: ";
    for (int i = 1; i <= n; i++){
        cout << "(" << a[i].x << "," << a[i].y <<"),";
    }
    for(int i = 1; i <= n; i++){
        for(int j = i+1; j <= n; j++){
            if(a[i].x > a[j].x || ((a[i].x == a[j].x) && a[i].y > a[j].y)){
                tempPoint = a[i];
                a[i] = a[j];
                a[j] = tempPoint;
            }
        }
    }
    Lup[1] = a[1];
    Lup[2] = a[2];
    int subPoint1  = 2;
    for(int i = 3; i <= n; i++){
        subPoint1++ ; 
        Lup[subPoint1] = a[i];
        while((subPoint1 > 2) && derminant(Lup[subPoint1-2],Lup[subPoint1-1],Lup[subPoint1]) >= 0){
            Lup[subPoint1 - 1] = Lup[subPoint1];
            subPoint1-- ;
        }
    }  
    int subPoint2 = 2;
    Llow[1] = a[n];
    Llow[2] = a[n-1];
    for(int i = n - 2; i > 1; i--){
        subPoint2++; 
        Llow[subPoint2] = a[i];
        while(subPoint2 > 2 && derminant(Llow[subPoint2-2],Llow[subPoint2-1],Llow[subPoint2]) >= 0){
            Llow[subPoint2 - 1] = Llow[subPoint2];
            subPoint2--;
        }
    }
    for(int i = 1; i < subPoint2 -2; i++){
        Lup[subPoint1 + i] = Llow[i + 1];
    }
    int countPoint = subPoint1 + subPoint2 - 2;
    cout << "the vertices: ";
    for(int i = 1; i < countPoint; i++){
        cout << "(" << Lup[i].x << "," << Lup[i].y << ")," ;
    }
    
} 
int main(){
    int n = 10;
    point a1[N] ;
    a1[0] = {0,0};
    for(int i = 1; i <= n ; i++){
        cout << "toa do x: " ; cin >> a1[i].x ; cout << "toa do y: "; cin >> a1[i].y; cout << endl;
    convexhull(a1,n);
    return 0;
}