// C++ implementation of search and insert
// operations on Trie
#include <bits/stdc++.h>
using namespace std;

const int ALPHABET_SIZE = 128;

// trie node
struct TrieNode
{
    struct TrieNode *children[ALPHABET_SIZE];

    // isEndOfWord is true if the node represents
    // end of a word
    vector<string> data;
    bool isEndOfWord;
};

// Returns new trie node (initialized to NULLs)
struct TrieNode *getNode(void)
{
    struct TrieNode *pNode = new TrieNode;

    pNode->isEndOfWord = false;

    for (int i = 0; i < ALPHABET_SIZE; i++)
        pNode->children[i] = NULL;

    return pNode;
}

// If not present, inserts key into trie
// If the key is prefix of trie node, just
// marks leaf node
void insert(struct TrieNode *root, string key, string data)
{
    struct TrieNode *pCrawl = root;

    for (int i = 0; i < key.length(); i++)
    {
        int index = key[i];
        if (!pCrawl->children[index])
            pCrawl->children[index] = getNode();
        pCrawl->children[index]->data.push_back(data);
        pCrawl = pCrawl->children[index];
    }

    // mark last node as leaf
    pCrawl->isEndOfWord = true;
}

void insert_key(struct TrieNode *root, string key)
{
    string data = key;
    while (key.length() > 0)
    {
        insert(root, key, data);
        key.erase(0, 1);
    }
}

vector<string> get_data(struct TrieNode *root, string key)
{
    struct TrieNode *pCrawl = root;
    for (int i = 0; i < key.length(); i++)
    {
        int index = key[i];
        if (!pCrawl->children[index])
        {
            vector<string> ans;
            ans.push_back("None");
            return ans;
        }
        pCrawl = pCrawl->children[index];
    }
    return pCrawl->data;
}

// Returns true if key presents in trie, else
// false
bool search(struct TrieNode *root, string key)
{
    struct TrieNode *pCrawl = root;

    for (int i = 0; i < key.length(); i++)
    {
        int index = key[i];
        if (!pCrawl->children[index])
            return false;

        pCrawl = pCrawl->children[index];
    }

    return (pCrawl->isEndOfWord);
}
struct TrieNode *rt = getNode();
// Driver

extern "C" void insert_trie(char *key)
{
    string new_key(key);
    insert_key(rt, new_key);
    cout << "Add complete!" << endl;
}

extern "C" void get_data_trie(char *key)
{
    string new_key(key);
    vector<string> res = get_data(rt, new_key);
    for (int i = 0; i < res.size(); i++)
        cout << res[i] << endl;
}

// int main()
// {
//     // Input keys (use only 'a' through 'z'
//     // and lower case)
//     string keys[] = {"the", "a", "there",
//                      "answer", "any", "by",
//                      "bye", "their"};
//     int n = sizeof(keys) / sizeof(keys[0]);

//     // Construct trie
//     for (int i = 0; i < n; i++)
//         insert_trie(keys[i]);

//     // Search for different keys
//     search(rt, "the") ? cout << "Yes\n" : cout << "No\n";
//     vector<string> res = get_data_trie("the");
//     for (int i=0;i<res.size();i++)
//         cout<<res[i]<<endl;
//     search(rt, "these") ? cout << "Yes\n" : cout << "No\n";
//     return 0;
// }
