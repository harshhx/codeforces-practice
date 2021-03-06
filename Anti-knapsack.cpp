#include<bits/stdc++.h>
using namespace std;
#define mem(x,y) memset(x,y,sizeof(x))
#define pb push_back
#define mp make_pair
#define ff first
#define ss second
#define MOD 1000000007
#define PI 3.141592653589793
#define setBitCount(x) __builtin_popcount(x)
#define all(a) (a).begin(), (a).end()
#define all_r(a) (a).rbegin(), (a).rend()
#define sz(x) (int)(x.size())
#define endl  '\n'
typedef long long ll;
typedef unsigned long long ull;
typedef long double lld;
 
const int mXn = 2e5 + 7;
ll gcd(ll a, ll b) {if (b > a) {return gcd(b, a);} if (b == 0) {return a;} return gcd(b, a % b);}
void fastIO() { ios_base::sync_with_stdio(false); cin.tie(NULL);}
ll LCM(ll a, ll b) {return a * b / gcd(a, b);}
ll expo(ll a, ll b, ll mod) {ll res = 1; while (b > 0) {if (b & 1)res = (res * a) % mod; a = (a * a) % mod; b = b >> 1;} return res;}
void google(ll t ,ll ans){
   cout<<"Case #"<<t<<": "<<ans<<endl;
   return ;
}
 
void solve() {
    int t, n,m,x,y,k;
    // write code here
    cin>>t;
    while(t--){
        cin>>n>>k;
        vector<ll>v;
        for(int i=k+1;i<=n;i++){
            v.pb(i);
        }
        set<ll>s;
        for(int i=k-1;i>=1;i--){
            if(s.find(k-i)==s.end()){
                v.pb(i);
                s.insert(i);
            }
 
        }
        cout<<v.size()<<endl;
        for(auto child:v){
            cout<<child<<" ";
        }cout<<endl;
    }
    return ;
}
int main() {
#ifndef ONLINE_JUDGE
 
    freopen("input.txt", "r", stdin);
 
    freopen("output.txt", "w", stdout);
    freopen("error.txt", "w", stderr);
#endif
    fastIO();
    solve();
    return 0;
}