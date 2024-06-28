#include <iostream>
#include<vector>
using namespace std;
int main()
{
    int m;
    int n;
    cout<<"Enter the number of edges : ";
    cin>>m;
    cout<<"Enter the number of vertices  : ";
    cin>>n;
    vector<int>adj[n];
    for(int i=0;i<m;i++)
    {
        int v;
        int u;
        cin>>u;
        cin>>v;
        adj[u].push_back(v);
        adj[v].push_back(u);        
    }
    for(int i=0;i<m;i++)
    {
        for(auto it : adj[i])
        {
            cout<<i;
            cout<<"->";
            cout<<it<<",";
        }
        cout<<endl;
    }
   return 0;
    // vector<vector<pair<int,int>>>adj(n);
    // cout<<"Enter the number of edges : ";
    // cin>>m;
    // cout<<"Enter the number of vertices  : ";
    // cin>>n;
    // for(int i=0;i<m;i++)
    // {
    //     int v;
    //     int u;
    //     int w;
    //     cin>>u;
    //     cin>>v;
    //     cin>>w;
    //     adj[u].push_back(make_pair(v,w));
    //     adj[v].push_back(make_pair(u,w));
    // }

    // for(int i=0;i<n;i++)
    // {
    //     for(auto it: adj[i])
    //     {
    //         int p=it.first;
    //         int w=it.second;
    //         cout<<p;
    //         cout<<endl;
    //         cout<<w;
    //         cout<<endl;
    //     }
    //     cout<<endl;
    // }


//     int n;
//     int m;
//     cout<<"Enter the number of edges : ";
//     cin>>m;
//     cout<<"Enter the number of vertices  : ";
//     cin>>n;
//     vector<vector<int>>adj(n);
//     for(int i=0;i<m;i++)
//     {
//         int v;
//         int u;
//         cin>>u;
//         cin>>v;
//         adj[u].push_back(v);
//         adj[v].push_back(u);        
//     }
//     for(int i=0;i<m;i++)
//     {
//         for(auto it : adj[i])
//         {
//             cout<<i;
//             cout<<"->";
//             cout<<it<<",";
//         }
//         cout<<endl;
//     }
//    return 0;
}